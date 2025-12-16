import pandas as pd
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Load and prepare data
df = pd.read_csv('train.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

print("=== KEY BUSINESS INSIGHTS FROM SALES DATA ANALYSIS ===\n")

# 1. OVERALL PERFORMANCE METRICS
print("1. OVERALL BUSINESS PERFORMANCE")
print("=" * 50)
total_sales = df['Sales'].sum()
total_orders = len(df)
avg_order_value = df['Sales'].mean()
unique_customers = df['Customer Name'].nunique()
unique_products = df['Product Name'].nunique()

print(f"Total Sales Revenue: ${total_sales:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Average Order Value: ${avg_order_value:.2f}")
print(f"Unique Customers: {unique_customers:,}")
print(f"Unique Products: {unique_products:,}")

# 2. CATEGORY PERFORMANCE INSIGHTS
print("\n\n2. CATEGORY PERFORMANCE INSIGHTS")
print("=" * 50)
category_analysis = df.groupby('Category').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Customer Name': 'nunique'
}).round(2)

category_analysis.columns = ['Total_Sales', 'Avg_Order_Value', 'Order_Count', 'Unique_Customers']
category_analysis = category_analysis.sort_values('Total_Sales', ascending=False)

print("Category Rankings by Total Sales:")
for i, (category, row) in enumerate(category_analysis.iterrows(), 1):
    percentage = (row['Total_Sales'] / total_sales) * 100
    print(f"{i}. {category}: ${row['Total_Sales']:,.2f} ({percentage:.1f}% of total sales)")
    print(f"   - Average Order Value: ${row['Avg_Order_Value']:.2f}")
    print(f"   - Total Orders: {row['Order_Count']:,}")
    print(f"   - Unique Customers: {row['Unique_Customers']:,}")

# Identify best performing sub-categories
print("\nTOP PERFORMING SUB-CATEGORIES:")
top_subcategories = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(5)
for i, (subcat, sales) in enumerate(top_subcategories.items(), 1):
    print(f"{i}. {subcat}: ${sales:,.2f}")

# 3. REGIONAL INSIGHTS
print("\n\n3. REGIONAL PERFORMANCE INSIGHTS")
print("=" * 50)
region_analysis = df.groupby('Region').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Customer Name': 'nunique'
}).round(2)

region_analysis.columns = ['Total_Sales', 'Avg_Order_Value', 'Order_Count', 'Unique_Customers']
region_analysis = region_analysis.sort_values('Total_Sales', ascending=False)

print("Regional Performance Rankings:")
for i, (region, row) in enumerate(region_analysis.iterrows(), 1):
    percentage = (row['Total_Sales'] / total_sales) * 100
    print(f"{i}. {region}: ${row['Total_Sales']:,.2f} ({percentage:.1f}% of total sales)")
    print(f"   - Average Order Value: ${row['Avg_Order_Value']:.2f}")
    print(f"   - Market Penetration: {row['Unique_Customers']:,} customers")

# Top performing states
print("\nTOP 5 STATES BY SALES:")
top_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(5)
for i, (state, sales) in enumerate(top_states.items(), 1):
    print(f"{i}. {state}: ${sales:,.2f}")

# 4. CUSTOMER SEGMENT INSIGHTS
print("\n\n4. CUSTOMER SEGMENT INSIGHTS")
print("=" * 50)
segment_analysis = df.groupby('Segment').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Customer Name': 'nunique'
}).round(2)

segment_analysis.columns = ['Total_Sales', 'Avg_Order_Value', 'Order_Count', 'Unique_Customers']
segment_analysis = segment_analysis.sort_values('Total_Sales', ascending=False)

print("Customer Segment Performance:")
for i, (segment, row) in enumerate(segment_analysis.iterrows(), 1):
    percentage = (row['Total_Sales'] / total_sales) * 100
    avg_orders_per_customer = row['Order_Count'] / row['Unique_Customers']
    print(f"{i}. {segment}: ${row['Total_Sales']:,.2f} ({percentage:.1f}% of total sales)")
    print(f"   - Average Order Value: ${row['Avg_Order_Value']:.2f}")
    print(f"   - Average Orders per Customer: {avg_orders_per_customer:.1f}")

# 5. TEMPORAL INSIGHTS
print("\n\n5. TEMPORAL PERFORMANCE INSIGHTS")
print("=" * 50)

# Yearly growth
yearly_sales = df.groupby('Year')['Sales'].sum().sort_index()
print("Year-over-Year Performance:")
for year, sales in yearly_sales.items():
    percentage = (sales / total_sales) * 100
    print(f"{year}: ${sales:,.2f} ({percentage:.1f}% of total sales)")

