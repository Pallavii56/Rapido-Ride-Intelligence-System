"""
===========================================================
Rapido Ride Intelligence System
Main EDA Pipeline
===========================================================

This script executes the complete EDA workflow:

1. KPI Analysis
2. Visualizations
3. Statistical Analysis
4. Report Generation

Author : Naina
===========================================================
"""

import time
import subprocess
import os
import sys

# ===========================================================
# Paths
# ===========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SCRIPTS = [
    "eda_kpi.py",
    "eda_visualization.py",
    "eda_statistics.py",
    "eda_report.py"
]

# ===========================================================
# Banner
# ===========================================================

def banner():

    print("\n")
    print("=" * 70)
    print("      RAPIDO RIDE INTELLIGENCE SYSTEM")
    print("      EXPLORATORY DATA ANALYSIS PIPELINE")
    print("=" * 70)
    print()


# ===========================================================
# Run Script
# ===========================================================

def run_script(script_name):

    print("\n")
    print("-" * 70)
    print(f"Running : {script_name}")
    print("-" * 70)

    script_path = os.path.join(BASE_DIR, script_name)

    start = time.time()

    result = subprocess.run(
        [sys.executable, script_path]
    )

    end = time.time()

    if result.returncode == 0:

        print(f"Completed : {script_name}")

    else:

        print(f"Failed : {script_name}")

        sys.exit()

    print(f"Execution Time : {round(end-start,2)} seconds")


# ===========================================================
# Main
# ===========================================================

def main():

    banner()

    total_start = time.time()

    for script in SCRIPTS:

        run_script(script)

    total_end = time.time()

    print("\n")
    print("=" * 70)
    print("EDA PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print("\nModules Executed")

    print("✔ KPI Analysis")

    print("✔ Visualizations")

    print("✔ Statistical Analysis")

    print("✔ Report Generation")

    print("\nOutputs Generated")

    print("✔ KPI Report")

    print("✔ Charts")

    print("✔ Statistics")

    print("✔ Final Project Report")

    print(f"\nTotal Execution Time : {round(total_end-total_start,2)} seconds")

    print("\n")
    print("=" * 70)
    print("Project Ready For SQL & Power BI")
    print("=" * 70)


# ===========================================================
# Execute
# ===========================================================

if __name__ == "__main__":

    main()