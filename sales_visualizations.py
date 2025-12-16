import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
df['Quarter'] = df['Order Date'].dt.quarter

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Create comprehensive visualizations
fig = plt.figure(figsize=(20, 24))

# 1. Sales by Category
plt.subplot(4, 3, 1)
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=True)
category_sales.plot(kind='barh', color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
plt.title('Total Sales by Category', fontsize=14, fontweight='bold')
plt.xlabel('Sales ($)')
plt.ylabel('Category')
for i, v in enumerate(category_sales.values):
    plt.text(v + 10000, i, f'${v:,.0f}', va='center', fontweight='bold')

# 2. Sales by Region
plt.subplot(4, 3, 2)
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4']
plt.pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Sales Distribution by Region', fontsize=14, fontweight='bold')

# 3. Sales by Customer Segment
plt.subplot(4, 3, 3)
segment_sales = df.groupby('Segment')['Sales'].sum().sort_values(ascending=True)
segment_sales.plot(kind='barh', color=['#FECA57', '#FF9FF3', '#54A0FF'])
plt.title('Sales by Customer Segment', fontsize=14, fontweight='bold')
plt.xlabel('Sales ($)')
plt.ylabel('Segment')
for i, v in enumerate(segment_sales.values):
    plt.text(v + 5000, i, f'${v:,.0f}', va='center', fontweight='bold')

# 4. Monthly Sales Trend
plt.subplot(4, 3, 4)
monthly_sales = df.groupby('Month')['Sales'].sum()
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linewidth=3, markersize=8, color='#FF6B6B')
plt.title('Monthly Sales Trend', fontsize=14, fontweight='bold')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(range(1, 13))
plt.grid(True, alpha=0.3)

# 5. Yearly Sales Trend
plt.subplot(4, 3, 5)
yearly_sales = df.groupby('Year')['Sales'].sum()
plt.bar(yearly_sales.index, yearly_sales.values, color=['#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57'])
plt.title('Yearly Sales Performance', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Sales ($)')
for i, v in enumerate(yearly_sales.values):
    plt.text(yearly_sales.index[i], v + 10000, f'${v:,.0f}', ha='center', fontweight='bold')

# 6. Top 10 Sub-Categories
plt.subplot(4, 3, 6)
top_subcategories = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)
top_subcategories.plot(kind='bar', color='#FF9FF3')
plt.title('Top 10 Sub-Categories by Sales', fontsize=14, fontweight='bold')
plt.xlabel('Sub-Category')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45, ha='right')

