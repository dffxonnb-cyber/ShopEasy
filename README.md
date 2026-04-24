# ShopEasy

## Website

- Public site: [https://dffxonnb-cyber.github.io/ShopEasy/](https://dffxonnb-cyber.github.io/ShopEasy/)
- 참고: 저장소를 `Public`으로 전환하거나, 비공개 Pages를 지원하는 요금제를 사용해야 외부에서 열립니다.

## GitHub Pages 설정

- 권장: `Settings > Pages > Source`를 `Deploy from a branch`로 두고 `main` / `/(root)`를 선택합니다.
- 대안: 이미 Actions 방식으로 운영하고 싶다면 `Settings > Pages > Source`를 `GitHub Actions`로 설정합니다.
- 배포 워크플로는 `looker-dashboard` 폴더만 Pages 아티팩트로 올리도록 구성되어 있습니다.
- 배포 아티팩트의 최상단에 `index.html`과 `404.html`이 배치되도록 수정되어 404 가능성을 줄였습니다.
- 브랜치 배포를 써도 루트에 `index.html`과 `404.html`이 있어서 바로 게시 가능합니다.

## 포함 내용

- `index.html`: 저장소 루트에서 바로 열리는 웹사이트 진입점
- `looker-dashboard/`: 실제 대시보드 자산과 렌더링 스크립트
- `dataset/`: 더미 원본 CSV 데이터

## 미리보기 방식

- 로컬: `index.html`을 브라우저에서 직접 열기
- GitHub Pages: 저장소 공개 후 Pages를 켜면 정적 사이트로 사용 가능

## 대시보드 특징

- Looker 스타일 레이아웃
- 한글 깨짐 방지를 위한 UTF-8 기반 구성
- KPI 카드, 월별 주문, 카테고리 완료율, 진입 페이지 전환, 디바이스 성과, 연령대 이탈률 포함
