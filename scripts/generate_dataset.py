from __future__ import annotations

import argparse
import csv
import random
from collections import Counter, defaultdict
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT_DIR = ROOT / "dataset"
DEFAULT_SEED = 20250930

USER_FIELDS = [
    "user_id",
    "age_group",
    "gender",
    "join_date",
    "last_login",
    "purchase_count",
    "region",
    "acquisition_channel",
    "membership_tier",
    "marketing_opt_in",
    "preferred_device",
    "lifecycle_segment",
]
ORDER_FIELDS = [
    "order_id",
    "user_id",
    "category",
    "amount",
    "order_status",
    "order_date",
    "device",
    "payment_method",
    "coupon_used",
    "discount_rate",
    "shipping_fee",
    "delivery_days",
    "is_first_order",
]
SESSION_FIELDS = [
    "session_id",
    "user_id",
    "entry_page",
    "exit_page",
    "session_duration",
    "device",
    "session_date",
    "traffic_source",
    "category_viewed",
    "is_logged_in",
    "add_to_cart",
    "checkout_start",
    "purchase_completed",
    "linked_order_id",
    "bounce_flag",
]

MONTHLY_ORDER_TARGETS = {
    "2025-07": (420, 305),
    "2025-08": (340, 224),
    "2025-09": (240, 159),
}
CATEGORIES = {
    "전자기기": {"weight": 0.22, "base_amount": 270000, "completion_bias": -0.22},
    "패션": {"weight": 0.25, "base_amount": 115000, "completion_bias": -0.05},
    "홈리빙": {"weight": 0.18, "base_amount": 156000, "completion_bias": 0.02},
    "뷰티": {"weight": 0.18, "base_amount": 72000, "completion_bias": 0.08},
    "식품": {"weight": 0.17, "base_amount": 49000, "completion_bias": 0.12},
}
DEVICE_WEIGHTS = {"mobile": 0.68, "desktop": 0.25, "tablet": 0.07}


def weighted_choice(rng: random.Random, weights: dict[str, float]) -> str:
    return rng.choices(list(weights), weights=list(weights.values()), k=1)[0]


def random_date(rng: random.Random, start: date, end: date) -> date:
    return start + timedelta(days=rng.randint(0, (end - start).days))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def pct(value: float) -> str:
    return str(round(value * 100, 2))


def build_users(rng: random.Random) -> list[dict[str, object]]:
    age_weights = {"20대": 0.31, "30대": 0.33, "40대": 0.19, "50대 이상": 0.17}
    acquisition = {"paid_search": 0.31, "organic": 0.24, "social": 0.23, "referral": 0.12, "display": 0.10}
    tiers = {"BRONZE": 0.48, "SILVER": 0.28, "GOLD": 0.18, "VIP": 0.06}
    users = []

    for idx in range(1, 501):
        join_day = random_date(rng, date(2024, 7, 1), date(2025, 9, 30))
        last_login = random_date(rng, date(2025, 6, 1), date(2025, 9, 30))
        users.append(
            {
                "user_id": f"U{idx:04d}",
                "age_group": weighted_choice(rng, age_weights),
                "gender": weighted_choice(rng, {"F": 0.54, "M": 0.46}),
                "join_date": join_day.isoformat(),
                "last_login": last_login.isoformat(),
                "purchase_count": 0,
                "region": rng.choice(["서울", "경기", "인천", "부산", "대전"]),
                "acquisition_channel": weighted_choice(rng, acquisition),
                "membership_tier": weighted_choice(rng, tiers),
                "marketing_opt_in": weighted_choice(rng, {"Y": 0.62, "N": 0.38}),
                "preferred_device": weighted_choice(rng, DEVICE_WEIGHTS),
                "lifecycle_segment": "신규",
            }
        )
    return users


