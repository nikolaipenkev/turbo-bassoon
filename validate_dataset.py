from src.data_validation import load_dataset, validate_dataset

def main():
    DATASET_PATH = 'test_dataset.csv'
    df = load_dataset(DATASET_PATH)
    report, issues = validate_dataset(df)

    print("DATA QUALITY REPORT:")
    for item in report:
        print("-", item)

    with open('data_quality_report.txt', 'w') as f:
        f.write("DATA QUALITY REPORT:\n")
        for item in report:
            f.write(f"- {item}\n")

if __name__ == "__main__":
    main()
