"""패키지와 원본 무변경을 읽기 전용으로 확인하고 결과를 표준 출력에 기록함."""
from pathlib import Path
import hashlib
import json
import re
import zipfile

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent
PKG = OUT / 'plugins/esg-framepack-chatgpt'
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

snapshot = json.loads((OUT / 'original_snapshot.json').read_text(encoding='utf-8-sig'))
for row in snapshot:
    p = ROOT / row['path']
    check(p.is_file(), '원본 누락: ' + row['path'])
    if p.is_file():
        check(digest(p).lower() == row['sha256'].lower(), '원본 내용 변경: ' + row['path'])
        check(p.stat().st_size == row['length'], '원본 크기 변경: ' + row['path'])
        ticks = p.stat().st_mtime_ns // 100 + 621355968000000000
        check(ticks == row['modified'], '원본 수정시각 변경: ' + row['path'])
old = {Path(row['path']).as_posix() for row in snapshot}
actual = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and not p.is_relative_to(OUT)}
check(actual == old, '허용 폴더 밖 파일 목록 변경')

mapping = json.loads((OUT / 'conversion_manifest.json').read_text(encoding='utf-8'))
for row in mapping:
    source, target = ROOT / row['source'], OUT / row['target']
    check(target.is_file(), '변환 파일 누락: ' + row['target'])
    if target.is_file():
        check(digest(target) == row['target_sha256'], '변환본 해시 불일치: ' + row['target'])
    check(digest(source) == row['source_sha256'], '복제 후 원본 해시 변경')
    if row['conversion'] == '바이트 동일 복제':
        check(source.read_bytes() == target.read_bytes(), '복제 무손실 실패')

skills = sorted((PKG / 'skills').iterdir())
check(len(skills) == 4, '스킬 수 불일치')
for skill in skills:
    text = (skill / 'SKILL.md').read_text(encoding='utf-8')
    check('name: ' + skill.name + '\n' in text, '스킬 이름 불일치')
    check('$ARGUMENTS' not in text and '../../' not in text, '이전 실행 경로 잔존')
    for relative in re.findall(r'`((?:references|methodology)/[A-Za-z0-9_/-]+\.md)`', text):
        if 'NN' not in relative:
            check((skill / relative).is_file(), '스킬 참조 누락: ' + relative)
    if skill.name != 'esg-proofread':
        check(len(list((skill / 'references/core').glob('*.md'))) == 23, 'Core 수 불일치')
        check(len(list((skill / 'references/pool').glob('*.md'))) == 37, 'Pool 수 불일치')
        for family in ('core', 'pool'):
            for p in (skill / 'references' / family).glob('*.md'):
                for category, number in re.findall(r'\b(core|pool)-(\d+[ab]?)\b', p.read_text(encoding='utf-8-sig')):
                    check((skill / 'references' / category / (number + '.md')).exists(), '항목 연계 대상 누락')

archives = list(OUT.glob('*.zip'))
for p in archives:
    base = PKG if p.name == 'ESG_FramePack_ChatGPT_Plugin.zip' else PKG / 'skills' / p.stem
    with zipfile.ZipFile(p) as z:
        check(z.testzip() is None, 'ZIP CRC 오류')
        check(set(z.namelist()) == {f.relative_to(base).as_posix() for f in base.rglob('*') if f.is_file()}, 'ZIP 파일 목록 불일치')
        for name in z.namelist():
            check(z.read(name) == (base / name).read_bytes(), 'ZIP 내용 불일치')
check(len(archives) == 5, 'ZIP 수 불일치')
for folder, combined in [('core', '01_Core.md'), ('pool', '02_Pool.md')]:
    text = (OUT / 'project' / combined).read_text(encoding='utf-8')
    for p in (ROOT / 'plugin/esg-framepack/references' / folder).glob('*.md'):
        check(p.read_text(encoding='utf-8-sig') in text, '프로젝트 자료 원문 누락')

market = json.loads((OUT / '.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
entry = market['plugins'][0]
check((OUT / entry['source']['path']).resolve() == PKG, '마켓플레이스 경로 오류')
result = {'status': 'PASS' if not errors else 'FAIL', 'original_files_checked': len(snapshot), 'source_content_and_modified_times_unchanged': not any('원본' in e for e in errors), 'mapped_files_checked': len(mapping), 'skills': len(skills), 'core_per_reference_skill': 23, 'pool_per_reference_skill': 37, 'archives_checked': len(archives), 'chatgpt_live_test': 'NOT_RUN', 'errors': errors}
print(json.dumps(result, ensure_ascii=True, indent=2))
raise SystemExit(1 if errors else 0)