# 7. Sales Distribution (Histogram)
plt.subplot(4, 3, 7)
plt.hist(df['Sales'], bins=50, color='#54A0FF', alpha=0.7, edgecolor='black')
plt.title('Sales Distribution', fontsize=14, fontweight='bold')
plt.xlabel('Sales Amount ($)')
plt.ylabel('Frequency')
plt.axvline(df['Sales'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: ${df["Sales"].mean():.2f}')
plt.legend()

# 8. Shipping Mode Analysis
plt.subplot(4, 3, 8)
shipping_sales = df.groupby('Ship Mode')['Sales'].sum().sort_values(ascending=True)
shipping_sales.plot(kind='barh', color=['#96CEB4', '#FECA57', '#FF9FF3', '#54A0FF'])
plt.title('Sales by Shipping Mode', fontsize=14, fontweight='bold')
plt.xlabel('Sales ($)')
plt.ylabel('Shipping Mode')

# 9. Top 10 States
plt.subplot(4, 3, 9)
top_states = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
top_states.plot(kind='bar', color='#45B7D1')
plt.title('Top 10 States by Sales', fontsize=14, fontweight='bold')
plt.xlabel('State')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45, ha='right')

# 10. Sales vs Orders by Category
plt.subplot(4, 3, 10)
category_stats = df.groupby('Category').agg({'Sales': 'sum', 'Row ID': 'count'}).reset_index()
category_stats.columns = ['Category', 'Sales', 'Orders']
plt.scatter(category_stats['Orders'], category_stats['Sales'], s=200, alpha=0.7, c=['#FF6B6B', '#4ECDC4', '#45B7D1'])
for i, txt in enumerate(category_stats['Category']):
    plt.annotate(txt, (category_stats['Orders'].iloc[i], category_stats['Sales'].iloc[i]), 
                xytext=(5, 5), textcoords='offset points', fontweight='bold')
plt.title('Sales vs Orders by Category', fontsize=14, fontweight='bold')
plt.xlabel('Number of Orders')
plt.ylabel('Total Sales ($)')

# 11. Quarterly Sales Trend
plt.subplot(4, 3, 11)
quarterly_sales = df.groupby(['Year', 'Quarter'])['Sales'].sum().reset_index()
quarterly_sales['Period'] = quarterly_sales['Year'].astype(str) + '-Q' + quarterly_sales['Quarter'].astype(str)
plt.plot(range(len(quarterly_sales)), quarterly_sales['Sales'], marker='o', linewidth=3, markersize=8, color='#96CEB4')
plt.title('Quarterly Sales Trend', fontsize=14, fontweight='bold')
plt.xlabel('Quarter')
plt.ylabel('Sales ($)')
plt.xticks(range(len(quarterly_sales)), quarterly_sales['Period'], rotation=45)
plt.grid(True, alpha=0.3)

# 12. Average Order Value by Segment
plt.subplot(4, 3, 12)
avg_order_value = df.groupby('Segment')['Sales'].mean().sort_values(ascending=True)
avg_order_value.plot(kind='barh', color=['#FECA57', '#FF9FF3', '#54A0FF'])
plt.title('Average Order Value by Segment', fontsize=14, fontweight='bold')
plt.xlabel('Average Order Value ($)')
plt.ylabel('Segment')
for i, v in enumerate(avg_order_value.values):
    plt.text(v + 2, i, f'${v:.2f}', va='center', fontweight='bold')

plt.tight_layout(pad=3.0)
plt.savefig('sales_analysis_dashboard.png', dpi=300, bbox_inches='tight')
plt.show()

# Create additional focused visualizations
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Heatmap of Sales by Region and Category
pivot_data = df.pivot_table(values='Sales', index='Region', columns='Category', aggfunc='sum')
sns.heatmap(pivot_data, annot=True, fmt='.0f', cmap='YlOrRd', ax=axes[0,0])
axes[0,0].set_title('Sales Heatmap: Region vs Category', fontsize=14, fontweight='bold')

# Box plot of Sales by Category
df.boxplot(column='Sales', by='Category', ax=axes[0,1])
axes[0,1].set_title('Sales Distribution by Category', fontsize=14, fontweight='bold')
axes[0,1].set_xlabel('Category')
axes[0,1].set_ylabel('Sales ($)')

# Time series of daily sales
daily_sales = df.groupby('Order Date')['Sales'].sum().reset_index()
axes[1,0].plot(daily_sales['Order Date'], daily_sales['Sales'], alpha=0.7, color='#4ECDC4')
axes[1,0].set_title('Daily Sales Trend', fontsize=14, fontweight='bold')
axes[1,0].set_xlabel('Date')
axes[1,0].set_ylabel('Sales ($)')
axes[1,0].tick_params(axis='x', rotation=45)

# Top 15 Products by Sales
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(15)
top_products.plot(kind='barh', ax=axes[1,1], color='#FF6B6B')
axes[1,1].set_title('Top 15 Products by Sales', fontsize=14, fontweight='bold')
axes[1,1].set_xlabel('Sales ($)')

plt.tight_layout()
plt.savefig('detailed_sales_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

print("Visualizations created successfully!")
print("Files saved: 'sales_analysis_dashboard.png' and 'detailed_sales_analysis.png'")