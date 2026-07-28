"""
============================================================
RAPIDO RIDE INTELLIGENCE SYSTEM
Data Cleaning Script
============================================================

Purpose:
    Clean the raw Rapido dataset before feature engineering,
    SQL analysis, and Power BI dashboard creation.

Author : Naina
"""

import pandas as pd
from pathlib import Path

# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "Dataset" / "Raw" / "rides_data.csv"

OUTPUT_DATA = BASE_DIR / "Dataset" / "Cleaned" / "cleaned_rides.csv"

# ============================================================
# CHECK FILE EXISTS
# ============================================================

if not RAW_DATA.exists():
    raise FileNotFoundError(
        f"Dataset not found:\n{RAW_DATA}"
    )

# ============================================================
# LOAD DATASET
# ============================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(RAW_DATA)

print("Dataset Loaded Successfully.")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# ============================================================
# STANDARDIZE COLUMN NAMES
# ============================================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nColumns Found")
print(df.columns.tolist())

# ============================================================
# REMOVE DUPLICATE ROWS
# ============================================================

duplicate_rows = df.duplicated().sum()

print(f"\nDuplicate Rows : {duplicate_rows}")

df.drop_duplicates(inplace=True)

# ============================================================
# REMOVE DUPLICATE RIDE IDS
# ============================================================

if "ride_id" in df.columns:

    duplicate_ids = df["ride_id"].duplicated().sum()

    print(f"Duplicate Ride IDs : {duplicate_ids}")

    df.drop_duplicates(
        subset="ride_id",
        inplace=True
    )

# ============================================================
# MISSING VALUES
# ============================================================

print("\nMissing Values Before Cleaning")

print(df.isnull().sum())

# ============================================================
# NUMERIC COLUMNS
# ============================================================

numeric_columns = [

    "duration",

    "distance",

    "ride_charge",

    "misc_charge",

    "total_fare"

]

for col in numeric_columns:

    if col in df.columns:

        df[col] = pd.to_numeric(

            df[col],

            errors="coerce"

        )

# ============================================================
# FILL NUMERIC NULLS
# ============================================================

for col in numeric_columns:

    if col in df.columns:

        median = df[col].median()

        df[col].fillna(

            median,

            inplace=True

        )

# ============================================================
# TEXT COLUMNS
# ============================================================

text_columns = [

    "services",

    "ride_status",

    "source",

    "destination",

    "payment_method"

]

for col in text_columns:

    if col in df.columns:

        df[col] = (

            df[col]

            .fillna("Unknown")

            .astype(str)

            .str.strip()

            .str.title()

        )

# ============================================================
# DATE COLUMN
# ============================================================

df["date"] = pd.to_datetime(

    df["date"],

    errors="coerce"

)

# ============================================================
# TIME COLUMN
# ============================================================

time_values = pd.to_datetime(

    df["time"],

    format="%H:%M:%S.%f",

    errors="coerce"

)

# Store clean HH:MM:SS only
df["time"] = time_values.dt.strftime("%H:%M:%S")

# ============================================================
# REMOVE INVALID NUMERIC VALUES
# ============================================================

for col in numeric_columns:

    if col in df.columns:

        df = df[df[col] >= 0]

# ============================================================
# REMOVE EMPTY ROWS
# ============================================================

df.dropna(

    how="all",

    inplace=True

)

# ============================================================
# ROUND NUMERIC VALUES
# ============================================================

for col in numeric_columns:

    if col in df.columns:

        df[col] = df[col].round(2)

# ============================================================
# SORT DATA
# ============================================================

df.sort_values(

    by=["date", "time"],

    inplace=True

)

df.reset_index(

    drop=True,

    inplace=True

)

# ============================================================
# FINAL QUALITY CHECK
# ============================================================

print("\nMissing Values After Cleaning")

print(df.isnull().sum())

print("\nFinal Dataset Shape")

print(df.shape)

print("\nData Types")

print(df.dtypes)

print("\nDataset Preview")

print(df.head())

# ============================================================
# SAVE CLEAN DATASET
# ============================================================

OUTPUT_DATA.parent.mkdir(

    parents=True,

    exist_ok=True

)

df.to_csv(

    OUTPUT_DATA,

    index=False

)

# ============================================================
# SUCCESS MESSAGE
# ============================================================

print("\n" + "=" * 60)

print("Cleaning Completed Successfully")

print("=" * 60)

print(f"Saved To :\n{OUTPUT_DATA}")