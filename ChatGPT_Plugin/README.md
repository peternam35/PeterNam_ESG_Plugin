# ESG FramePack — ChatGPT 전환본

작성일: 2026-09-13 · 원본 업무 규칙: v0.3 · 패키지: 0.3.0

클로드 플러그인의 4개 기능과 Core 23개·Pool 37개 자료를 ChatGPT용으로 구성했습니다. 기존 파일을 수정하지 않고 이 폴더에만 새 파일을 만들었습니다. 설치·업로드·공유는 아직 수행하지 않았습니다.

## 설치 방법을 선택해 주세요

### 1. ChatGPT 스킬 업로드 — 개별 설치

ChatGPT에서 **Plugins → Skills → Create → Upload from your computer**가 제공되는 경우 아래 ZIP을 각각 업로드해 주세요. 이 경로는 OpenAI의 공식 Skills 안내에 근거합니다. 스캔 또는 관리자 검토가 끝난 뒤 활성화해 주세요.

| 파일 | 기능 |
|---|---|
| `esg-guide.zip` | 항목별 작성 가이드와 서식 소재 안내 |
| `esg-check.zip` | 사용자 초안의 누락·불충분 점검 |
| `esg-crosscheck.zip` | 계획/실적, 합계, 중복, 원자료 대사 |
| `esg-proofread.zip` | 전문용어를 유지한 설명 교정·번호 정리 |

각 ZIP의 최상위에는 `SKILL.md`가 있으며 필요한 참고자료가 함께 들어 있습니다. 다른 스킬이나 원본 PC 경로에 의존하지 않습니다. 통합 플러그인을 설치한 경우 같은 스킬을 다시 설치할 필요는 없습니다. 업로드 메뉴의 제공 여부는 계정·워크스페이스 권한에 따라 다릅니다.

### 2. 통합 플러그인 — 관리자 배포

`ESG_FramePack_ChatGPT_Plugin.zip`은 `.codex-plugin/plugin.json`, 4개 스킬과 리소스를 포함한 통합 아카이브입니다. 관리자 화면에서 플러그인 아카이브 가져오기를 제공하는 경우 이 파일을 사용해 주세요. 실제 계정에서 이 가져오기 방식은 확인하지 않았습니다.

공식적으로 문서화된 GitHub 마켓플레이스 가져오기를 쓰려면 이 폴더의 `.agents/plugins/marketplace.json`과 `plugins/`를 **함께** 승인된 별도 저장소에 배치해 주세요. 이 작업에서는 저장소 생성·업로드를 수행하지 않았습니다.

1. Workspace settings → Plugins → Add → Import marketplace를 선택해 주세요.
2. Source에 실제 승인된 GitHub 저장소 주소를 입력해 주세요.
3. 이 폴더 내용이 저장소 루트라면 Path를 비워 주세요. 저장소의 `ChatGPT_Plugin` 하위에 배치했다면 Path에 `ChatGPT_Plugin`을 입력해 주세요.
4. 가져오기 결과를 확인하고 워크스페이스의 사용 권한을 설정해 주세요. GitHub 가져오기는 JSON의 설치 정책을 그대로 적용하지 않으므로 관리자 화면에서 설정해야 합니다.

서버·API·MCP·외부 앱은 필요하지 않습니다. OpenAI Verified 표시나 공개 배포 승인을 받은 패키지는 아닙니다.

### 3. 스킬 기능이 없는 계정 — ChatGPT 프로젝트

1. 새 프로젝트 `ESG FramePack`을 만들어 주세요.
2. `project/Instructions.txt`의 내용을 프로젝트 지침에 붙여 넣어 주세요.
3. `project/00_Workflows.md`, `01_Core.md`, `02_Pool.md`, `03_Rules_Methodology.md` 4개를 프로젝트 자료로 업로드해 주세요. ZIP 자체를 지식 자료로 올리지 마세요.
4. 프로젝트 안에서 아래 예시로 시작해 주세요. 점검할 초안은 대화에 별도로 제공해 주세요.

프로젝트 경로는 파일 검색을 통한 대체 사용 방식이며 설치형 스킬과 같은 자동 호출을 보장하지 않습니다. 검색되지 않는 자료는 관련 부분을 직접 첨부해 주세요. GPT 편집 권한이 있는 기존 GPT나 허용된 관리형 워크스페이스에서도 같은 Instructions와 자료를 활용할 수 있지만, 신규 GPT 생성을 기본 설치 방법으로 삼지는 않았습니다.

