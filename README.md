# Betsson Data Quality Assessment Challenge

This repository contains a Python project for automated data quality assessment and correction, designed for QA Engineers in DATA at Betsson.

## Features
- **Data Quality Assessment**: Identifies common data issues in CSV datasets (e.g., negative amounts, unrealistic ages, invalid emails).
- **Automated Data Correction**: Cleans and corrects problematic data fields.
- **Test Suite**: Robust pytest-based tests for all validation rules.

## Project Structure
```
├── src/
│   ├── data_validation.py   # Data validation logic
│   └── data_correction.py   # Data correction logic
├── tests/
│   └── test_data_validation.py  # Pytest test suite
├── test_dataset.csv         # Original dataset
├── test_dataset_clean.csv   # Cleaned dataset (output)
├── validate_dataset.py      # CLI script for validation
├── clean_dataset.py         # CLI script for cleaning
├── requirements.txt         # Python dependencies
```

## Setup
1. **Install dependencies**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. **Run validation**
   ```powershell
   python validate_dataset.py
   ```
   - Outputs a data quality report to `data_quality_report.txt`.

3. **Run data cleaning**
   ```powershell
   python clean_dataset.py
   ```
   - Outputs a cleaned CSV as `test_dataset_clean.csv`.

4. **Run tests**
   ```powershell
   pytest tests
   ```

## How it works
- Validation logic is in `src/data_validation.py`.
- Correction logic is in `src/data_correction.py`.
- All rules and fixes are documented in code and tested in `tests/test_data_validation.py`.

## Customization
You can easily add new validation or correction rules by editing the respective modules in `src/` and adding tests in `tests/`.

## Author
Nikolai Penkev
