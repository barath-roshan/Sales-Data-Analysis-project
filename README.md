# Sales Data Analysis Dashboard

## 🚀 Interactive Django Web Application

A comprehensive sales analytics dashboard built with Django, featuring interactive Plotly charts and business intelligence insights.

## ✨ Features

### 📊 Interactive Dashboard
- **Real-time Metrics**: Total Sales ($2.26M), Orders (9,800), AOV, Customers
- **Interactive Charts**: Pie, Bar, Line charts with hover effects
- **Responsive Design**: Bootstrap 5 with mobile support
- **Professional UI**: Gradient cards, Font Awesome icons

### 📈 Business Intelligence
- **Category Analysis**: Performance across Technology, Furniture, Office Supplies
- **Regional Insights**: Sales distribution across West, East, Central, South
- **Customer Segmentation**: Consumer, Corporate, Home Office analysis
- **Strategic Recommendations**: Data-driven business insights

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5
- **Data Processing**: Pandas 2.2.3
- **Visualizations**: Plotly 5.15.0
- **Frontend**: Bootstrap 5, Font Awesome
- **Database**: SQLite (development)

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Sales-Data-Analysis-project-main
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py migrate
   ```

4. **Start the server**
   ```bash
   python manage.py runserver
   ```

5. **Access the dashboard**
   - Main Dashboard: http://127.0.0.1:8000/
   - Business Insights: http://127.0.0.1:8000/insights/

## 📁 Project Structure

```
sales_dashboard/
├── dashboard/              # Main app
│   ├── templates/         # HTML templates
│   ├── views.py          # Data processing & charts
│   └── urls.py           # URL routing
├── sales_dashboard/       # Django project
├── static/               # Static files
├── train.csv            # Sales data
├── sales_eda.py         # Exploratory analysis
├── key_insights.py      # Business insights
└── requirements.txt     # Dependencies
```

## 📊 Key Insights

- **Technology** leads with 36.6% of sales ($827K)
- **West region** dominates with 31.4% market share
- **Q4 seasonality** shows peak performance (Nov-Dec)
- **Corporate segment** offers highest AOV ($233.15)
- **Growth opportunity** in South region expansion

## 🎯 Business Value

This dashboard transforms raw sales data into actionable business intelligence, enabling:
- Strategic decision making
- Performance monitoring
- Growth opportunity identification
- Customer segment optimization

---

*Built with ❤️ using Django and modern web technologies*