"""
===========================================================
Rapido Ride Intelligence System
EDA Module : KPI Calculations
===========================================================
"""

import os
import pandas as pd

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

REPORT_FOLDER = os.path.join(BASE_DIR, "Report")
os.makedirs(REPORT_FOLDER, exist_ok=True)


# -------------------------------------------------------
# Load Dataset
# -------------------------------------------------------

def load_dataset():

    print("=" * 60)
    print("Loading Feature Engineered Dataset...")
    print("=" * 60)

    df = pd.read_csv(DATA_PATH)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    return df


# -------------------------------------------------------
# Calculate KPIs
# -------------------------------------------------------

def calculate_kpis(df):

    kpis = {}

    # -------------------------------
    # Ride KPIs
    # -------------------------------

    kpis["Total Rides"] = len(df)

    kpis["Completed Rides"] = (
        df["ride_status"]
        .str.lower()
        .eq("completed")
        .sum()
    )

    kpis["Cancelled Rides"] = (
        df["ride_status"]
        .str.lower()
        .eq("cancelled")
        .sum()
    )

    kpis["Completion Rate (%)"] = round(
        (kpis["Completed Rides"] /
         kpis["Total Rides"]) * 100,
        2
    )

    kpis["Cancellation Rate (%)"] = round(
        (kpis["Cancelled Rides"] /
         kpis["Total Rides"]) * 100,
        2
    )

    # -------------------------------
    # Revenue KPIs
    # -------------------------------

    kpis["Total Revenue"] = round(
        df["total_fare"].sum(),
        2
    )

    kpis["Average Fare"] = round(
        df["total_fare"].mean(),
        2
    )

    kpis["Maximum Fare"] = round(
        df["total_fare"].max(),
        2
    )

    kpis["Minimum Fare"] = round(
        df["total_fare"].min(),
        2
    )

    # -------------------------------
    # Distance KPIs
    # -------------------------------

    kpis["Average Distance"] = round(
        df["distance"].mean(),
        2
    )

    kpis["Maximum Distance"] = round(
        df["distance"].max(),
        2
    )

    kpis["Minimum Distance"] = round(
        df["distance"].min(),
        2
    )

    # -------------------------------
    # Duration KPIs
    # -------------------------------

    kpis["Average Duration"] = round(
        df["duration"].mean(),
        2
    )

    kpis["Maximum Duration"] = round(
        df["duration"].max(),
        2
    )

    kpis["Minimum Duration"] = round(
        df["duration"].min(),
        2
    )

    # -------------------------------
    # Speed KPI
    # -------------------------------

    if "Average_Speed" in df.columns:

        kpis["Average Speed"] = round(
            df["Average_Speed"].mean(),
            2
        )

    # -------------------------------
    # High Value Ride
    # -------------------------------

    if "High_Value_Ride" in df.columns:

        kpis["High Value Rides"] = (
            df["High_Value_Ride"]
            .sum()
        )

    # -------------------------------
    # Peak Hour Ride Count
    # -------------------------------

    if "Peak_Hour" in df.columns:

        kpis["Peak Hour Rides"] = (
            df["Peak_Hour"]
            .sum()
        )

    # -------------------------------
    # Weekend Ride Count
    # -------------------------------

    if "Is_Weekend" in df.columns:

        kpis["Weekend Rides"] = (
            df["Is_Weekend"]
            .sum()
        )

    # -------------------------------
    # Unique Customers (Source Areas)
    # -------------------------------

    kpis["Unique Pickup Locations"] = (
        df["source"]
        .nunique()
    )

    kpis["Unique Destination Locations"] = (
        df["destination"]
        .nunique()
    )

    # -------------------------------
    # Services
    # -------------------------------

    kpis["Ride Services"] = (
        df["services"]
        .nunique()
    )

    # -------------------------------
    # Payment Methods
    # -------------------------------

    kpis["Payment Methods"] = (
        df["payment_method"]
        .nunique()
    )

    return kpis


# -------------------------------------------------------
# Print KPIs
# -------------------------------------------------------

def print_kpis(kpis):

    print("\n")
    print("=" * 60)
    print("BUSINESS KPI SUMMARY")
    print("=" * 60)

    for key, value in kpis.items():

        print(f"{key:<35} : {value}")


# -------------------------------------------------------
# Save KPIs
# -------------------------------------------------------

def save_kpis(kpis):

    df = pd.DataFrame(
        kpis.items(),
        columns=["KPI", "Value"]
    )

    output = os.path.join(
        REPORT_FOLDER,
        "KPI_Report.csv"
    )

    df.to_csv(
        output,
        index=False
    )

    print("\nKPI Report Saved Successfully")
    print(output)


# -------------------------------------------------------
# Main
# -------------------------------------------------------

def run_kpi_analysis():

    df = load_dataset()

    kpis = calculate_kpis(df)

    print_kpis(kpis)

    save_kpis(kpis)

    return df, kpis


if __name__ == "__main__":

    run_kpi_analysis()