

# Betsson DATA QA Engineer Coding Challenge

## Overview

This is a code challenge for QA Engineer in DATA at Betsson.

**It is expected that all points are addressed.**

This challenge covers:
- Data Quality Assessment and Identification
- Data Validation and Error Handling

## Tasks

- **Identify and document the data quality issues present in the dataset, explaining the nature of each issue.**
- **Write a validation script for the dataset, suggest solutions to correct or handle the errors.**

---

## Project Structure

- `src/data_validation.py` — Main validation logic and entry point for validation/report generation.
- `src/reporting.py` — HTML report generator.
- `src/config.py` — Central config for dataset path.
- `test_dataset.csv` — Provided test dataset.
- `validate_dataset.py` — CLI script for validation and text report.
- `requirements.txt` — Python dependencies (`pandas`, `pytest`).
- `tests/test_data_validation.py` — Pytest-based unit tests for validation logic.

---

## Instructions

### 1. Setup Python Environment & Install Dependencies

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
```

### 2. Run Data Validation & Generate Reports

```bash
python src/data_validation.py
```
- Prints a summary to the console.
- Saves a text report (e.g. `data_quality_report.txt`).
- Generates an HTML report (e.g. `report.html`).

### 3. Run Automated Tests

```bash
pytest tests
```
- Runs all unit tests to verify the validation logic.

---

## Validation Criteria

The scripts check for:
- Negative purchase amounts
- Unrealistic age values
- Non-integer purchase quantities
- Odd product names
- Unusual country names
- Incorrect purchase date formats
- Invalid email formats
- Company field quotes

Each issue is documented and a suggested solution is provided in the code and reports.

---
**Author:** nikolaipenkev
