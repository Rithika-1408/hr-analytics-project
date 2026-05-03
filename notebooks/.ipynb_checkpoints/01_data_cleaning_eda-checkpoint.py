# ============================================================
# HR Analytics — Data Cleaning & Exploratory Data Analysis
# File: notebooks/01_data_cleaning_eda.ipynb
# Author: Rithika N | Data Analyst | Chennai
# ============================================================
# Run each cell in Jupyter Notebook top to bottom.
# Output: data/processed/hr_cleaned.csv
# ============================================================

# ── CELL 1: Import libraries ────────────────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# Set plot style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("✅ Libraries imported successfully")
print(f"   Pandas version  : {pd.__version__}")
print(f"   NumPy version   : {np.__version__}")


# ── CELL 2: Load dataset ────────────────────────────────────
RAW_PATH = "../data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
PROCESSED_PATH = "../data/processed/hr_cleaned.csv"

df = pd.read_csv(RAW_PATH)

print(f"✅ Dataset loaded successfully")
print(f"   Rows    : {df.shape[0]}")
print(f"   Columns : {df.shape[1]}")
print()
print("First 5 rows:")
df.head()


# ── CELL 3: Basic info ──────────────────────────────────────
print("Dataset Info:")
print("-" * 40)
df.info()

print()
print("Column names:")
print(list(df.columns))


# ── CELL 4: Check for missing values ────────────────────────
print("Missing values per column:")
print("-" * 40)
missing = df.isnull().sum()
print(missing[missing > 0] if missing.sum() > 0 else "✅ No missing values found!")

print()
print("Duplicate rows:", df.duplicated().sum())


# ── CELL 5: Check unique values for key columns ─────────────
categorical_cols = [
    'Attrition', 'BusinessTravel', 'Department', 'EducationField',
    'Gender', 'JobRole', 'MaritalStatus', 'OverTime'
]

for col in categorical_cols:
    print(f"{col}: {df[col].unique()}")


# ── CELL 6: Drop constant/useless columns ───────────────────
# These columns have only 1 unique value — no analytical value
cols_to_drop = ['EmployeeCount', 'Over18', 'StandardHours']
df = df.drop(columns=cols_to_drop)

print(f"✅ Dropped {len(cols_to_drop)} useless columns: {cols_to_drop}")
print(f"   Remaining columns: {df.shape[1]}")


# ── CELL 7: Encode target variable ──────────────────────────
# Attrition: Yes → 1, No → 0 (needed for SQL and Power BI calculations)
df['Attrition_Flag'] = df['Attrition'].map({'Yes': 1, 'No': 0})

print("✅ Attrition encoded:")
print(df['Attrition_Flag'].value_counts())
print()
attrition_rate = df['Attrition_Flag'].mean() * 100
print(f"   Overall Attrition Rate: {attrition_rate:.1f}%")


# ── CELL 8: Create Age Band column ──────────────────────────
def age_band(age):
    if age < 25:
        return 'Under 25'
    elif age < 35:
        return '25-34'
    elif age < 45:
        return '35-44'
    else:
        return '45+'

df['AgeBand'] = df['Age'].apply(age_band)

print("✅ Age Band created:")
print(df['AgeBand'].value_counts())


# ── CELL 9: Create Salary Band column ───────────────────────
def salary_band(income):
    if income < 3000:
        return 'Under $3K'
    elif income < 5000:
        return '$3K-$5K'
    elif income < 8000:
        return '$5K-$8K'
    else:
        return 'Above $8K'

df['SalaryBand'] = df['MonthlyIncome'].apply(salary_band)

print("✅ Salary Band created:")
print(df['SalaryBand'].value_counts())


# ── CELL 10: Create Tenure Band column ──────────────────────
def tenure_band(years):
    if years <= 2:
        return '0-2 Years'
    elif years <= 5:
        return '3-5 Years'
    elif years <= 10:
        return '6-10 Years'
    else:
        return '10+ Years'

df['TenureBand'] = df['YearsAtCompany'].apply(tenure_band)

print("✅ Tenure Band created:")
print(df['TenureBand'].value_counts())


# ── CELL 11: Summary statistics ─────────────────────────────
print("Summary Statistics — Numerical Columns:")
print("-" * 50)
df.describe().round(2)


# ── CELL 12: EDA — Attrition rate by Department ─────────────
dept_attrition = df.groupby('Department')['Attrition_Flag'].agg(['sum', 'count', 'mean'])
dept_attrition.columns = ['Attrition_Count', 'Total', 'Attrition_Rate']
dept_attrition['Attrition_Rate'] = (dept_attrition['Attrition_Rate'] * 100).round(1)
dept_attrition = dept_attrition.sort_values('Attrition_Rate', ascending=False)

print("Attrition by Department:")
print(dept_attrition)

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(dept_attrition.index, dept_attrition['Attrition_Rate'],
              color=['#D85A30', '#1D9E75', '#378ADD'])