def build_orders(rng: random.Random, users: list[dict[str, object]]) -> list[dict[str, object]]:
    user_ids = [str(user["user_id"]) for user in users]
    category_weights = {name: data["weight"] for name, data in CATEGORIES.items()}
    orders: list[dict[str, object]] = []

    for month, (total_orders, completed_orders) in MONTHLY_ORDER_TARGETS.items():
        year, month_num = [int(part) for part in month.split("-")]
        month_start = date(year, month_num, 1)
        month_end = date(year, month_num, 30 if month_num == 9 else 31)
        month_rows: list[dict[str, object]] = []

        for _ in range(total_orders):
            category = weighted_choice(rng, category_weights)
            device = weighted_choice(rng, DEVICE_WEIGHTS)
            base_amount = int(CATEGORIES[category]["base_amount"])
            amount = max(9000, int(rng.normalvariate(base_amount, base_amount * 0.22) // 1000 * 1000))
            coupon_used = weighted_choice(rng, {"Y": 0.37, "N": 0.63})
            completion_score = (
                0.68
                + float(CATEGORIES[category]["completion_bias"])
                + (0.06 if device == "desktop" else -0.08 if device == "mobile" else 0.01)
                + (0.04 if coupon_used == "Y" else 0.0)
                + rng.uniform(-0.12, 0.12)
            )
            month_rows.append(
                {
                    "order_id": f"O{len(orders) + len(month_rows) + 1:05d}",
                    "user_id": rng.choice(user_ids),
                    "category": category,
                    "amount": amount,
                    "order_status": "미정",
                    "order_date": random_date(rng, month_start, month_end).isoformat(),
                    "device": device,
                    "payment_method": weighted_choice(rng, {"card": 0.64, "kakao_pay": 0.18, "naver_pay": 0.12, "bank": 0.06}),
                    "coupon_used": coupon_used,
                    "discount_rate": rng.choice([0, 5, 10, 15]) if coupon_used == "Y" else 0,
                    "shipping_fee": 0 if amount >= 50000 else 3000,
                    "delivery_days": rng.randint(1, 5),
                    "is_first_order": "N",
                    "_completion_score": completion_score,
                }
            )

        ranked = sorted(month_rows, key=lambda row: float(row["_completion_score"]), reverse=True)
        completed_ids = {row["order_id"] for row in ranked[:completed_orders]}
        for row in month_rows:
            row["order_status"] = "완료" if row["order_id"] in completed_ids else weighted_choice(rng, {"취소": 0.58, "반품": 0.42})
            row.pop("_completion_score")
        orders.extend(month_rows)

    first_order_seen: set[str] = set()
    for row in sorted(orders, key=lambda item: str(item["order_date"])):
        user_id = str(row["user_id"])
        if user_id not in first_order_seen:
            row["is_first_order"] = "Y"
            first_order_seen.add(user_id)
    return orders


def update_users_from_orders(users: list[dict[str, object]], orders: list[dict[str, object]]) -> None:
    completed_by_user = Counter(str(row["user_id"]) for row in orders if row["order_status"] == "완료")
    for user in users:
        count = completed_by_user[str(user["user_id"])]
        user["purchase_count"] = count
        if count >= 4:
            user["lifecycle_segment"] = "충성"
        elif count >= 2:
            user["lifecycle_segment"] = "활성"
        elif count == 1:
            user["lifecycle_segment"] = "이탈위험"
        else:
            user["lifecycle_segment"] = "휴면징후"


def build_sessions(rng: random.Random, users: list[dict[str, object]], orders: list[dict[str, object]]) -> list[dict[str, object]]:
    user_ids = [str(user["user_id"]) for user in users]
    completed_orders = [row["order_id"] for row in orders if row["order_status"] == "완료"]
    category_weights = {name: data["weight"] for name, data in CATEGORIES.items()}
    sessions: list[dict[str, object]] = []

    for idx in range(1, 2001):
        entry_page = weighted_choice(rng, {"홈": 0.36, "검색": 0.26, "카테고리": 0.22, "상품상세": 0.16})
        device = weighted_choice(rng, DEVICE_WEIGHTS)
        category = weighted_choice(rng, category_weights)
        base_duration = {"홈": 110, "검색": 145, "카테고리": 165, "상품상세": 215}[entry_page]
        session_duration = max(12, int(rng.normalvariate(base_duration, 58)))
        score = (
            0.05
            + (0.10 if entry_page == "상품상세" else 0.04 if entry_page == "카테고리" else -0.03)
            + (0.08 if device == "desktop" else -0.04 if device == "mobile" else 0.02)
            + (0.04 if category != "전자기기" else -0.06)
            + (0.04 if session_duration > 180 else 0.0)
            + rng.uniform(-0.05, 0.05)
        )
        sessions.append(
            {
                "session_id": f"S{idx:05d}",
                "user_id": rng.choice(user_ids),
                "entry_page": entry_page,
                "exit_page": "미정",
                "session_duration": session_duration,
                "device": device,
                "session_date": random_date(rng, date(2025, 7, 1), date(2025, 9, 30)).isoformat(),
                "traffic_source": weighted_choice(rng, {"organic": 0.28, "paid_search": 0.26, "direct": 0.22, "social": 0.17, "email": 0.07}),
                "category_viewed": category,
                "is_logged_in": weighted_choice(rng, {"Y": 0.72, "N": 0.28}),
                "add_to_cart": "N",
                "checkout_start": "N",
                "purchase_completed": "N",
                "linked_order_id": "",
                "bounce_flag": "N",
                "_purchase_score": score,
            }
        )

    ranked = sorted(sessions, key=lambda row: float(row["_purchase_score"]), reverse=True)
    purchase_sessions = {row["session_id"] for row in ranked[:174]}
    order_iter = iter(completed_orders)
    for row in sessions:
        purchased = row["session_id"] in purchase_sessions
        row["purchase_completed"] = "Y" if purchased else "N"
        row["add_to_cart"] = "Y" if purchased or rng.random() < 0.24 else "N"
        row["checkout_start"] = "Y" if purchased or (row["add_to_cart"] == "Y" and rng.random() < 0.45) else "N"
        if purchased:
            row["exit_page"] = "결제완료"
            row["linked_order_id"] = next(order_iter, "")
        elif row["checkout_start"] == "Y":
            row["exit_page"] = "결제"
        elif row["add_to_cart"] == "Y":
            row["exit_page"] = "장바구니"
        else:
            row["exit_page"] = weighted_choice(rng, {"홈": 0.35, "검색": 0.28, "카테고리": 0.22, "상품상세": 0.15})
        row["bounce_flag"] = "Y" if row["session_duration"] < 45 and row["purchase_completed"] == "N" else "N"
        row.pop("_purchase_score")
    return sessions


def aggregate_orders(orders: list[dict[str, object]]) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    monthly: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_category: dict[str, list[dict[str, object]]] = defaultdict(list)
    for order in orders:
        monthly[str(order["order_date"])[:7]].append(order)
        by_category[str(order["category"])].append(order)

    monthly_rows = []
    for month in sorted(monthly):
        rows = monthly[month]
        completed = [row for row in rows if row["order_status"] == "완료"]
        rate = len(completed) / len(rows)
        monthly_rows.append(
            {
                "order_month": month,
                "total_orders": len(rows),
                "completed_orders": len(completed),
                "total_amount": sum(int(row["amount"]) for row in completed),
                "completion_rate": rate,
                "completion_rate_pct": pct(rate),
            }
        )

    category_rows = []
    for category in sorted(by_category):
        rows = by_category[category]
        completed = [row for row in rows if row["order_status"] == "완료"]
        rate = len(completed) / len(rows)
        category_rows.append(
            {
                "category": category,
                "total_orders": len(rows),
                "completed_orders": len(completed),
                "avg_amount": round(sum(int(row["amount"]) for row in rows) / len(rows)),
                "total_amount": sum(int(row["amount"]) for row in rows),
                "completion_rate": rate,
                "completion_rate_pct": pct(rate),
            }
        )
    return monthly_rows, category_rows


def aggregate_sessions(sessions: list[dict[str, object]], key: str) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for session in sessions:
        groups[str(session[key])].append(session)

    rows = []
    for value in sorted(groups):
        sessions_for_value = groups[value]
        completed = [row for row in sessions_for_value if row["purchase_completed"] == "Y"]
        rate = len(completed) / len(sessions_for_value)
        rows.append(
            {
                key: value,
                "total_sessions": len(sessions_for_value),
                "avg_session_duration": round(
                    sum(int(row["session_duration"]) for row in sessions_for_value) / len(sessions_for_value), 2
                ),
                "completed_purchases": len(completed),
                "conversion_rate": rate,
                "conversion_rate_pct": pct(rate),
            }
        )
    return rows


def aggregate_user_churn(users: list[dict[str, object]]) -> list[dict[str, object]]:
    groups: dict[str, list[dict[str, object]]] = defaultdict(list)
    for user in users:
        groups[str(user["age_group"])].append(user)

    rows = []
    for age_group in sorted(groups):
        users_for_group = groups[age_group]
        churned = [user for user in users_for_group if str(user["lifecycle_segment"]) in {"이탈위험", "휴면징후"}]
        rate = len(churned) / len(users_for_group)
        rows.append(
            {
                "age_group": age_group,
                "total_users": len(users_for_group),
                "churned_users": len(churned),
                "avg_purchase_count": round(
                    sum(int(user["purchase_count"]) for user in users_for_group) / len(users_for_group), 2
                ),
                "churn_rate": rate,
                "churn_rate_pct": pct(rate),
            }
        )
    return rows


def generate_dataset(output_dir: Path, seed: int) -> None:
    rng = random.Random(seed)
    users = build_users(rng)
    orders = build_orders(rng, users)
    update_users_from_orders(users, orders)
    sessions = build_sessions(rng, users, orders)
    monthly_rows, category_rows = aggregate_orders(orders)

    write_csv(output_dir / "shopeasy_users.csv", USER_FIELDS, users)
    write_csv(output_dir / "shopeasy_orders.csv", ORDER_FIELDS, orders)
    write_csv(output_dir / "shopeasy_sessions.csv", SESSION_FIELDS, sessions)
    write_csv(
        output_dir / "monthly_orders_result.csv",
        ["order_month", "total_orders", "completed_orders", "total_amount", "completion_rate", "completion_rate_pct"],
        monthly_rows,
    )
    write_csv(
        output_dir / "category_completion_result.csv",
        ["category", "total_orders", "completed_orders", "avg_amount", "total_amount", "completion_rate", "completion_rate_pct"],
        category_rows,
    )
    write_csv(
        output_dir / "device_conversion_result_fixed.csv",
        ["device", "total_sessions", "avg_session_duration", "completed_purchases", "conversion_rate", "conversion_rate_pct"],
        aggregate_sessions(sessions, "device"),
    )
    write_csv(
        output_dir / "entry_page_conversion_result_fixed.csv",
        ["entry_page", "total_sessions", "avg_session_duration", "completed_purchases", "conversion_rate", "conversion_rate_pct"],
        aggregate_sessions(sessions, "entry_page"),
    )
    write_csv(
        output_dir / "exit_page_analysis_result_fixed.csv",
        ["exit_page", "total_sessions", "avg_session_duration", "completed_purchases", "conversion_rate", "conversion_rate_pct"],
        aggregate_sessions(sessions, "exit_page"),
    )
    write_csv(
        output_dir / "age_group_churn_result.csv",
        ["age_group", "total_users", "churned_users", "avg_purchase_count", "churn_rate", "churn_rate_pct"],
        aggregate_user_churn(users),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate deterministic synthetic ShopEasy Q3 dashboard data.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR, help="Directory to write CSV files.")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED, help="Random seed for repeatable data generation.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    generate_dataset(output_dir=args.output_dir, seed=args.seed)
    print(f"Generated ShopEasy synthetic dataset in {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
