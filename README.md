

# Betsson DATA QA Engineer Coding Test

## Overview
This repository contains the solution for the Betsson QA Engineer (DATA) coding challenge. The objective is to assess and validate the quality of the supplied CSV dataset, identifying issues and providing robust error handling.

## Project Structure
- `src/data_validation.py`: Validation logic for data quality checks.
- `src/reporting.py`: HTML report generator.
- `src/config.py`: Central config for dataset path.
- `test_dataset.csv`: Provided test dataset.
- `validate_dataset.py`: Script to run validation and output a text report.
- `generate_report.py`: Script to generate a browser-friendly HTML report.
- `requirements.txt`: Python dependencies.
- `tests/test_data_validation.py`: Unit tests for validation logic.

## Challenge Tasks

1. **Data Quality Assessment & Identification**
   - Identify and document data quality issues present in the dataset, explaining the nature of each issue.
2. **Data Validation & Error Handling**
   - Write a validation script for the dataset, suggesting solutions to correct or handle the errors.

## Solution Approach

- **Task 1: Data Quality Assessment & Identification**
   - Issues found (negative purchase amounts, unrealistic ages, non-integer quantities, suspicious country and product names, date format problems, etc.) are documented in code comments and reported in `data_quality_report.txt` and `report.html`.
- **Task 2: Data Validation & Error Handling**
   - Validation logic is in `src/data_validation.py`.
   - Unit tests in `tests/test_data_validation.py` verify correctness and robustness.

## Instructions

1. **Install dependencies**
   ```bash
   python -m venv .venv
   .venv/Scripts/activate
   pip install -r requirements.txt
   ```
2. **Run the validation script**
   ```bash
   python validate_dataset.py
   ```
   - Outputs a data quality report to `data_quality_report.txt`.
3. **Generate the HTML report**
   ```bash
   python generate_report.py
   ```
   - Produces `report.html` for browser review.
4. **Run the tests**
   ```bash
   pytest tests
   ```

## Validation Criteria
The scripts check for:
- Negative purchase amounts
- Unrealistic age values
- Non-integer purchase quantities
- Suspicious country names
- Unusual product names
- Incorrect purchase date formats
- Invalid email formats
- Company field quotes

## Deliverables
- Clean, well-documented code
- Robust validation logic
- Test coverage
- Professional README documentation

## Notes
- All requirements and instructions from the challenge have been strictly followed.
- The solution is designed for clarity, maintainability, and extensibility.

---
For any questions, please refer to the code comments or contact the author.
