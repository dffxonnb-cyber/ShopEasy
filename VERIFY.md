# Verification Guide

ShopEasy is a static dashboard project. Its reproducibility target is whether the published HTML/CSS/JavaScript and CSV review artifacts are present, internally linked, and deployable through GitHub Pages.

## Verification Scope

| Area | Publicly Verifiable | Notes |
| --- | --- | --- |
| Static dashboard files | Yes | `looker-dashboard/index.html`, CSS, JavaScript, and 404 page are tracked. |
| CSV review artifacts | Yes | Synthetic order, user, session, and metric CSVs are tracked under `dataset/`. |
| Dataset generation | Yes | `scripts/generate_dataset.py` rebuilds the synthetic dataset with seed `20250930`. |
| Asset references | Yes | The checker confirms the dashboard HTML references CSS and JavaScript. |
| GitHub Pages package | Yes | CI verifies artifacts before packaging `looker-dashboard` as the Pages site. |

## Local Verification

```bash
python scripts/generate_dataset.py --output-dir dataset
python scripts/check_public_artifacts.py
```

The script checks:

- required HTML/CSS/JavaScript files
- required CSV files
- CSV schema and row counts
- monthly order totals and key friction signals
- dashboard references to `styles.css` and `script.js`

## CI Verification

GitHub Actions runs the same check before configuring and uploading the Pages artifact:

```bash
python scripts/check_public_artifacts.py
```

## Data Boundary

- The tracked dataset is synthetic educational sample data.
- Public verification checks completeness, deployability, schema, and key metric consistency.
- No external data source is required to review the dashboard.

## Known Limits

- CI does not run browser-based visual regression tests.
- The generator intentionally optimizes for realistic dashboard signals, not production-grade behavioral simulation.
