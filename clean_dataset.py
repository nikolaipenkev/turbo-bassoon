
# clean_dataset.py
# Requirements: pandas must be installed, and test_dataset.csv must exist in the project root.
# This script loads the dataset, applies data corrections, and saves a cleaned CSV.

from src.data_validation import load_dataset
from src.data_correction import correct_dataset
from src.config import DATASET_PATH

if __name__ == "__main__":
    df = load_dataset(DATASET_PATH)
    df_clean = correct_dataset(df)
    df_clean.to_csv("test_dataset_clean.csv", index=False)
    print("Cleaned dataset saved as test_dataset_clean.csv")
