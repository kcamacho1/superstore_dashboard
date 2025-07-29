import streamlit as st
import pandas as pd
import plotly.express as px
import os

# =========================
# LOAD DATA
# =========================
DATA_PATH = os.path.join("data", "Superstore-dataset-clean.csv")

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    return df

df = load_data()

# =========================
# SIDEBAR FILTERS
# =========================
st.sidebar.header("Filter Data")

# Date filter
min_date = df['Order Date'].min()
max_date = df['Order Date'].max()
date_range = st.sidebar.date_input("Order Date Range", [min_date, max_date])

# Category filter
categories = st.sidebar.multiselect("Category", options=df['Category'].unique(), default=df['Category'].unique())

# Region filter
regions = st.sidebar.multiselect("Region", options=df['Region'].unique(), default=df['Region'].unique())

# Apply filters
filtered_df = df[
    (df['Order Date'] >= pd.to_datetime(date_range[0])) &
    (df['Order Date'] <= pd.to_datetime(date_range[1])) &
    (df['Category'].isin(categories)) &
    (df['Region'].isin(regions))
]

# =========================
# KPI METRICS
# =========================
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
avg_order_value = filtered_df['Sales'].mean()

st.title("📊 Superstore Analytics Dashboard")
st.markdown("Interactive dashboard to analyze sales and profit trends.")

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Avg Order Value", f"${avg_order_value:,.2f}")

# =========================
# CHARTS
# =========================
# Sales by Category
category_sales = filtered_df.groupby('Category')['Sales'].sum().reset_index()
fig_cat = px.bar(category_sales, x='Sales', y='Category', orientation='h', title="Sales by Category", color='Category')
st.plotly_chart(fig_cat, use_container_width=True)

# Monthly Sales Trend
monthly_sales = filtered_df.groupby(pd.Grouper(key='Order Date', freq='M'))['Sales'].sum().reset_index()
fig_month = px.line(monthly_sales, x='Order Date', y='Sales', title="Monthly Sales Over Time")
st.plotly_chart(fig_month, use_container_width=True)

# Profit by Region
region_profit = filtered_df.groupby('Region')['Profit'].sum().reset_index()
fig_region = px.bar(region_profit, x='Profit', y='Region', orientation='h', title="Profit by Region", color='Region')
st.plotly_chart(fig_region, use_container_width=True)

# =========================
# DOWNLOAD FILTERED DATA
# =========================
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_superstore_data.csv',
    mime='text/csv'
)
