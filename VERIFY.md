# Verification Guide

ShopEasy is a static dashboard project. Its reproducibility target is whether the published HTML/CSS/JavaScript and CSV review artifacts are present, internally linked, and deployable through GitHub Pages.

## Verification Scope

| Area | Publicly Verifiable | Notes |
| --- | --- | --- |
| Static dashboard files | Yes | `looker-dashboard/index.html`, CSS, JavaScript, and 404 page are tracked. |
| CSV review artifacts | Yes | Synthetic order, user, session, and metric CSVs are tracked under `dataset/`. |
| Asset references | Yes | The checker confirms the dashboard HTML references CSS and JavaScript. |
| GitHub Pages package | Yes | CI verifies artifacts before packaging `looker-dashboard` as the Pages site. |
| Dataset generation | No | The repo verifies the published synthetic dataset, not its generator. |

## Local Verification

```bash
python scripts/check_public_artifacts.py
```

The script checks:

- required HTML/CSS/JavaScript files
- required CSV files
- CSV header and data row presence
- dashboard references to `styles.css` and `script.js`

## CI Verification

GitHub Actions runs the same check before configuring and uploading the Pages artifact:

```bash
python scripts/check_public_artifacts.py
```

## Data Boundary

- The tracked dataset is synthetic educational sample data.
- Public verification checks completeness and deployability of the current artifact set.
- No external data source is required to review the dashboard.

## Known Limits

- The current repo does not include a separate data-generation script.
- CI does not run browser-based visual regression tests.
- Future improvement: add a deterministic synthetic data generator and compare regenerated CSV outputs.