ax.set_title('Attrition Rate by Department', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Department')
ax.set_ylabel('Attrition Rate (%)')
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f"{bar.get_height():.1f}%", ha='center', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('../screenshots/01_attrition_by_dept.png', dpi=150)
plt.show()
print("✅ Chart saved to screenshots/")


# ── CELL 13: EDA — Attrition by Age Band ────────────────────
age_order = ['Under 25', '25-34', '35-44', '45+']
age_attrition = df.groupby('AgeBand')['Attrition_Flag'].mean() * 100
age_attrition = age_attrition.reindex(age_order)

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(age_attrition.index, age_attrition.values, color='#0F6E56', alpha=0.85)
ax.set_title('Attrition Rate by Age Band', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Age Band')
ax.set_ylabel('Attrition Rate (%)')
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f"{bar.get_height():.1f}%", ha='center', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('../screenshots/02_attrition_by_age.png', dpi=150)
plt.show()


# ── CELL 14: EDA — Salary vs Attrition ──────────────────────
salary_order = ['Under $3K', '$3K-$5K', '$5K-$8K', 'Above $8K']
salary_attrition = df.groupby('SalaryBand')['Attrition_Flag'].mean() * 100
salary_attrition = salary_attrition.reindex(salary_order)

fig, ax = plt.subplots(figsize=(8, 5))
colors = ['#D85A30', '#EF9F27', '#1D9E75', '#0C447C']
bars = ax.bar(salary_attrition.index, salary_attrition.values, color=colors)
ax.set_title('Attrition Rate by Salary Band', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Salary Band')
ax.set_ylabel('Attrition Rate (%)')
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f"{bar.get_height():.1f}%", ha='center', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('../screenshots/03_attrition_by_salary.png', dpi=150)
plt.show()


# ── CELL 15: EDA — Overtime vs Attrition ────────────────────
overtime_attrition = df.groupby('OverTime')['Attrition_Flag'].mean() * 100

fig, ax = plt.subplots(figsize=(6, 5))
bars = ax.bar(['No Overtime', 'With Overtime'], overtime_attrition.values,
              color=['#1D9E75', '#D85A30'])
ax.set_title('Attrition Rate — Overtime vs No Overtime', fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('Attrition Rate (%)')
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f"{bar.get_height():.1f}%", ha='center', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('../screenshots/04_attrition_by_overtime.png', dpi=150)
plt.show()


# ── CELL 16: EDA — Job Satisfaction Heatmap ─────────────────
pivot = df.pivot_table(
    values='Attrition_Flag',
    index='Department',
    columns='JobSatisfaction',
    aggfunc='mean'
) * 100

fig, ax = plt.subplots(figsize=(9, 5))
sns.heatmap(pivot, annot=True, fmt=".1f", cmap="RdYlGn_r",
            linewidths=0.5, ax=ax, cbar_kws={'label': 'Attrition Rate %'})
ax.set_title('Attrition Rate by Department × Job Satisfaction Score',
             fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Job Satisfaction Score (1=Low, 4=High)')
ax.set_ylabel('Department')
plt.tight_layout()
plt.savefig('../screenshots/05_satisfaction_heatmap.png', dpi=150)
plt.show()


# ── CELL 17: EDA — Age Distribution ─────────────────────────
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(df['Age'], bins=20, color='#0F6E56', edgecolor='white', alpha=0.85)
ax.set_title('Age Distribution of All Employees', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Age')
ax.set_ylabel('Number of Employees')
plt.tight_layout()
plt.savefig('../screenshots/06_age_distribution.png', dpi=150)
plt.show()


# ── CELL 18: Print key findings ─────────────────────────────
print("=" * 55)
print("  KEY FINDINGS FROM EDA")
print("=" * 55)
print(f"  Total employees          : {len(df):,}")
print(f"  Total attrition          : {df['Attrition_Flag'].sum():,}")
print(f"  Overall attrition rate   : {df['Attrition_Flag'].mean()*100:.1f}%")
print()

dept = df.groupby('Department')['Attrition_Flag'].mean()*100
print(f"  Highest attrition dept   : {dept.idxmax()} ({dept.max():.1f}%)")
print(f"  Lowest attrition dept    : {dept.idxmin()} ({dept.min():.1f}%)")
print()

ot_yes = df[df['OverTime']=='Yes']['Attrition_Flag'].mean()*100
ot_no  = df[df['OverTime']=='No']['Attrition_Flag'].mean()*100
print(f"  Attrition (Overtime=Yes) : {ot_yes:.1f}%")
print(f"  Attrition (Overtime=No)  : {ot_no:.1f}%")
print()

low_sal = df[df['SalaryBand']=='Under $3K']['Attrition_Flag'].mean()*100
hi_sal  = df[df['SalaryBand']=='Above $8K']['Attrition_Flag'].mean()*100
print(f"  Attrition (Under $3K)    : {low_sal:.1f}%")
print(f"  Attrition (Above $8K)    : {hi_sal:.1f}%")
print("=" * 55)


# ── CELL 19: Export cleaned data ────────────────────────────
os.makedirs('../data/processed', exist_ok=True)
df.to_csv(PROCESSED_PATH, index=False)

print(f"✅ Cleaned data saved to: {PROCESSED_PATH}")
print(f"   Final shape: {df.shape[0]} rows × {df.shape[1]} columns")
print()
print("New columns added:")
new_cols = ['Attrition_Flag', 'AgeBand', 'SalaryBand', 'TenureBand']
for col in new_cols:
    print(f"   + {col}")
print()
print("Next step: Run SQL files in MySQL Workbench")