# Calculate growth rates
if len(yearly_sales) > 1:
    print("\nYear-over-Year Growth Rates:")
    for i in range(1, len(yearly_sales)):
        current_year = yearly_sales.index[i]
        previous_year = yearly_sales.index[i-1]
        growth_rate = ((yearly_sales.iloc[i] - yearly_sales.iloc[i-1]) / yearly_sales.iloc[i-1]) * 100
        print(f"{previous_year} to {current_year}: {growth_rate:+.1f}%")

# Best performing months
monthly_sales = df.groupby('Month')['Sales'].sum().sort_values(ascending=False)
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print("\nTOP 5 MONTHS BY SALES:")
for i, (month, sales) in enumerate(monthly_sales.head(5).items(), 1):
    print(f"{i}. {month_names[month-1]}: ${sales:,.2f}")

# 6. SHIPPING AND LOGISTICS INSIGHTS
print("\n\n6. SHIPPING & LOGISTICS INSIGHTS")
print("=" * 50)
shipping_analysis = df.groupby('Ship Mode').agg({
    'Sales': ['sum', 'mean', 'count']
}).round(2)

shipping_analysis.columns = ['Total_Sales', 'Avg_Order_Value', 'Order_Count']
shipping_analysis = shipping_analysis.sort_values('Total_Sales', ascending=False)

print("Shipping Mode Performance:")
for mode, row in shipping_analysis.iterrows():
    percentage = (row['Total_Sales'] / total_sales) * 100
    print(f"{mode}: ${row['Total_Sales']:,.2f} ({percentage:.1f}% of total sales)")
    print(f"   - Average Order Value: ${row['Avg_Order_Value']:.2f}")
    print(f"   - Order Volume: {row['Order_Count']:,}")

# 7. TOP PERFORMERS
print("\n\n7. TOP PERFORMERS")
print("=" * 50)

# Top customers
print("TOP 5 CUSTOMERS BY SALES:")
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)
for i, (customer, sales) in enumerate(top_customers.items(), 1):
    orders = df[df['Customer Name'] == customer].shape[0]
    avg_order = sales / orders
    print(f"{i}. {customer}: ${sales:,.2f} ({orders} orders, ${avg_order:.2f} avg)")

# Top products
print("\nTOP 5 PRODUCTS BY SALES:")
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
for i, (product, sales) in enumerate(top_products.items(), 1):
    print(f"{i}. {product[:50]}{'...' if len(product) > 50 else ''}: ${sales:,.2f}")

# 8. KEY BUSINESS RECOMMENDATIONS
print("\n\n8. KEY BUSINESS RECOMMENDATIONS")
print("=" * 50)

# Identify growth opportunities
lowest_region = region_analysis.index[-1]
highest_region = region_analysis.index[0]
underperforming_category = category_analysis.index[-1]
top_category = category_analysis.index[0]

print("STRATEGIC RECOMMENDATIONS:")
print(f"1. REGIONAL EXPANSION: Focus on {lowest_region} region - significant growth potential")
print(f"   Current performance: ${region_analysis.loc[lowest_region, 'Total_Sales']:,.2f}")
print(f"   Gap to top region ({highest_region}): ${region_analysis.loc[highest_region, 'Total_Sales'] - region_analysis.loc[lowest_region, 'Total_Sales']:,.2f}")

print(f"\n2. CATEGORY OPTIMIZATION: Improve {underperforming_category} category performance")
print(f"   Current performance: ${category_analysis.loc[underperforming_category, 'Total_Sales']:,.2f}")
print(f"   Potential if matching {top_category}: ${category_analysis.loc[top_category, 'Total_Sales'] - category_analysis.loc[underperforming_category, 'Total_Sales']:,.2f}")

# Seasonal insights
peak_month = monthly_sales.index[0]
low_month = monthly_sales.index[-1]
print(f"\n3. SEASONAL STRATEGY: Capitalize on {month_names[peak_month-1]} peak, boost {month_names[low_month-1]} performance")
print(f"   Peak month sales: ${monthly_sales.iloc[0]:,.2f}")
print(f"   Lowest month sales: ${monthly_sales.iloc[-1]:,.2f}")

print(f"\n4. CUSTOMER RETENTION: Focus on Corporate segment - highest AOV (${segment_analysis.loc['Corporate', 'Avg_Order_Value']:.2f})")

print(f"\n5. SHIPPING OPTIMIZATION: Standard Class dominates - consider premium service promotion")

print("\n" + "="*70)
print("ANALYSIS COMPLETE - DATA-DRIVEN INSIGHTS FOR STRATEGIC DECISIONS")
print("="*70)