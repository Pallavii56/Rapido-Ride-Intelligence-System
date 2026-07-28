"""
===========================================================
Rapido Ride Intelligence System
EDA Statistics Module
===========================================================
"""

import os
import pandas as pd

# ===========================================================
# Paths
# ===========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "Dataset",
    "Feature_Engineered",
    "feature_engineered_rides.csv"
)

REPORT_FOLDER = os.path.join(
    BASE_DIR,
    "Report"
)

os.makedirs(REPORT_FOLDER, exist_ok=True)

# ===========================================================
# Load Dataset
# ===========================================================

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

df = pd.read_csv(DATA_PATH)

print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

# ===========================================================
# Dataset Information
# ===========================================================

print("\nDataset Information")
print(df.info())

# ===========================================================
# Missing Values
# ===========================================================

missing = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum(),
    "Percentage": (
        df.isnull().sum() / len(df) * 100
    ).round(2)
})

missing.to_csv(
    os.path.join(
        REPORT_FOLDER,
        "Missing_Value_Report.csv"
    ),
    index=False
)

print("\nMissing Value Report Saved")

# ===========================================================
# Descriptive Statistics
# ===========================================================

statistics = df.describe(include="all")

statistics.to_csv(
    os.path.join(
        REPORT_FOLDER,
        "Descriptive_Statistics.csv"
    )
)

print("Descriptive Statistics Saved")

# ===========================================================
# Numerical Statistics
# ===========================================================

numeric = df.select_dtypes(include="number")

summary = pd.DataFrame({
    "Mean": numeric.mean(),
    "Median": numeric.median(),
    "Minimum": numeric.min(),
    "Maximum": numeric.max(),
    "Standard Deviation": numeric.std(),
    "Variance": numeric.var(),
    "Skewness": numeric.skew(),
    "Kurtosis": numeric.kurt()
})

summary = summary.round(2)

summary.to_csv(
    os.path.join(
        REPORT_FOLDER,
        "Numeric_Summary.csv"
    )
)

print("Numeric Summary Saved")

# ===========================================================
# Correlation Matrix
# ===========================================================

correlation = numeric.corr().round(2)

correlation.to_csv(
    os.path.join(
        REPORT_FOLDER,
        "Correlation_Matrix.csv"
    )
)

print("Correlation Matrix Saved")

# ===========================================================
# Duplicate Report
# ===========================================================

duplicates = pd.DataFrame({

    "Total Rows": [len(df)],

    "Duplicate Rows": [df.duplicated().sum()]

})

duplicates.to_csv(

    os.path.join(

        REPORT_FOLDER,

        "Duplicate_Report.csv"

    ),

    index=False

)

print("Duplicate Report Saved")

# ===========================================================
# Data Types
# ===========================================================

dtype = pd.DataFrame({

    "Column": df.columns,

    "Data Type": df.dtypes.astype(str)

})

dtype.to_csv(

    os.path.join(

        REPORT_FOLDER,

        "Data_Types.csv"

    ),

    index=False

)

print("Data Type Report Saved")

# ===========================================================
# Unique Values
# ===========================================================

unique = pd.DataFrame({

    "Column": df.columns,

    "Unique Values": [

        df[col].nunique()

        for col in df.columns

    ]

})

unique.to_csv(

    os.path.join(

        REPORT_FOLDER,

        "Unique_Values.csv"

    ),

    index=False

)

print("Unique Value Report Saved")

# ===========================================================
# Outlier Detection (IQR)
# ===========================================================

outliers = []

for col in numeric.columns:

    Q1 = numeric[col].quantile(0.25)

    Q3 = numeric[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR

    upper = Q3 + 1.5 * IQR

    count = numeric[
        (numeric[col] < lower) |
        (numeric[col] > upper)
    ].shape[0]

    outliers.append([col, count])

outlier_df = pd.DataFrame(

    outliers,

    columns=["Column", "Outliers"]

)

outlier_df.to_csv(

    os.path.join(

        REPORT_FOLDER,

        "Outlier_Report.csv"

    ),

    index=False

)

print("Outlier Report Saved")

# ===========================================================
# Summary Report
# ===========================================================

with open(

    os.path.join(

        REPORT_FOLDER,

        "Summary_Report.txt"

    ),

    "w",

    encoding="utf-8"

) as f:

    f.write("=" * 60 + "\n")

    f.write("RAPIDO DATASET SUMMARY\n")

    f.write("=" * 60 + "\n\n")

    f.write(f"Rows : {df.shape[0]}\n")

    f.write(f"Columns : {df.shape[1]}\n\n")

    f.write("Missing Values\n")

    f.write(str(df.isnull().sum()))

    f.write("\n\n")

    f.write("Data Types\n")

    f.write(str(df.dtypes))

    f.write("\n\n")

    f.write("Statistical Summary\n")

    f.write(str(df.describe()))

print("Summary Report Saved")

# ===========================================================
# Finished
# ===========================================================

print("\n" + "=" * 60)
print("EDA Statistics Completed Successfully")
print("=" * 60)

print("\nReports Saved To")

print(REPORT_FOLDER)