# ShopEasy 통합 웹 대시보드

ShopEasy는 2025년 3분기 이커머스 주문, 전환, 이탈 흐름을 한 화면에서 점검할 수 있도록 만든 서비스 지표 분석 대시보드입니다. 주문 감소를 단순 유입 감소로만 보지 않고, 카테고리, 진입 페이지, 디바이스, 연령대, 이탈 페이지 관점으로 나누어 구매 완료 흐름의 병목을 정리했습니다.

- Live Dashboard: [dffxonnb-cyber.github.io/ShopEasy](https://dffxonnb-cyber.github.io/ShopEasy/)
- Repository Description: 2025년 3분기 이커머스 주문·전환·이탈 흐름을 분석한 ShopEasy 웹 대시보드.
- Project Type: E-commerce analytics / conversion analysis / web dashboard
- Data Type: 주문 데이터, 사용자 데이터, 세션 데이터
- Role: 데이터 설계, 지표 산출, 인사이트 정리, 웹 대시보드 구현, A/B 테스트 설계

## Business Problem

ShopEasy는 2025년 7월부터 9월까지 전체 주문 수와 완료 주문 수가 함께 감소했습니다. 경영진 관점에서는 "주문이 줄었다"는 결과보다 다음 질문에 답하는 분석 구조가 필요했습니다.

| Question | Analysis Goal |
| --- | --- |
| 어떤 고객군에서 이탈 위험이 높은가? | 세그먼트별 이탈 위험 파악 |
| 어떤 카테고리에서 주문 완료율이 낮은가? | 전환 저하 카테고리 식별 |
| 세션 수 대비 구매 완료율이 낮은 흐름은 어디인가? | 진입, 탐색, 장바구니, 결제 병목 파악 |

## Dashboard Focus

- 월별 전체 주문 수와 완료 주문 수 변화
- 카테고리별 주문 완료율과 평균 객단가 비교
- 진입 페이지별 구매 전환율 비교
- 디바이스별 구매 전환 효율 비교
- 연령대별 이탈률과 고객 상태 분포
- 검색, 홈, 장바구니, 결제 단계의 이탈 신호
- 모바일 전자기기 구매 완료율 개선을 위한 A/B 테스트 제안

## Key Metrics

| Metric | Result | Interpretation |
| --- | ---: | --- |
| 전체 주문 | 1,000건 | 2025년 3분기 주문 분석 기준 |
| 완료 주문 | 688건 | 전체 완료율 68.8% |
| 완료 매출 | 89,439,000원 | 완료 주문 기준 3개월 누적 매출 |
| 전체 세션 | 2,000회 | 구매 완료 세션 174회, 세션 전환율 8.7% |
| 모바일 전환율 | 6.38% | 세션 규모는 가장 크지만 전환율은 가장 낮음 |
| 전자기기 완료율 | 52.34% | 평균 객단가는 가장 높지만 완료율은 가장 낮음 |

## Main Findings

1. 7월 대비 9월 전체 주문 수는 420건에서 240건으로 감소했고, 완료 주문 수는 305건에서 159건으로 감소했습니다.
2. 전자기기 카테고리는 주문 완료율이 52.34%로 가장 낮고 평균 객단가가 270,009원으로 가장 높아 우선 개선 대상입니다.
3. 모바일은 1,349회로 세션 수가 가장 많지만 구매 전환율은 6.38%로 가장 낮습니다.
4. 홈과 검색 진입 유저는 세션 수는 많지만 구매 전환율이 낮아 탐색에서 상품상세, 장바구니, 결제까지 이어지는 흐름이 약합니다.
5. 장바구니와 결제 페이지 이탈은 구매 의도가 높았던 사용자의 마찰 신호로 볼 수 있습니다.

## Recommendation

가장 우선순위가 높은 실험은 **모바일 전자기기 상품상세/장바구니 화면 개선 A/B 테스트**입니다.

| Area | Proposal | KPI |
| --- | --- | --- |
| 모바일 상품상세 | 혜택, 배송, 반품 정보를 더 명확히 노출 | 구매 완료율 |
| 장바구니 | 고가 상품의 추가 확인 요소를 짧게 정리 | 장바구니 이탈률 |
| 구매 CTA | 모바일에서 고정 구매 버튼과 핵심 혜택을 함께 노출 | 결제 시작률 |

## Data

분석 실습을 위해 생성한 더미 데이터를 사용했습니다. 단순 랜덤 데이터가 아니라 이커머스 지표 분석 흐름을 연습할 수 있도록 주문 감소, 카테고리별 완료율 차이, 디바이스별 전환율 차이, 고객 이탈 신호가 드러나도록 설계했습니다.

| File | Description |
| --- | --- |
| `dataset/shopeasy_orders.csv` | 주문, 카테고리, 금액, 주문 상태, 주문일 |
| `dataset/shopeasy_users.csv` | 사용자 연령대, 성별, 가입일, 최근 로그인, 구매 횟수 |
| `dataset/shopeasy_sessions.csv` | 진입 페이지, 이탈 페이지, 체류시간, 디바이스, 구매 완료 여부 |
| `dataset/monthly_orders_result.csv` | 월별 주문 수, 완료 주문 수, 완료율 |
| `dataset/category_completion_result.csv` | 카테고리별 주문 완료율 |
| `dataset/device_conversion_result_fixed.csv` | 디바이스별 구매 전환율 |
| `dataset/entry_page_conversion_result_fixed.csv` | 진입 페이지별 구매 전환율 |
| `dataset/exit_page_analysis_result_fixed.csv` | 이탈 페이지별 세션 수와 전환 신호 |

## Project Structure

```text
.
├── index.html
├── looker-dashboard/
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   └── assets/
├── dataset/
├── .github/workflows/deploy-pages.yml
└── README.md
```

## Tech Stack

- HTML
- CSS
- JavaScript
- Python/pandas 기반 지표 산출 결과 CSV
- GitHub Pages
- GitHub Actions

## Deployment

`main` 브랜치에 push하면 GitHub Actions가 `looker-dashboard` 산출물을 Pages artifact로 구성하고 GitHub Pages에 배포합니다.

## GitHub About

이 저장소의 GitHub About 영역은 아래 값으로 맞춥니다.

- Description: `2025년 3분기 이커머스 주문·전환·이탈 흐름을 분석한 ShopEasy 웹 대시보드.`
- Website: `https://dffxonnb-cyber.github.io/ShopEasy/`
- Topics: `ecommerce-analytics web-dashboard data-analysis javascript github-pages conversion-rate customer-segmentation ab-testing pandas business-intelligence`
