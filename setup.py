"""
setup.py
--------
Run this once to install all dependencies and verify your environment.

Usage:
    python setup.py
"""

import subprocess
import sys
import os

REQUIRED = [
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "jupyter",
    "notebook",
    "mysql-connector-python",
    "sqlalchemy",
    "openpyxl",
]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_folders():
    folders = [
        "data/raw",
        "data/processed",
        "notebooks",
        "sql",
        "powerbi",
        "screenshots",
        "docs",
    ]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
    print("✅ Project folders verified.")

def main():
    print("=" * 55)
    print("  HR Analytics Dashboard — Environment Setup")
    print("  By Rithika N | Data Analyst | Chennai")
    print("=" * 55)
    print()

    print("📦 Installing Python dependencies...")
    for pkg in REQUIRED:
        try:
            __import__(pkg.replace("-", "_").split("==")[0])
            print(f"   ✅ {pkg} already installed")
        except ImportError:
            print(f"   ⬇️  Installing {pkg}...")
            install(pkg)
            print(f"   ✅ {pkg} installed")

    print()
    print("📁 Checking project folder structure...")
    check_folders()

    print()
    print("🔍 Checking for dataset...")
    dataset_path = os.path.join("data", "raw", "WA_Fn-UseC_-HR-Employee-Attrition.csv")
    if os.path.exists(dataset_path):
        print("   ✅ Dataset found!")
    else:
        print("   ⚠️  Dataset NOT found.")
        print("   👉 Please download from Kaggle:")
        print("      https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset")
        print(f"   👉 Save it to: {dataset_path}")

    print()
    print("=" * 55)
    print("✅ Setup complete! Next steps:")
    print()
    print("  1. Download dataset from Kaggle (link above)")
    print("  2. Run: jupyter notebook notebooks/01_data_cleaning_eda.ipynb")
    print("  3. Run SQL files in MySQL Workbench (sql/ folder)")
    print("  4. Open powerbi/HR_Analytics_Dashboard.pbix in Power BI Desktop")
    print("=" * 55)

if __name__ == "__main__":
    main()
