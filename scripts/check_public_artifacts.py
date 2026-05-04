from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "index.html",
    ROOT / "404.html",
    ROOT / "looker-dashboard" / "index.html",
    ROOT / "looker-dashboard" / "styles.css",
    ROOT / "looker-dashboard" / "script.js",
    ROOT / "looker-dashboard" / "404.html",
    ROOT / "dataset" / "shopeasy_orders.csv",
    ROOT / "dataset" / "shopeasy_users.csv",
    ROOT / "dataset" / "shopeasy_sessions.csv",
    ROOT / "dataset" / "monthly_orders_result.csv",
    ROOT / "dataset" / "category_completion_result.csv",
    ROOT / "dataset" / "device_conversion_result_fixed.csv",
    ROOT / "dataset" / "entry_page_conversion_result_fixed.csv",
    ROOT / "dataset" / "exit_page_analysis_result_fixed.csv",
    ROOT / "dataset" / "age_group_churn_result.csv",
]

CSV_SCHEMAS = {
    "shopeasy_orders.csv": [
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
    ],
    "shopeasy_users.csv": [
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
    ],
    "shopeasy_sessions.csv": [
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
    ],
    "monthly_orders_result.csv": [
        "order_month",
        "total_orders",
        "completed_orders",
        "total_amount",
        "completion_rate",
        "completion_rate_pct",
    ],
    "category_completion_result.csv": [
        "category",
        "total_orders",
        "completed_orders",
        "avg_amount",
        "total_amount",
        "completion_rate",
        "completion_rate_pct",
    ],
    "device_conversion_result_fixed.csv": [
        "device",
        "total_sessions",
        "avg_session_duration",
        "completed_purchases",
        "conversion_rate",
        "conversion_rate_pct",
    ],
    "entry_page_conversion_result_fixed.csv": [
        "entry_page",
        "total_sessions",
        "avg_session_duration",
        "completed_purchases",
        "conversion_rate",
        "conversion_rate_pct",
    ],
    "exit_page_analysis_result_fixed.csv": [
        "exit_page",
        "total_sessions",
        "avg_session_duration",
        "completed_purchases",
        "conversion_rate",
        "conversion_rate_pct",
    ],
    "age_group_churn_result.csv": [
        "age_group",
        "total_users",
        "churned_users",
        "avg_purchase_count",
        "churn_rate",
        "churn_rate_pct",
    ],
}

EXPECTED_ROW_COUNTS = {
    "shopeasy_orders.csv": 1000,
    "shopeasy_users.csv": 500,
    "shopeasy_sessions.csv": 2000,
    "monthly_orders_result.csv": 3,
    "category_completion_result.csv": 5,
    "device_conversion_result_fixed.csv": 3,
    "entry_page_conversion_result_fixed.csv": 4,
    "exit_page_analysis_result_fixed.csv": 5,
    "age_group_churn_result.csv": 4,
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        return reader.fieldnames or [], list(reader)


def validate_csv(path: Path) -> list[str]:
    header, rows = read_csv(path)
    errors: list[str] = []
    expected_header = CSV_SCHEMAS.get(path.name)
    expected_count = EXPECTED_ROW_COUNTS.get(path.name)

    if expected_header and header != expected_header:
        errors.append(f"{path.relative_to(ROOT)} schema mismatch: {header}")
    if expected_count is not None and len(rows) != expected_count:
        errors.append(f"{path.relative_to(ROOT)} row count is {len(rows)}, expected {expected_count}")
    if not rows:
        errors.append(f"{path.relative_to(ROOT)} has no data rows")

    return errors


def validate_metric_consistency() -> list[str]:
    errors: list[str] = []
    monthly_header, monthly_rows = read_csv(ROOT / "dataset" / "monthly_orders_result.csv")
    device_header, device_rows = read_csv(ROOT / "dataset" / "device_conversion_result_fixed.csv")
    category_header, category_rows = read_csv(ROOT / "dataset" / "category_completion_result.csv")

    if not (monthly_header and device_header and category_header):
        return ["one or more metric CSV files are missing headers"]

    total_orders = sum(int(row["total_orders"]) for row in monthly_rows)
    completed_orders = sum(int(row["completed_orders"]) for row in monthly_rows)
    if total_orders != 1000 or completed_orders != 688:
        errors.append(f"monthly order totals are {total_orders}/{completed_orders}, expected 1000/688")

    mobile = next((row for row in device_rows if row["device"] == "mobile"), None)
    if not mobile or float(mobile["conversion_rate_pct"]) > 7:
        errors.append("mobile conversion should remain at or below 7%")

    electronics = next((row for row in category_rows if row["category"] == "전자기기"), None)
    if not electronics or float(electronics["completion_rate_pct"]) > 55:
        errors.append("electronics completion should remain at or below 55%")

    return errors


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not path.exists()]
    csv_errors = []
    for path in REQUIRED_FILES:
        if path.suffix == ".csv" and path.exists():
            csv_errors.extend(validate_csv(path))

    dashboard_html = (ROOT / "looker-dashboard" / "index.html").read_text(encoding="utf-8")
    missing_references = [
        reference for reference in ("styles.css", "script.js") if reference not in dashboard_html
    ]
    metric_errors = [] if missing else validate_metric_consistency()

    if missing or csv_errors or missing_references or metric_errors:
        if missing:
            print("Missing required public artifacts:")
            for path in missing:
                print(f"- {path.relative_to(ROOT)}")
        if csv_errors:
            print("CSV validation errors:")
            for error in csv_errors:
                print(f"- {error}")
        if missing_references:
            print("Dashboard HTML is missing required asset references:")
            for reference in missing_references:
                print(f"- {reference}")
        if metric_errors:
            print("Metric consistency errors:")
            for error in metric_errors:
                print(f"- {error}")
        return 1

    print("ShopEasy public artifacts verified:")
    for path in REQUIRED_FILES:
        print(f"- {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
