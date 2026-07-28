"""
============================================================
RAPIDO RIDE INTELLIGENCE SYSTEM
Feature Engineering
============================================================

Purpose:
Create business features for SQL analysis and Power BI.

Author : Naina
"""

import pandas as pd
from pathlib import Path

# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "Dataset" / "Cleaned" / "cleaned_rides.csv"

OUTPUT_FILE = (
    BASE_DIR
    / "Dataset"
    / "Feature_Engineered"
    / "feature_engineered_rides.csv"
)

# ============================================================
# CHECK INPUT FILE
# ============================================================

if not INPUT_FILE.exists():
    raise FileNotFoundError(f"Cannot find:\n{INPUT_FILE}")

# ============================================================
# LOAD CLEAN DATA
# ============================================================

print("=" * 60)
print("Loading Clean Dataset...")
print("=" * 60)

df = pd.read_csv(INPUT_FILE)

print(df.shape)

# ============================================================
# DATE FEATURES
# ============================================================

df["date"] = pd.to_datetime(df["date"])

df["Year"] = df["date"].dt.year
df["Month"] = df["date"].dt.month_name()
df["Month_Number"] = df["date"].dt.month
df["Quarter"] = df["date"].dt.quarter
df["Day"] = df["date"].dt.day
df["Weekday"] = df["date"].dt.day_name()
df["Week_Number"] = df["date"].dt.isocalendar().week.astype(int)

# ============================================================
# TIME FEATURES
# ============================================================

time_dt = pd.to_datetime(
    df["time"],
    format="%H:%M:%S",
    errors="coerce"
)

df["Hour"] = time_dt.dt.hour
df["Minute"] = time_dt.dt.minute
df["Second"] = time_dt.dt.second

# ============================================================
# TIME OF DAY
# ============================================================

def get_time_period(hour):

    if hour < 5:
        return "Late Night"

    elif hour < 12:
        return "Morning"

    elif hour < 17:
        return "Afternoon"

    elif hour < 21:
        return "Evening"

    return "Night"

df["Time_Of_Day"] = df["Hour"].apply(get_time_period)

# ============================================================
# PEAK HOURS
# ============================================================

def peak(hour):

    if 7 <= hour <= 10:
        return "Peak"

    elif 17 <= hour <= 21:
        return "Peak"

    return "Non-Peak"

df["Peak_Hour"] = df["Hour"].apply(peak)

# ============================================================
# WEEKEND
# ============================================================

df["Is_Weekend"] = df["Weekday"].isin(
    ["Saturday", "Sunday"]
)

# ============================================================
# RIDE REVENUE
# ============================================================

df["Ride_Revenue"] = df["total_fare"]

# ============================================================
# DISTANCE CATEGORY
# ============================================================

def distance_category(distance):

    if distance < 3:
        return "Short"

    elif distance < 8:
        return "Medium"

    elif distance < 15:
        return "Long"

    return "Very Long"

df["Distance_Category"] = df["distance"].apply(
    distance_category
)

# ============================================================
# DURATION CATEGORY
# ============================================================

def duration_category(duration):

    if duration < 15:
        return "Short"

    elif duration < 30:
        return "Medium"

    elif duration < 60:
        return "Long"

    return "Very Long"

df["Duration_Category"] = df["duration"].apply(
    duration_category
)

# ============================================================
# FARE CATEGORY
# ============================================================

def fare_category(fare):

    if fare < 150:
        return "Low"

    elif fare < 300:
        return "Medium"

    elif fare < 500:
        return "High"

    return "Premium"

df["Fare_Category"] = df["total_fare"].apply(
    fare_category
)

# ============================================================
# FARE PER KM
# ============================================================

df["Fare_Per_KM"] = (
    df["total_fare"] / df["distance"]
).round(2)

df["Fare_Per_KM"] = df["Fare_Per_KM"].replace(
    [float("inf"), -float("inf")],
    0
).fillna(0)

# ============================================================
# AVERAGE SPEED
# ============================================================

df["Average_Speed"] = (
    df["distance"] /
    (df["duration"] / 60)
).round(2)

df["Average_Speed"] = df["Average_Speed"].replace(
    [float("inf"), -float("inf")],
    0
).fillna(0)

# ============================================================
# HIGH VALUE RIDE
# ============================================================

median_fare = df["total_fare"].median()

df["High_Value_Ride"] = (
    df["total_fare"] > median_fare
)

# ============================================================
# CANCELLATION FLAG
# ============================================================

df["Cancelled"] = (
    df["ride_status"]
    .str.lower()
    .eq("cancelled")
)

# ============================================================
# COMPLETION FLAG
# ============================================================

df["Completed"] = (
    df["ride_status"]
    .str.lower()
    .eq("completed")
)

# ============================================================
# SORT
# ============================================================

df = df.sort_values(
    ["date", "Hour", "Minute"]
)

df.reset_index(drop=True, inplace=True)

# ============================================================
# SAVE
# ============================================================

OUTPUT_FILE.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ============================================================
# SUMMARY
# ============================================================

print("\nFeature Engineering Completed")

print("\nRows :", df.shape[0])

print("Columns :", df.shape[1])

print("\nNew Features Created")

new_columns = [
    "Year",
    "Month",
    "Month_Number",
    "Quarter",
    "Day",
    "Weekday",
    "Week_Number",
    "Hour",
    "Minute",
    "Second",
    "Time_Of_Day",
    "Peak_Hour",
    "Is_Weekend",
    "Ride_Revenue",
    "Distance_Category",
    "Duration_Category",
    "Fare_Category",
    "Fare_Per_KM",
    "Average_Speed",
    "High_Value_Ride",
    "Cancelled",
    "Completed"
]

for col in new_columns:
    print("✔", col)

print("\nSaved To")
print(OUTPUT_FILE)