"""
Superstore Data Exploration Script
Author: Kristina Camacho
Purpose: Perform Exploratory Data Analysis (EDA) on the cleaned Superstore dataset
         and save key visualizations for business insights.
"""

# ===== 1. IMPORT LIBRARIES =====
import pandas as pd               # For data manipulation and analysis
import matplotlib.pyplot as plt   # For creating and customizing plots
import seaborn as sns             # For enhanced visualizations
import os                         # For file path handling and directory creation

# ===== 2. DEFINE FILE PATHS =====
DATA_PATH = os.path.join("data", "Superstore-dataset-clean.csv")  # Location of cleaned dataset
SCREENSHOT_DIR = "screenshots"  # Folder to store generated charts

# Create screenshots folder if it doesn't exist (avoids errors if it already exists)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# ===== 3. LOAD DATA =====
df = pd.read_csv(DATA_PATH)  # Load CSV file into a Pandas DataFrame

# ===== 4. BASIC OVERVIEW OF THE DATA =====
print("=== DATA OVERVIEW ===")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")  # Show dataset size

print("\nColumn Types:")
print(df.dtypes)  # Data types of each column

print("\nMissing Values:")
print(df.isnull().sum())  # Count missing values per column

print("\nSummary Statistics:")
print(df.describe())  # Show descriptive statistics for numeric columns

# ===== 5. KEY BUSINESS METRICS =====
total_sales = df['Sales'].sum()       # Total revenue
total_profit = df['Profit'].sum()     # Total profit
avg_order_value = df['Sales'].mean()  # Average revenue per order

print("\n=== KEY METRICS ===")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Order Value: ${avg_order_value:,.2f}")

# ===== 6. CATEGORY-LEVEL INSIGHTS =====
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

print("\n=== SALES BY CATEGORY ===")
print(category_sales)
print("\n=== PROFIT BY CATEGORY ===")
print(category_profit)

# --- Plot: Sales by Category ---
plt.figure(figsize=(8, 5))
sns.barplot(x=category_sales.values, y=category_sales.index, palette="viridis")
plt.title("Sales by Category")
plt.xlabel("Sales ($)")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(os.path.join(SCREENSHOT_DIR, "sales_by_category.png"))  # Save chart
plt.close()

# ===== 7. SALES TRENDS OVER TIME =====
df['Order Date'] = pd.to_datetime(df['Order Date'])  # Convert to date format
sales_over_time = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()

# --- Plot: Monthly Sales Over Time ---
plt.figure(figsize=(10, 5))
sales_over_time.plot()
plt.title("Monthly Sales Over Time")
plt.ylabel("Sales ($)")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig(os.path.join(SCREENSHOT_DIR, "monthly_sales.png"))
plt.close()

# ===== 8. REGIONAL ANALYSIS =====
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)

# --- Plot: Profit by Region ---
plt.figure(figsize=(8, 5))
sns.barplot(x=region_profit.values, y=region_profit.index, palette="coolwarm")
plt.title("Profit by Region")
plt.xlabel("Profit ($)")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig(os.path.join(SCREENSHOT_DIR, "profit_by_region.png"))
plt.close()

# ===== 9. COMPLETION MESSAGE =====
print("\nEDA Complete. Visuals saved in 'screenshots/' folder.")
