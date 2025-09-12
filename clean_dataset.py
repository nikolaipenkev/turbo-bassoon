from src.data_validation import load_dataset
from src.data_correction import correct_dataset

if __name__ == "__main__":
    DATASET_PATH = "test_dataset.csv"
    df = load_dataset(DATASET_PATH)
    df_clean = correct_dataset(df)
    df_clean.to_csv("test_dataset_clean.csv", index=False)
    print("Cleaned dataset saved as test_dataset_clean.csv")
