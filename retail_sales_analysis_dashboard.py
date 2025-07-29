import pandas as pd

# Load the dataset
df = pd.read_csv("Superstore-dataset.csv", encoding="utf-8")

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
