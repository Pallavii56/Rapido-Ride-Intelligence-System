"""
===========================================================
Rapido Ride Intelligence System
EDA Report Generator
===========================================================
"""

import os
import pandas as pd
from datetime import datetime

# ===========================================================
# Paths
# ===========================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REPORT_FOLDER = os.path.join(BASE_DIR, "Report")
IMAGE_FOLDER = os.path.join(BASE_DIR, "Images", "EDA_Charts")

os.makedirs(REPORT_FOLDER, exist_ok=True)

KPI_FILE = os.path.join(REPORT_FOLDER, "KPI_Report.csv")
MISSING_FILE = os.path.join(REPORT_FOLDER, "Missing_Value_Report.csv")
DUPLICATE_FILE = os.path.join(REPORT_FOLDER, "Duplicate_Report.csv")
OUTLIER_FILE = os.path.join(REPORT_FOLDER, "Outlier_Report.csv")
SUMMARY_FILE = os.path.join(REPORT_FOLDER, "Project_Report.txt")

# ===========================================================
# Helper Function
# ===========================================================

def section(file, title):
    file.write("\n")
    file.write("=" * 70 + "\n")
    file.write(title + "\n")
    file.write("=" * 70 + "\n\n")


# ===========================================================
# Generate Report
# ===========================================================

with open(SUMMARY_FILE, "w", encoding="utf-8") as report:

    report.write("=" * 70 + "\n")
    report.write("RAPIDO RIDE INTELLIGENCE SYSTEM\n")
    report.write("EDA FINAL REPORT\n")
    report.write("=" * 70 + "\n\n")

    report.write(
        f"Generated On : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n\n"
    )

    # =======================================================
    # KPI SECTION
    # =======================================================

    section(report, "BUSINESS KPI SUMMARY")

    if os.path.exists(KPI_FILE):

        kpi = pd.read_csv(KPI_FILE)

        for _, row in kpi.iterrows():

            report.write(
                f"{row['KPI']:<35} : {row['Value']}\n"
            )

    else:

        report.write("KPI_Report.csv not found.\n")

    # =======================================================
    # Missing Values
    # =======================================================

    section(report, "MISSING VALUE REPORT")

    if os.path.exists(MISSING_FILE):

        missing = pd.read_csv(MISSING_FILE)

        report.write(
            missing.to_string(index=False)
        )

    else:

        report.write("Missing_Value_Report.csv not found.\n")

    # =======================================================
    # Duplicate Report
    # =======================================================

    section(report, "DUPLICATE REPORT")

    if os.path.exists(DUPLICATE_FILE):

        duplicate = pd.read_csv(DUPLICATE_FILE)

        report.write(
            duplicate.to_string(index=False)
        )

    else:

        report.write("Duplicate_Report.csv not found.\n")

    # =======================================================
    # Outlier Report
    # =======================================================

    section(report, "OUTLIER REPORT")

    if os.path.exists(OUTLIER_FILE):

        outlier = pd.read_csv(OUTLIER_FILE)

        report.write(
            outlier.to_string(index=False)
        )

    else:

        report.write("Outlier_Report.csv not found.\n")

    # =======================================================
    # Charts
    # =======================================================

    section(report, "GENERATED VISUALIZATIONS")

    if os.path.exists(IMAGE_FOLDER):

        charts = sorted(os.listdir(IMAGE_FOLDER))

        if charts:

            for chart in charts:

                report.write(f"• {chart}\n")

        else:

            report.write("No charts available.\n")

    else:

        report.write("Image folder not found.\n")

    # =======================================================
    # Business Insights
    # =======================================================

    section(report, "BUSINESS INSIGHTS")

    report.write("1. Analyze peak demand hours.\n")
    report.write("2. Compare weekday vs weekend demand.\n")
    report.write("3. Study cancellation trends.\n")
    report.write("4. Identify high revenue services.\n")
    report.write("5. Optimize driver allocation.\n")
    report.write("6. Improve payment experience.\n")
    report.write("7. Track top pickup & drop locations.\n")
    report.write("8. Monitor average ride distance.\n")
    report.write("9. Monitor average ride duration.\n")
    report.write("10. Use Power BI for interactive dashboards.\n")

    # =======================================================
    # Footer
    # =======================================================

    report.write("\n")
    report.write("=" * 70 + "\n")
    report.write("END OF REPORT\n")
    report.write("=" * 70 + "\n")

print("=" * 60)
print("EDA REPORT GENERATED SUCCESSFULLY")
print("=" * 60)
print(f"\nSaved To:\n{SUMMARY_FILE}")