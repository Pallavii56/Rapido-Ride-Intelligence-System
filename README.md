Rapido Ride Intelligence System
End-to-End Data Analytics Project using Python | SQL | Power BI

## 📌 Project Overview

The **Rapido Ride Intelligence System** is an end-to-end Data Analytics project that analyzes Rapido ride data to uncover business insights related to ride demand, revenue, customer behavior, ride performance, and operational efficiency.

The project demonstrates the complete analytics workflow, starting from raw data cleaning in Python to SQL database management and interactive Power BI dashboards.

---

# 🎯 Project Objectives

- Clean and preprocess raw ride data.
- Handle missing values and duplicate records.
- Perform feature engineering for business analysis.
- Store processed data in a MySQL database.
- Write SQL business queries for analysis.
- Build interactive Power BI dashboards.
- Generate actionable business insights.

---

# 📊 Dataset Information

**Dataset Name:** Bangalore Rapido Ride Services Dataset

**Source:** Kaggle

**Records:** 50,000

**Original Columns:** 13

**Feature Engineered Columns:** 35

---

# 🛠️ Tech Stack

## Programming

- Python 3.10

## Python Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- SciPy

## Database

- MySQL

## Visualization

- Power BI Desktop

## Development Tools

- VS Code
- MySQL Workbench

---

# 📂 Project Structure

```text
Rapido Ride Intelligence System
│
├── Dataset
│   ├── rapido_raw.csv
│   ├── Cleaned
│   │      cleaned_rides.csv
│   └── Feature_Engineered
│          feature_engineered_rides.csv
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
│   ├── dashboard1.png
│   ├── dashboard2.png
│   ├── dashboard3.png
│   └── dashboard4.png
│
├── Report
│   └── Project_Report.pdf
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Python Workflow

### Data Cleaning

- Removed duplicate records
- Standardized column names
- Converted date and time columns
- Handled missing values
- Corrected data types

### Feature Engineering

Created business-ready features including:

- Year
- Month
- Quarter
- Week Number
- Day
- Weekday
- Hour
- Time of Day
- Peak Hour
- Weekend Indicator
- Ride Revenue
- Fare per KM
- Average Speed
- High Value Ride
- Completed Flag
- Cancelled Flag
- Distance Category
- Duration Category
- Fare Category

### Exploratory Data Analysis (EDA)

- KPI Analysis
- Statistical Summary
- Revenue Analysis
- Ride Trends
- Service Distribution
- Payment Analysis
- Distance Analysis
- Ride Duration Analysis

---

# 🗄️ SQL Workflow

The cleaned and feature-engineered dataset was imported into MySQL.

The SQL layer includes:

- Database Creation
- Table Creation
- Data Import
- Business Queries
- KPI Calculations
- Revenue Analysis
- Ride Analysis

---

# 📈 Power BI Dashboards

## Dashboard 1 — Executive Summary

- Total Rides
- Total Revenue
- Average Fare
- Average Distance
- Ride Status
- Revenue Trend
- Service Distribution

---

## Dashboard 2 — Executive Analytics

- Monthly Revenue Trend
- Revenue by Service
- Peak Hour Analysis
- Payment Distribution
- Top Pickup Locations
- Top Drop Locations

---

## Dashboard 3 — Operations Dashboard

- Hourly Ride Trend
- Ride Status by Service
- Weekend vs Weekday Analysis
- Distance Categories
- Duration Categories
- Cancellation Analysis
- Service Performance

---

## Dashboard 4 — Customer & Revenue Insights

- Revenue by Service
- Revenue vs Ride Count
- Monthly Revenue
- Payment Method Revenue
- Revenue by Distance Category
- High Value Ride Analysis
- Top Revenue Pickup Locations
- Top Revenue Drop Locations
- Fare Distribution
- Decomposition Tree

---

# 📊 Key Business Insights

- Bike services accounted for the highest ride volume.
- Completed rides significantly outnumbered cancelled rides.
- Digital payment methods were the most frequently used.
- Revenue varied across different service types.
- Ride demand peaked during office commuting hours.
- Certain pickup and drop locations consistently generated higher revenue.

---

# 📸 Dashboard Preview

## Dashboard 1 – Executive Summary

*(Insert Screenshot Here)*

---

## Dashboard 2 – Executive Analytics

*(Insert Screenshot Here)*

---

## Dashboard 3 – Operations Dashboard

*(Insert Screenshot Here)*

---

## Dashboard 4 – Customer & Revenue Insights

*(Insert Screenshot Here)*

---

# 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Rapido-Ride-Intelligence-System.git
```

### 2. Install required libraries

```bash
pip install -r requirements.txt
```

### 3. Run Python scripts

```bash
python cleaning.py

python feature_engineering.py

python eda.py
```

### 4. Execute SQL scripts

Run the following files in MySQL Workbench:

- create_tables.sql
- insert_data.sql
- business_queries.sql

### 5. Open Power BI

Open:

```
Rapido Dashboard.pbix
```

Refresh the data if required.

---

# 💼 Skills Demonstrated

- Data Cleaning
- Data Preprocessing
- Feature Engineering
- Exploratory Data Analysis
- SQL Query Writing
- Database Design
- Data Visualization
- Dashboard Design
- Business Intelligence
- KPI Development
- Data Storytelling

---

# 🔮 Future Enhancements

- Real-time ride monitoring
- Predictive demand forecasting
- Customer segmentation
- Driver performance analytics
- Geographic route analysis
- Machine learning-based fare prediction

---

# 👩‍💻 Author

**Naina**

### Technologies Used

- Python
- Pandas
- NumPy
- MySQL
- Power BI
- VS Code

---

## ⭐ If you found this project useful, consider giving it a star!
