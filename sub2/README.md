# 카카오톡 받은 파일 자동 분류기 (Python)

## 프로젝트 개요
지정된 소스 폴더에서 파일 확장자에 따라 사진/문서/영상/압축 등으로 자동 분류해 바탕화면의 폴더로 이동합니다.
- 사진: `.jpg, .jpeg, .png, .gif`
- 문서: `.pdf, .docx, .xlsx, .hwp, .pptx, .txt`
- 영상: `.mp4, .mov, .avi`
- 압축: `.zip`
- 그 외: `기타` 로 이동

## 주요 기능
- 대상 폴더가 없으면 자동 생성
- 파일명 충돌 시 자동으로 `(1)`, `(2)` 숫자 붙여서 이동
- 재귀 탐색(하위 폴더 포함) 옵션
- OneDrive/일반 Desktop 경로 자동 인식

## 사용 방법
```bash
python classify_files.py
>>>>>>> 99a4994 (first commit)
