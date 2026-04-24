# ShopEasy 통합 웹 대시보드

> 2025년 3분기 이커머스 주문 감소 원인을 분석하고, 모바일·전자기기 구매 완료율 개선을 위한 A/B 테스트를 제안한 웹 기반 데이터 분석 프로젝트입니다.

- **Web Dashboard**: [https://dffxonnb-cyber.github.io/ShopEasy/](https://dffxonnb-cyber.github.io/ShopEasy/)
- **GitHub Repository**: [https://github.com/dffxonnb-cyber/ShopEasy](https://github.com/dffxonnb-cyber/ShopEasy)
- **Project Type**: 이커머스 주문 감소 원인 분석 / 전환율 분석 / 웹 대시보드
- **Data Type**: 주문 데이터, 사용자 데이터, 세션 데이터
- **Role**: 데이터 설계, 분석, 인사이트 도출, 웹 대시보드 구현, A/B 테스트 설계

---

## 1. Executive Summary

ShopEasy는 2025년 3분기 동안 전체 주문 수와 완료 주문 수가 함께 감소하는 흐름을 보였습니다.

본 프로젝트는 주문 감소의 원인을 단순 유입 감소로 보지 않고, **고객 세그먼트, 상품 카테고리, 진입 페이지, 디바이스, 이탈 페이지** 관점으로 나누어 분석했습니다.

분석 결과, 주문 감소는 다음 요인과 관련이 있는 것으로 나타났습니다.

- 홈·검색 진입 이후 구매로 이어지는 흐름 약화
- 모바일 환경의 낮은 구매 전환율
- 전자기기 카테고리의 낮은 주문 완료율
- 장바구니·결제 단계에서 발생하는 고의도 사용자 이탈

이를 바탕으로 **모바일 환경에서 전자기기 상품의 혜택·배송·반품 정보와 구매 버튼 노출을 개선하는 A/B 테스트**를 제안했습니다.

---

## 2. Project Output

| 구분 | 내용 |
| --- | --- |
| 프로젝트명 | ShopEasy 통합 웹 대시보드 |
| 분석 주제 | 2025년 3분기 주문 감소 원인 분석 |
| 분석 대상 | 주문 데이터, 사용자 데이터, 세션 데이터 |
| 최종 결과물 | 웹 기반 통합 대시보드, 인사이트 리포트, A/B 테스트 설계안 |
| 분석 방식 | Python/pandas 기반 지표 산출 후 HTML/CSS/JavaScript 대시보드 구현 |
| 배포 방식 | GitHub Pages |

---

## 3. Business Problem

ShopEasy는 최근 3개월간 주문 수가 꾸준히 감소하고 있는 상황입니다.

경영진은 단순히 “주문이 줄었다”는 결과가 아니라, 다음 질문에 답할 수 있는 분석 결과를 필요로 했습니다.

| 핵심 질문 | 분석 목적 |
| --- | --- |
| 어떤 유저 세그먼트에서 이탈이 가장 많이 발생했는가? | 고객 이탈 위험군 파악 |
| 어떤 상품 카테고리에서 주문 완료율이 낮은가? | 전환 저하 카테고리 식별 |
| 세션 수 대비 구매 완료율이 낮은 원인은 무엇인가? | 유입·탐색·구매 흐름의 병목 파악 |

---

## 4. Data Overview

본 프로젝트에서는 분석 실습을 위해 생성한 더미 데이터를 사용했습니다.

단순 랜덤 데이터가 아니라 실제 이커머스 지표 분석 흐름을 연습할 수 있도록 **주문 감소, 카테고리별 완료율 차이, 디바이스별 전환율 차이, 고객 이탈 신호**가 드러나도록 설계했습니다.

### 4-1. Raw Data

| 데이터 | 건수 | 주요 컬럼 | 활용 목적 |
| --- | ---: | --- | --- |
| `orders` | 1,000건 | order_id, user_id, category, amount, order_status, order_date | 월별 주문 추이, 주문 완료율, 카테고리별 성과 분석 |
| `users` | 500건 | user_id, age_group, gender, join_date, last_login, purchase_count | 연령대별 이탈률, 고객 상태 분류 |
| `sessions` | 2,000건 | session_id, user_id, entry_page, exit_page, session_duration, device, purchase_completed | 진입 페이지, 이탈 페이지, 디바이스별 전환 분석 |

### 4-2. Analysis Output

Python 분석 후 대시보드 제작에 활용하기 위해 아래 결과 테이블을 생성했습니다.

| 분석 결과 파일 | 설명 |
| --- | --- |
| `monthly_orders_result.csv` | 월별 전체 주문 수, 완료 주문 수, 완료율 |
| `category_completion_result.csv` | 카테고리별 주문 완료율 |
| `age_group_churn_result.csv` | 연령대별 이탈률 |
| `entry_page_conversion_result_fixed.csv` | 진입 페이지별 구매 전환율 |
| `device_conversion_result_fixed.csv` | 디바이스별 구매 전환율 |
| `exit_page_analysis_result_fixed.csv` | 이탈 페이지별 세션 수 및 전환 신호 |

---

## 5. Analysis Framework

주문 감소 원인을 하나의 숫자로만 판단하지 않고, 다음과 같이 분석 관점을 분리했습니다.

| 분석 관점 | 핵심 지표 | 판단 기준 |
| --- | --- | --- |
| 월별 성과 | 전체 주문 수, 완료 주문 수, 완료율 | 7월~9월 주문 흐름 변화 |
| 고객 세그먼트 | 연령대별 이탈률 | `purchase_count = 0`인 유저 비율 |
| 상품 카테고리 | 카테고리별 주문 완료율 | 전체 주문 중 `order_status = 완료` 비율 |
| 진입 페이지 | 진입 페이지별 구매 전환율 | 세션 중 `purchase_completed = Y` 비율 |
| 디바이스 | 디바이스별 구매 전환율 | mobile / desktop / tablet 전환율 비교 |
| 이탈 페이지 | 이탈 페이지별 세션 수 | 검색, 홈, 장바구니, 결제, 완료 페이지별 이탈 신호 |

분석 흐름은 아래와 같이 구성했습니다.

```text
주문 감소 확인
→ 카테고리별 완료율 비교
→ 진입 페이지별 전환율 확인
→ 디바이스별 전환 차이 확인
→ 고객 이탈 세그먼트 확인
→ 이탈 페이지 분석
→ A/B 테스트 제안