## 사용 예시

- “안전보건 연간 관리계획서에 무엇을 넣어야 하나요?”
- “Core 14번 용수·폐수 상반기 실적서 초안입니다. 누락을 점검해 주세요.”
- “Core 02 계획서와 Core 22 실적서를 첨부했습니다. 목표값을 대조해 주세요.”
- “이 문장의 전문용어는 유지하고 설명만 쉽게 고쳐 주세요.”

## 원본과 변환 범위

`plugin/esg-framepack`을 동작 기준으로 삼았습니다. `framepack`은 편집 원천, `dist`는 별도 배포 트랙이며, `dist/Output_Spec.md`의 출력 순서·권고 노출 조건은 설치형 플러그인과 다릅니다. 충돌하는 규칙을 섞지 않았습니다. PRD의 초창기 제외 범위보다 실제 v0.3 플러그인의 4개 스킬을 변환 대상으로 삼았습니다.

| 원본 | 변환 |
|---|---|
| `.claude-plugin/plugin.json` | `.codex-plugin/plugin.json`과 로컬 마켓플레이스 카탈로그 |
| guide/check/crosscheck/proofread | 이름에 `esg-`를 붙이고 ChatGPT 입력·리소스 안내 추가 |
| `$ARGUMENTS` | 사용자의 현재 요청 |
| `../../references/`, `../../methodology/` | 스킬 내부의 `references/`, `methodology/` |
| Core·Pool·방법론 문서 | 스킬 안에 바이트 동일 복제; 공통 규칙 파일은 경로만 변환 |
| Claude 평가 실행 설정 | ChatGPT용 수동 프롬프트·성공 기준으로 분리 |

원본의 평가 결과 HTML·실행 로그·기존 ZIP·개발용 빌드 도구는 실행 패키지에 넣지 않았습니다. `dist/Form_Drafts.md`는 원본 스킬이 서식 생성·동봉을 금지하므로 포함하지 않았습니다. 원본 자료 자체는 그대로 남아 있습니다.

초안 자동 작성, 서식 생성, 추정 수치 입력, EcoVadis 점수 예측은 원본과 동일하게 하지 않습니다. 법령·평가기준 내용은 원본 시점의 스냅샷이며 이번 작업에서 법적 정확성을 재검증하거나 내용을 갱신하지 않았습니다.

## 검증 자료

- `original_snapshot.json`: 작업 전 기존 202개 파일의 SHA-256·크기·수정 시각
- `conversion_manifest.json`: 원본과 복제본의 경로·해시·변환 유형
- `Validation_Report.json`: 원본 무변경, 복제 무손실, 경로·ZIP 구조 검사 결과
- `Acceptance_Tests.md`: 실제 ChatGPT에서 실행할 5개 원본 시나리오와 추가 경계 테스트

로컬 재검증은 이 폴더에서 `python -B validate_package.py`로 실행해 주세요. 원본과 같은 위치에서 실행해야 원본 무변경 검사가 가능합니다. `build_package.py`는 최초 생성 기록이며 기존 결과를 덮어쓰지 않도록 재실행 시 중단됩니다. 원본의 빌드 스크립트는 실행하지 않았습니다.

## 공식 문서 — 2026-09-13 확인

- [ChatGPT와 Codex 플러그인](https://help.openai.com/en/articles/20001256)
- [ChatGPT 스킬 업로드](https://help.openai.com/en/articles/20001066)
- [네이티브 매니페스트와 마켓플레이스 구조](https://learn.chatgpt.com/docs/enterprise/plugin-management)
- [GitHub 마켓플레이스 가져오기](https://help.openai.com/en/articles/20001504)
- [ChatGPT 프로젝트](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt)

최신 안내에서는 ChatGPT도 스킬 기반 플러그인을 지원합니다. 기존 `dist/ChatGPT_GPT_Setup.md`의 “플러그인 파일 형식이 없다”는 문구를 새 안내에는 적용하지 않았습니다. 설치 기능은 계정·역할·워크스페이스별로 다르므로 실제 설치와 모델 응답은 현장에서 검증해야 합니다.
