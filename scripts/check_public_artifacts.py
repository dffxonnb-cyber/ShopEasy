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
]


def csv_has_header_and_rows(path: Path) -> bool:
    with path.open(newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        header = next(reader, [])
        first_row = next(reader, [])
    return bool(header) and bool(first_row)


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not path.exists()]
    empty_csvs = [
        path for path in REQUIRED_FILES if path.suffix == ".csv" and path.exists() and not csv_has_header_and_rows(path)
    ]

    dashboard_html = (ROOT / "looker-dashboard" / "index.html").read_text(encoding="utf-8")
    missing_references = [
        reference for reference in ("styles.css", "script.js") if reference not in dashboard_html
    ]

    if missing or empty_csvs or missing_references:
        if missing:
            print("Missing required public artifacts:")
            for path in missing:
                print(f"- {path.relative_to(ROOT)}")
        if empty_csvs:
            print("CSV files without both header and data rows:")
            for path in empty_csvs:
                print(f"- {path.relative_to(ROOT)}")
        if missing_references:
            print("Dashboard HTML is missing required asset references:")
            for reference in missing_references:
                print(f"- {reference}")
        return 1

    print("ShopEasy public artifacts verified:")
    for path in REQUIRED_FILES:
        print(f"- {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
