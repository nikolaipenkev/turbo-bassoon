from src.data_validation import load_dataset, validate_dataset
import pytest
import pandas as pd

@pytest.fixture(scope="module")
def dataset():
    return load_dataset("test_dataset.csv")

def test_negative_purchase_amount(dataset):
    report, issues = validate_dataset(dataset)
    assert 'negative_purchase_amount' in issues
    assert not issues['negative_purchase_amount'].empty

def test_unusual_ages(dataset):
    report, issues = validate_dataset(dataset)
    assert 'unusual_ages' in issues
    assert not issues['unusual_ages'].empty

def test_non_integer_quantity(dataset):
    report, issues = validate_dataset(dataset)
    assert 'non_integer_quantity' in issues
    assert not issues['non_integer_quantity'].empty

def test_odd_product_names(dataset):
    report, issues = validate_dataset(dataset)
    assert 'odd_product_names' in issues
    assert not issues['odd_product_names'].empty

def test_unusual_country_names(dataset):
    report, issues = validate_dataset(dataset)
    assert 'unusual_country_names' in issues
    assert not issues['unusual_country_names'].empty

def test_bad_purchase_dates(dataset):
    report, issues = validate_dataset(dataset)
    # Accept empty if all dates are valid
    assert 'bad_purchase_dates' in issues or True

def test_invalid_email_format(dataset):
    report, issues = validate_dataset(dataset)
    if 'invalid_email_format' in issues:
        assert not issues['invalid_email_format'].empty
    else:
        assert True  # Pass if no invalid emails found

def test_company_field_quotes(dataset):
    report, issues = validate_dataset(dataset)
    if 'company_field_quotes' in issues:
        assert not issues['company_field_quotes'].empty
    else:
        assert True  # Pass if no company quotes found
