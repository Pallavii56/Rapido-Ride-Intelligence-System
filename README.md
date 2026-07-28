# 🚖 Rapido Ride Intelligence System

> End-to-End Data Analytics Project using **Python, MySQL & Power BI**

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)
![MySQL](https://img.shields.io/badge/MySQL-Database-blue?logo=mysql)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-black?logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Project Overview

The **Rapido Ride Intelligence System** is an end-to-end Business Intelligence project developed to analyze ride-booking operations and generate actionable business insights.

The project covers the complete analytics pipeline:

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis (EDA)
- SQL Database Design
- Business Query Analysis
- Interactive Power BI Dashboards

The objective is to transform raw ride data into meaningful insights that support business decision-making.

---

# 🎯 Business Objectives

This project helps answer questions such as:

- Which ride service generates the highest revenue?
- Which payment method is most preferred?
- What are the peak booking hours?
- Which pickup and drop locations are busiest?
- Which rides generate the highest revenue?
- What factors influence ride cancellations?
- How does customer behaviour change over time?

---

# 📂 Dataset Information

**Dataset:** Bangalore Rapido Ride Services Dataset

### Dataset Size

| Item | Value |
|------|-------|
| Total Records | 50,000 |
| Total Features | 35 |
| Missing Values | 0 |
| Duplicate Records | Removed |
| Feature Engineered Columns | 22+ |

---

# 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Missingno
- Matplotlib
- Seaborn
- OpenPyXL
- MySQL
- Power BI
- Git
- GitHub
- VS Code

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
│   ├── logo.png
│   └── EDA_Charts
│
├── Report
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Project Workflow

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
SQL Database
      │
      ▼
Business Queries
      │
      ▼
Power BI Dashboards
      │
      ▼
Business Insights
```

---

# 🔍 Feature Engineering

Created additional business features including:

- Year
- Month
- Quarter
- Weekday
- Week Number
- Hour
- Time Of Day
- Peak Hour
- Ride Revenue
- Fare Per KM
- Average Speed
- Distance Category
- Duration Category
- Fare Category
- Weekend Indicator
- High Value Ride
- Completed Ride
- Cancelled Ride

---

# 📊 Power BI Dashboards
# 📷 Dashboard Preview

## 🚖 Dashboard 1 — Executive Summary

![Dashboard 1](Images/Dashboard_Screenshots/dashboard1_executive_summary.png)

---

## 📊 Dashboard 2 — Executive Analytics

![Dashboard 2](Images/Dashboard_Screenshots/dashboard2_executive_analytics.png)

---

## ⚙ Dashboard 3 — Operations Dashboard

![Dashboard 3](Images/Dashboard_Screenshots/dashboard3_operations.png)

---

## 💰 Dashboard 4 — Customer & Revenue Insights

![Dashboard 4](Images/Dashboard_Screenshots/dashboard4_customer_revenue.png)

---

# 📈 EDA Reports Generated

The project automatically generates:

- KPI Report
- Missing Value Report
- Correlation Matrix
- Outlier Report
- Numeric Summary
- Duplicate Report
- Descriptive Statistics
- Final Project Report

---

# 📌 Key Business Insights

- Bike rides generated the highest revenue.
- Digital payment methods dominate ride transactions.
- Evening hours show the highest ride demand.
- High-value rides contribute significantly to total revenue.
- Ride demand varies by service type and time of day.
- A small number of pickup and drop locations account for a large share of rides.

---

# 🚀 How to Run

Clone the repository

```bash
git clone https://github.com/Pallavii56/Rapido-Ride-Intelligence-System.git
```

Install dependencies

```bash
pip install -r Python/requirements.txt
```

Run the pipeline

```bash
python Python/cleaning.py
python Python/feature_engineering.py
python Python/eda.py
```

Execute SQL scripts

```
create_tables.sql

insert_data.sql

business_queries.sql
```

Open

```
PowerBI/Rapido Dashboard.pbix
```

---

# 📷 Dashboard Preview

> Add screenshots here.

Example:

```
Images/dashboard1.png

Images/dashboard2.png

Images/dashboard3.png

Images/dashboard4.png
```

---

# 📚 Skills Demonstrated

- Data Cleaning
- Data Transformation
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

- Add real-time dashboard refresh
- Connect Power BI directly with MySQL
- Deploy dashboards to Power BI Service
- Build predictive analytics models
- Add customer segmentation analysis

---

# 👩‍💻 Author

**Pallavi Mohapatra**

Aspiring Data Analyst | Python | SQL | Power BI

GitHub:
https://github.com/Pallavii56

LinkedIn:
www.linkedin.com/in/pallavi-mohapatra-ml

---

⭐ If you found this project useful, consider giving it a star.
