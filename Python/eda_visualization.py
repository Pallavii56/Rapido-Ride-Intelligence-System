"""
==========================================================
Rapido Ride Intelligence System
EDA Visualization Module
==========================================================
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------
# Paths
# -------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "Dataset",
    "Feature_Engineered",
    "feature_engineered_rides.csv"
)

IMAGE_FOLDER = os.path.join(
    BASE_DIR,
    "Images",
    "EDA_Charts"
)

os.makedirs(IMAGE_FOLDER, exist_ok=True)

# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

print("=" * 60)
print("Loading Feature Engineered Dataset...")
print("=" * 60)

df = pd.read_csv(DATA_PATH)

print(df.shape)

# -------------------------------------------------------
# Graph Style
# -------------------------------------------------------

plt.style.use("ggplot")

# -------------------------------------------------------
# Helper Function
# -------------------------------------------------------

def save_chart(filename):

    path = os.path.join(IMAGE_FOLDER, filename)

    plt.tight_layout()
    plt.savefig(path, dpi=300)
    plt.close()

    print(f"Saved : {filename}")

# =======================================================
# 1 Revenue by Service
# =======================================================

service = (
    df.groupby("services")["total_fare"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
service.plot(kind="bar")
plt.title("Revenue by Service")
plt.xlabel("Service")
plt.ylabel("Revenue")
save_chart("01_Revenue_by_Service.png")

# =======================================================
# 2 Ride Status
# =======================================================

status = df["ride_status"].value_counts()

plt.figure(figsize=(6,6))
status.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Ride Status Distribution")
save_chart("02_Ride_Status.png")

# =======================================================
# 3 Payment Method
# =======================================================

payment = df["payment_method"].value_counts()

plt.figure(figsize=(8,5))
payment.plot(kind="bar")
plt.title("Payment Method")
plt.xlabel("Payment")
plt.ylabel("Ride Count")
save_chart("03_Payment_Method.png")

# =======================================================
# 4 Hourly Demand
# =======================================================

hour = df.groupby("Hour").size()

plt.figure(figsize=(10,5))
hour.plot(kind="line", marker="o")
plt.title("Hourly Ride Demand")
plt.xlabel("Hour")
plt.ylabel("Rides")
save_chart("04_Hourly_Demand.png")

# =======================================================
# 5 Weekday Demand
# =======================================================

days = [
    "Monday","Tuesday","Wednesday",
    "Thursday","Friday","Saturday","Sunday"
]

weekday = (
    df["Weekday"]
    .value_counts()
    .reindex(days)
)

plt.figure(figsize=(9,5))
weekday.plot(kind="bar")
plt.title("Ride Count by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Ride Count")
save_chart("05_Weekday.png")

# =======================================================
# 6 Distance Distribution
# =======================================================

plt.figure(figsize=(8,5))
plt.hist(df["distance"], bins=30)
plt.title("Distance Distribution")
plt.xlabel("Distance")
plt.ylabel("Frequency")
save_chart("06_Distance_Distribution.png")

# =======================================================
# 7 Fare Distribution
# =======================================================

plt.figure(figsize=(8,5))
plt.hist(df["total_fare"], bins=30)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")
save_chart("07_Fare_Distribution.png")

# =======================================================
# 8 Top Pickup Locations
# =======================================================

pickup = (
    df["source"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(9,5))
pickup.plot(kind="bar")
plt.title("Top 10 Pickup Locations")
plt.xlabel("Location")
plt.ylabel("Ride Count")
save_chart("08_Top_Pickup_Locations.png")

print("\n" + "="*60)
print("Visualization Completed Successfully")
print("="*60)
print(f"Charts Saved To :\n{IMAGE_FOLDER}")