import pandas as pd
import re
from datetime import datetime

def load_dataset(path):
    return pd.read_csv(path)

def validate_dataset(df):
    report = []
    issues = {}
    suggestions = []

    # 1. Negative PurchaseAmount
    neg_amounts = df[df['PurchaseAmount'] < 0]
    if not neg_amounts.empty:
        report.append(f"Negative PurchaseAmount rows: {len(neg_amounts)}")
        issues['negative_purchase_amount'] = neg_amounts
        suggestions.append("Solution: Set negative PurchaseAmount to absolute value or flag for review.")

    # 2. Unusual Age values
    unusual_ages = df[(df['Age'] < 18) | (df['Age'] > 100)]
    if not unusual_ages.empty:
        report.append(f"Unusual Age values (<18 or >100): {len(unusual_ages)}")
        issues['unusual_ages'] = unusual_ages
        suggestions.append("Solution: Set unusual ages to None or flag for review.")

    # 3. PurchaseQuantity as float
    non_int_qty = df[df['PurchaseQuantity'] % 1 != 0]
    if not non_int_qty.empty:
        report.append(f"Non-integer PurchaseQuantity: {len(non_int_qty)}")
        issues['non_integer_quantity'] = non_int_qty
        suggestions.append("Solution: Round PurchaseQuantity to nearest integer.")

    # 4. Product field odd values (simple heuristic: not alphabetic or too short)
    odd_products = df[df['Product'].str.len() < 3]
    if not odd_products.empty:
        report.append(f"Odd Product names (len<3): {len(odd_products)}")
        issues['odd_product_names'] = odd_products
        suggestions.append("Solution: Replace odd Product names with 'Unknown'.")

    # 5. Country field unusual entries (length > 30)
    long_countries = df[df['Country'].str.len() > 30]
    if not long_countries.empty:
        report.append(f"Unusual Country names (len>30): {len(long_countries)}")
        issues['unusual_country_names'] = long_countries
        suggestions.append("Solution: Truncate Country names to 30 characters.")

    # 6. PurchaseDate format
    bad_dates = []
    for i, val in enumerate(df['PurchaseDate']):
        try:
            datetime.strptime(val, '%Y-%m-%d %H:%M:%S.%f')
        except Exception:
            bad_dates.append(i)
    if bad_dates:
        report.append(f"Bad PurchaseDate format rows: {len(bad_dates)}")
        issues['bad_purchase_dates'] = df.iloc[bad_dates]
        suggestions.append("Solution: Standardize PurchaseDate format to '%Y-%m-%d %H:%M:%S.%f'.")

    # 7. Email format
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    bad_emails = df[~df['Email'].str.match(email_regex)]
    if not bad_emails.empty:
        report.append(f"Invalid Email format: {len(bad_emails)}")
        issues['invalid_email_format'] = bad_emails
        suggestions.append("Solution: Lowercase and validate Email with regex.")

    # 8. Company field inconsistent quoting (contains quotes)
    quoted_companies = df[df['Company'].str.startswith('"') | df['Company'].str.endswith('"')]
    if not quoted_companies.empty:
        report.append(f"Company field with quotes: {len(quoted_companies)}")
        issues['company_field_quotes'] = quoted_companies
        suggestions.append("Solution: Remove leading/trailing quotes from Company field.")

    return report, issues, suggestions

if __name__ == "__main__":
    df = load_dataset("test_dataset.csv")
    report, issues, suggestions = validate_dataset(df)
    print("Data Validation Report:")
    for line in report:
        print(line)
    # Generate a unique report ID (timestamp)
    from datetime import datetime
    report_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Write text report with ID
    with open(f"data_quality_report_{report_id}.txt", "w") as f:
        f.write(f"Data Validation Report (ID: {report_id}):\n")
        for line in report:
            f.write(line + "\n")
    # Generate HTML report with ID in filename and header
    import reporting
    reporting.generate_html_report("test_dataset.csv", f"report_{report_id}.html")
    print("\nSuggested Solutions:")
    for s in suggestions:
        print(s)