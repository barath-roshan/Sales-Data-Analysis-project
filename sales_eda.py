import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Load the data
df = pd.read_csv('train.csv')

print("=== SALES DATA ANALYSIS - EXPLORATORY DATA ANALYSIS ===\n")

# 1. BASIC DATA OVERVIEW
print("1. BASIC DATA OVERVIEW")
print("=" * 50)
print(f"Dataset Shape: {df.shape}")
print(f"Total Records: {df.shape[0]:,}")
print(f"Total Features: {df.shape[1]}")
print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

# 2. DATA QUALITY ASSESSMENT
print("\n\n2. DATA QUALITY ASSESSMENT")
print("=" * 50)
print("Missing Values:")
missing_data = df.isnull().sum()
print(missing_data[missing_data > 0])

print("\nDuplicate Rows:")
print(f"Number of duplicate rows: {df.duplicated().sum()}")

print("\nBasic Statistics:")
print(df.describe())

# 3. SALES PERFORMANCE ANALYSIS
print("\n\n3. SALES PERFORMANCE ANALYSIS")
print("=" * 50)

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')

# Extract date components
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Quarter'] = df['Order Date'].dt.quarter

# Key metrics
total_sales = df['Sales'].sum()
total_orders = df.shape[0]
avg_order_value = df['Sales'].mean()

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: ${avg_order_value:.2f}")

# 4. CATEGORY ANALYSIS
print("\n\n4. CATEGORY & SUB-CATEGORY ANALYSIS")
print("=" * 50)

# Sales by Category
category_sales = df.groupby('Category')['Sales'].agg(['sum', 'count', 'mean']).round(2)
category_sales.columns = ['Total_Sales', 'Order_Count', 'Avg_Order_Value']
category_sales = category_sales.sort_values('Total_Sales', ascending=False)
print("Sales by Category:")
print(category_sales)

# Top Sub-Categories
print("\nTop 10 Sub-Categories by Sales:")
subcategory_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)
print(subcategory_sales)

# 5. REGIONAL ANALYSIS
print("\n\n5. REGIONAL ANALYSIS")
print("=" * 50)

# Sales by Region
region_sales = df.groupby('Region')['Sales'].agg(['sum', 'count', 'mean']).round(2)
region_sales.columns = ['Total_Sales', 'Order_Count', 'Avg_Order_Value']
region_sales = region_sales.sort_values('Total_Sales', ascending=False)
print("Sales by Region:")
print(region_sales)

# Top States
print("\nTop 10 States by Sales:")
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
print(state_sales)

# 6. CUSTOMER SEGMENT ANALYSIS
print("\n\n6. CUSTOMER SEGMENT ANALYSIS")
print("=" * 50)

segment_analysis = df.groupby('Segment')['Sales'].agg(['sum', 'count', 'mean']).round(2)
segment_analysis.columns = ['Total_Sales', 'Order_Count', 'Avg_Order_Value']
segment_analysis = segment_analysis.sort_values('Total_Sales', ascending=False)
print("Sales by Customer Segment:")
print(segment_analysis)

# 7. TEMPORAL ANALYSIS
print("\n\n7. TEMPORAL ANALYSIS")
print("=" * 50)

# Sales by Year
yearly_sales = df.groupby('Year')['Sales'].sum().sort_index()
print("Sales by Year:")
print(yearly_sales)

# Sales by Month
monthly_sales = df.groupby('Month')['Sales'].sum().sort_index()
print("\nSales by Month:")
print(monthly_sales)

# 8. SHIPPING MODE ANALYSIS
print("\n\n8. SHIPPING MODE ANALYSIS")
print("=" * 50)

shipping_analysis = df.groupby('Ship Mode')['Sales'].agg(['sum', 'count', 'mean']).round(2)
shipping_analysis.columns = ['Total_Sales', 'Order_Count', 'Avg_Order_Value']
shipping_analysis = shipping_analysis.sort_values('Total_Sales', ascending=False)
print("Sales by Shipping Mode:")
print(shipping_analysis)

# 9. TOP CUSTOMERS AND PRODUCTS
print("\n\n9. TOP CUSTOMERS AND PRODUCTS")
print("=" * 50)

# Top Customers
print("Top 10 Customers by Sales:")
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_customers)

# Top Products
print("\nTop 10 Products by Sales:")
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
print(top_products)

# 10. SALES DISTRIBUTION ANALYSIS
print("\n\n10. SALES DISTRIBUTION ANALYSIS")
print("=" * 50)

print(f"Sales Statistics:")
print(f"Minimum Sale: ${df['Sales'].min():.2f}")
print(f"Maximum Sale: ${df['Sales'].max():.2f}")
print(f"Median Sale: ${df['Sales'].median():.2f}")
print(f"Standard Deviation: ${df['Sales'].std():.2f}")

# Quartiles
print(f"\nSales Quartiles:")
print(f"25th Percentile: ${df['Sales'].quantile(0.25):.2f}")
print(f"50th Percentile: ${df['Sales'].quantile(0.50):.2f}")
print(f"75th Percentile: ${df['Sales'].quantile(0.75):.2f}")

print("\n=== EDA COMPLETE ===")
print("Key insights have been generated. Run the visualization script for charts.")