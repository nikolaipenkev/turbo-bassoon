from src.data_validation import load_dataset, validate_dataset
from src.data_correction import correct_dataset

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <title>Data Quality Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 2em; }}
        h1 {{ color: #2c3e50; }}
        ul {{ background: #f9f9f9; padding: 1em; border-radius: 8px; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 2em; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; }}
        th {{ background: #2c3e50; color: #fff; }}
        tr:nth-child(even) {{ background: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>Data Quality Report</h1>
    <h2>Summary</h2>
    <ul>
        {summary}
    </ul>
    <h2>Sample Issues</h2>
    {tables}
</body>
</html>
"""

def generate_html_report(dataset_path, output_path="report.html", sample_size=10):
    df = load_dataset(dataset_path)
    report, issues = validate_dataset(df)
    summary = "".join([f"<li>{item}</li>" for item in report])
    tables = ""
    for key, issue_df in issues.items():
        if not issue_df.empty:
            tables += f"<h3>{key.replace('_', ' ').title()}</h3>"
            tables += issue_df.head(sample_size).to_html(index=False)
    html = HTML_TEMPLATE.format(summary=summary, tables=tables)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML report generated: {output_path}")
