import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
from django.shortcuts import render
import os

def load_data():
    df = pd.read_csv('train.csv')
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    return df

def dashboard(request):
    df = load_data()
    
    # Key metrics
    total_sales = df['Sales'].sum()
    total_orders = len(df)
    avg_order_value = df['Sales'].mean()
    unique_customers = df['Customer Name'].nunique()
    
    # Category chart
    category_sales = df.groupby('Category')['Sales'].sum().reset_index()
    fig1 = px.pie(category_sales, values='Sales', names='Category', 
                  title='Sales by Category', color_discrete_sequence=px.colors.qualitative.Set3)
    chart1 = plot(fig1, output_type='div', include_plotlyjs=False)
    
    # Regional chart
    region_sales = df.groupby('Region')['Sales'].sum().reset_index()
    fig2 = px.bar(region_sales, x='Region', y='Sales', 
                  title='Sales by Region', color='Sales', color_continuous_scale='Blues')
    chart2 = plot(fig2, output_type='div', include_plotlyjs=False)
    
    # Monthly trend
    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
    fig3 = px.line(monthly_sales, x='Month', y='Sales', 
                   title='Monthly Sales Trend', markers=True)
    chart3 = plot(fig3, output_type='div', include_plotlyjs=False)
    
    # Top products
    top_products = df.groupby('Product Name')['Sales'].sum().nlargest(10).reset_index()
    fig4 = px.bar(top_products, x='Sales', y='Product Name', 
                  title='Top 10 Products', orientation='h', color='Sales')
    chart4 = plot(fig4, output_type='div', include_plotlyjs=False)
    
    context = {
        'total_sales': f"${total_sales:,.2f}",
        'total_orders': f"{total_orders:,}",
        'avg_order_value': f"${avg_order_value:.2f}",
        'unique_customers': f"{unique_customers:,}",
        'chart1': chart1,
        'chart2': chart2,
        'chart3': chart3,
        'chart4': chart4,
    }
    
    return render(request, 'dashboard/dashboard.html', context)

def insights(request):
    df = load_data()
    
    # Business insights
    category_analysis = df.groupby('Category').agg({
        'Sales': ['sum', 'mean', 'count']
    }).round(2)
    
    region_analysis = df.groupby('Region').agg({
        'Sales': ['sum', 'mean', 'count']
    }).round(2)
    
    segment_analysis = df.groupby('Segment').agg({
        'Sales': ['sum', 'mean', 'count']
    }).round(2)
    
    # Top performers
    top_customers = df.groupby('Customer Name')['Sales'].sum().nlargest(5)
    top_states = df.groupby('State')['Sales'].sum().nlargest(5)
    
    context = {
        'category_analysis': category_analysis.to_html(classes='table table-striped'),
        'region_analysis': region_analysis.to_html(classes='table table-striped'),
        'segment_analysis': segment_analysis.to_html(classes='table table-striped'),
        'top_customers': top_customers.to_dict(),
        'top_states': top_states.to_dict(),
    }
    
    return render(request, 'dashboard/insights.html', context)