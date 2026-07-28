# 🚖 Rapido Ride Intelligence System

> **End-to-End Data Analytics Project using Python, MySQL & Power BI**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?logo=mysql)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?logo=pandas)
![Git](https://img.shields.io/badge/Git-Version%20Control-red?logo=git)
![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# 📌 Project Overview

The **Rapido Ride Intelligence System** is an **End-to-End Data Analytics Project** that transforms raw ride-booking data into actionable business insights.

The project demonstrates the complete analytics lifecycle:

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- SQL Database Design
- Business Query Analysis
- Interactive Power BI Dashboards
- Business Insight Generation

This project simulates how a real-world Data Analyst works using Python, SQL and Power BI.

---

# 🚀 Project Highlights

✅ 50,000 Ride Records

✅ 35 Features

✅ Python ETL Pipeline

✅ 22+ Engineered Features

✅ Automated EDA Reports

✅ SQL Database Design

✅ Business Query Analysis

✅ 4 Interactive Power BI Dashboards

✅ GitHub Documentation

---

# 🎯 Business Objectives

This project answers important business questions such as:

- Which ride service generates the highest revenue?
- Which payment method is preferred by customers?
- What are the peak booking hours?
- Which pickup and drop locations receive the most rides?
- Which rides contribute the highest revenue?
- What factors affect ride cancellations?
- How does customer behaviour change over time?
- Which service category performs best?

---

# 📂 Dataset Information

### Dataset

**Bangalore Rapido Ride Services Dataset**

### Dataset Summary

| Metric | Value |
|---------|-------|
| Total Records | 50,000 |
| Total Features | 35 |
| Missing Values | 0 |
| Duplicate Records | Removed |
| Feature Engineered Columns | 22+ |

---

# 🛠 Tech Stack

| Tool | Purpose |
|------|----------|
| Python | Data Cleaning & Feature Engineering |
| Pandas | Data Manipulation |
| NumPy | Numerical Computing |
| Missingno | Missing Value Analysis |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| OpenPyXL | Excel Report Generation |
| MySQL | Database Management |
| Power BI | Dashboard Development |
| Git | Version Control |
| GitHub | Project Hosting |
| VS Code | Development Environment |

---

# 📁 Project Structure

```
Rapido-Ride-Intelligence-System
│
├── Dataset
│   ├── Raw
│   ├── Cleaned
│   └── Feature_Engineered
│
├── Python
│   ├── cleaning.py
│   ├── feature_engineering.py
│   ├── eda.py
│   ├── eda_kpi.py
│   ├── eda_statistics.py
│   ├── eda_visualization.py
│   └── eda_report.py
│
├── SQL
│   ├── create_tables.sql
│   ├── insert_data.sql
│   └── business_queries.sql
│
├── PowerBI
│   └── Rapido Dashboard.pbix
│
├── Images
│   ├── Dashboard_Screenshots
│   ├── EDA_Charts
│   └── logo.png
│
├── Report
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🔄 Project Workflow

```
                    Raw Dataset
                         │
                         ▼
                 Data Cleaning
                         │
                         ▼
             Feature Engineering
                         │
                         ▼
         Exploratory Data Analysis
                         │
                         ▼
                 MySQL Database
                         │
                         ▼
             Business SQL Queries
                         │
                         ▼
          Interactive Power BI Dashboards
                         │
                         ▼
              Business Decision Making
```

---

# ⚙ Feature Engineering

The following business features were created:

- Year
- Month
- Month Number
- Quarter
- Weekday
- Week Number
- Hour
- Minute
- Time Of Day
- Peak Hour
- Weekend Indicator
- Ride Revenue
- Fare Per KM
- Average Speed
- Distance Category
- Duration Category
- Fare Category
- High Value Ride
- Completed Ride
- Cancelled Ride

---

# 📊 Power BI Dashboard Preview

## 🚖 Dashboard 1 — Executive Summary

<p align="center">
<img src="Images/Dashboard_Screenshots/dashboard1_executive_summary.png" width="900">
</p>

---

## 📈 Dashboard 2 — Executive Analytics

<p align="center">
<img src="Images/Dashboard_Screenshots/dashboard2_executive_analytics.png" width="900">
</p>

---

## ⚙ Dashboard 3 — Operations Dashboard

<p align="center">
<img src="Images/Dashboard_Screenshots/dashboard3_operations.png" width="900">
</p>

---

## 💰 Dashboard 4 — Customer & Revenue Insights

<p align="center">
<img src="Images/Dashboard_Screenshots/dashboard4_customer_revenue.png" width="900">
</p>

---

# 📈 Key Performance Indicators (KPIs)

- Total Revenue
- Total Rides
- Completed Rides
- Cancelled Rides
- Completion Rate
- Cancellation Rate
- Average Fare
- Average Distance
- Average Speed
- Peak Hour Analysis
- High Value Ride Count

---

# 📊 Power BI Features

- KPI Cards
- Interactive Slicers
- Dynamic Filters
- Cross Filtering
- Drill Down
- Trend Analysis
- Revenue Analysis
- Location Analysis
- Customer Insights
- Service Performance Analysis

---

# 📉 Python EDA Reports

The project automatically generates:

- KPI Report
- Missing Value Report
- Duplicate Report
- Data Type Report
- Numeric Summary
- Descriptive Statistics
- Correlation Matrix
- Outlier Report
- Unique Value Report
- Final Project Report

---

# 📈 Sample SQL Query

```sql
SELECT
services,
SUM(total_fare) AS Total_Revenue
FROM rapido_rides
GROUP BY services
ORDER BY Total_Revenue DESC;
```

---

# 💡 Key Business Insights

- Bike services generated the highest revenue.
- Digital payment methods dominated ride transactions.
- Evening hours experienced the highest ride demand.
- High-value rides significantly increased total revenue.
- Ride demand varied across services and time periods.
- A few pickup and drop locations contributed to a large percentage of rides.
- Revenue distribution differed across distance categories.

---

# ▶ How to Run the Project

### Clone Repository

```bash
git clone https://github.com/Pallavii56/Rapido-Ride-Intelligence-System.git
```

### Install Dependencies

```bash
pip install -r Python/requirements.txt
```

### Execute Python Pipeline

```bash
python Python/cleaning.py

python Python/feature_engineering.py

python Python/eda.py
```

### Execute SQL Files

```
SQL/create_tables.sql

SQL/insert_data.sql

SQL/business_queries.sql
```

### Open Dashboard

```
PowerBI/Rapido Dashboard.pbix
```

---

# 💼 Skills Demonstrated

- Data Cleaning
- Data Wrangling
- Feature Engineering
- Exploratory Data Analysis
- Statistical Analysis
- SQL Query Writing
- Database Design
- Business Intelligence
- Dashboard Design
- Data Visualization
- Git & GitHub
- Documentation

---

# 🔮 Future Improvements

- Power BI Service Deployment
- Real-Time Dashboard Refresh
- MySQL Live Connection
- Predictive Analytics
- Customer Segmentation
- Machine Learning Forecasting

---

# 👩‍💻 Author

## Pallavi Mohapatra

**Aspiring Data Analyst**

### Skills

Python • SQL • Power BI • Excel • Data Analytics • Data Visualization

**GitHub**

https://github.com/Pallavii56

**LinkedIn**

https://www.linkedin.com/in/pallavi-mohapatra-ml

---

# ⭐ Support

If you found this project useful,

⭐ **Please consider giving this repository a Star!**

It helps others discover the project and motivates future improvements.

---

> **Made with ❤️ using Python, MySQL & Power BI**
