import pandas as pd
import chardet

with open("data/Superstore-dataset.csv", "rb") as f:
    result = chardet.detect(f.read())
    print(result)

# Load the dataset
df = pd.read_csv("data/Superstore-dataset.csv", encoding=result['encoding'])

# Preview first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset info
print("\nDataset info:")
print(df.info())

# Summary statistics for numeric columns
print("\nSummary statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())
