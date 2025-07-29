# superstore_data_exploration.py
# Step 2: Exploratory Data Analysis (EDA) for Superstore Dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# File paths
DATA_PATH = os.path.join("data", "Superstore-dataset-clean.csv")
SCREENSHOT_DIR = "screenshots"

# Create screenshots folder if it doesn't exist
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA_PATH)

# ===== 1. BASIC OVERVIEW =====
print("=== DATA OVERVIEW ===")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("\nColumn Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nSummary Statistics:")
print(df.describe())

# ===== 2. KEY BUSINESS METRICS =====
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
avg_order_value = df['Sales'].mean()

print("\n=== KEY METRICS ===")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Order Value: ${avg_order_value:,.2f}")

# ===== 3. TOP CATEGORIES =====
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
category_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)

print("\n=== SALES BY CATEGORY ===")
print(category_sales)
print("\n=== PROFIT BY CATEGORY ===")
print(category_profit)

# Plot category sales
plt.figure(figsize=(8, 5))
sns.barplot(x=category_sales.values, y=category_sales.index, palette="viridis")
plt.title("Sales by Category")
plt.xlabel("Sales ($)")
plt.ylabel("Category")
plt.tight_layout()
plt.savefig(os.path.join(SCREENSHOT_DIR, "sales_by_category.png"))
plt.close()

# ===== 4. TRENDS OVER TIME =====
df['Order Date'] = pd.to_datetime(df['Order Date'])
sales_over_time = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()

plt.figure(figsize=(10, 5))
sales_over_time.plot()
plt.title("Monthly Sales Over Time")
plt.ylabel("Sales ($)")
plt.xlabel("Month")
plt.tight_layout()
plt.savefig(os.path.join(SCREENSHOT_DIR, "monthly_sales.png"))
plt.close()

# ===== 5. REGIONAL ANALYSIS =====
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)

# Plot region profit
plt.figure(figsize=(8, 5))
sns.barplot(x=region_profit.values, y=region_profit.index, palette="coolwarm")
plt.title("Profit by Region")
plt.xlabel("Profit ($)")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig(os.path.join(SCREENSHOT_DIR, "profit_by_region.png"))
plt.close()

print("\nEDA Complete. Visuals saved in 'screenshots/' folder.")
