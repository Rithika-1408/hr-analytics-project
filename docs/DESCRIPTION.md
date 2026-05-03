# Project Description
## HR Analytics Dashboard — Employee Attrition & Workforce Intelligence

---

## Problem Statement

Employee attrition is one of the most expensive and disruptive challenges faced by organisations today. According to industry research, replacing a single employee costs between 1.5x to 2x their annual salary when you account for recruitment, onboarding, training, and lost productivity.

Despite this, most HR teams in India still rely on spreadsheets and manual monthly reports to track attrition. By the time they notice a pattern, it is already too late to act.

**This project builds a data-driven HR Analytics Dashboard that answers:**
- What is the current attrition rate, and is it improving or worsening?
- Which departments, job roles, and age groups are most at risk?
- Does salary level drive attrition — are low-paid employees leaving more?
- Is there a link between job satisfaction, work-life balance, and attrition?
- What does the overall workforce profile look like?

---

## Objectives

1. Clean and prepare raw HR data using Python for reliable analysis
2. Store structured data in MySQL and write metric queries for key KPIs
3. Build a 4-page interactive Power BI dashboard with slicers, KPI cards, and drill-downs
4. Surface actionable insights that an HR team or business leader can act on

---

## Dataset

**Name:** IBM HR Analytics Employee Attrition & Performance Dataset

**Source:** Kaggle — https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

**Size:** 1,470 employee records | 35 columns

**Key columns used:**

| Column | Description |
|--------|-------------|
| Attrition | Whether the employee left (Yes/No) — target variable |
| Age | Employee age |
| Department | Sales, R&D, HR |
| JobRole | Manager, Analyst, Technician etc. |
| MonthlyIncome | Salary in USD |
| YearsAtCompany | Tenure |
| JobSatisfaction | Score 1–4 |
| WorkLifeBalance | Score 1–4 |
| PerformanceRating | Score 1–4 |
| Gender | Male / Female |
| EducationField | Background domain |
| OverTime | Yes / No |

---

## Methodology

### Phase 1 — Data Cleaning (Python)
- Load raw CSV using Pandas
- Check for missing values, duplicates, and incorrect data types
- Encode categorical columns (Attrition: Yes=1, No=0)
- Create derived columns: Age Band, Salary Band, Tenure Band
- Export cleaned data to `hr_cleaned.csv`

### Phase 2 — SQL Analysis (MySQL)
- Create `hr_analytics` database and `employees` table
- Load cleaned CSV into MySQL using LOAD DATA INFILE
- Write SQL queries for each KPI used in Power BI
- Validate metric calculations before connecting to dashboard

### Phase 3 — Dashboard (Power BI)
- Connect Power BI to MySQL using native connector
- Build data model (single table — no joins needed for this dataset)
- Write DAX measures for all calculated KPIs
- Build 4 dashboard pages with consistent theme and interactivity
- Add slicers for Department, Gender, Age Band, Job Role

---

## Dashboard Pages — Detailed

### Page 1: Executive Overview
**Purpose:** Give an HR Director a 10-second summary of workforce health.

**Visuals:**
- 5 KPI cards: Total Employees | Attrition Count | Attrition Rate % | Avg Monthly Income | Avg Tenure (Years)
- Line chart: Attrition trend by Years at Company
- Donut chart: Active vs Departed employees
- Bar chart: Headcount by Department

**DAX Measures:**
- `Attrition Rate = DIVIDE(COUNTROWS(FILTER(employees, employees[Attrition]=1)), COUNTROWS(employees))`
- `Avg Tenure = AVERAGE(employees[YearsAtCompany])`

---

### Page 2: Attrition Deep Dive
**Purpose:** Identify exactly which segment of employees is leaving the most.

**Visuals:**
- Clustered bar: Attrition count by Department
- Stacked bar: Attrition by Age Band (Under 25 / 25–35 / 35–45 / 45+)
- Bar chart: Attrition by Job Role (top 5 roles with highest attrition)
- Heatmap matrix: Attrition Rate by Department × Salary Band
- Slicer: Gender, OverTime (Yes/No)

**Key Insight to highlight:** Employees earning under $5,000/month and working overtime have significantly higher attrition — this is a salary + burnout signal.

---

### Page 3: Workforce Profile
**Purpose:** Understand who the current workforce is.

**Visuals:**
- Histogram: Age distribution across the company
- Treemap: Headcount by Department → Job Role (drill-down)
- Donut: Gender split
- Bar: Education field breakdown
- KPI: % of workforce with overtime

---

### Page 4: Performance & Satisfaction
**Purpose:** Find the link between satisfaction, performance, and attrition.

**Visuals:**
- Scatter plot: Job Satisfaction Score vs Attrition Rate (by department)
- Heatmap: Work-Life Balance Score × Attrition (shows which WLB score = highest exits)
- Bar: Avg Performance Rating — leavers vs stayers (are high performers leaving?)
- Gauge: Overall Job Satisfaction average score

**Key Insight to highlight:** Employees with WorkLifeBalance = 1 (worst) have 3x higher attrition than those rated 3 or 4.

---

## Key Findings (after analysis)

1. **Overall attrition rate is 16.1%** — above industry average of 10–13% for IT/tech firms
2. **Sales department has the highest attrition** — nearly 21% of the Sales team left
3. **Young employees (under 35) account for 60%+ of attrition** — early career dissatisfaction
4. **Low salary is the biggest driver** — employees earning under $3,000/month leave at 2.5x the rate of those above $7,000/month
5. **Overtime = red flag** — employees with overtime = Yes leave at 30.5% vs 10.4% for those without
6. **High performers leave too** — 15% of Performance Rating 4 employees still left, indicating non-monetary dissatisfaction

---

## DAX Measures Reference

```dax
-- Attrition Rate
Attrition Rate =
DIVIDE(
    COUNTROWS(FILTER(employees, employees[Attrition] = 1)),
    COUNTROWS(employees),
    0
)

-- Attrition Count
Attrition Count =
COUNTROWS(FILTER(employees, employees[Attrition] = 1))

-- Active Employees
Active Employees =
COUNTROWS(FILTER(employees, employees[Attrition] = 0))

-- Avg Monthly Income
Avg Monthly Income =
AVERAGE(employees[MonthlyIncome])

-- Avg Tenure
Avg Tenure =
AVERAGE(employees[YearsAtCompany])

-- Avg Job Satisfaction
Avg Satisfaction =
AVERAGE(employees[JobSatisfaction])

-- Overtime Attrition Rate
Overtime Attrition Rate =
CALCULATE(
    [Attrition Rate],
    employees[OverTime] = "Yes"
)
```

---

## Skills Demonstrated

| Skill | How demonstrated |
|-------|-----------------|
| Python / Pandas | Data cleaning, feature engineering, EDA |
| SQL / MySQL | Database creation, data loading, KPI queries |
| Power BI | 4-page dashboard, DAX measures, slicers, drill-through |
| Data Storytelling | Insights translated into business language |
| Data Modelling | Clean star schema understanding |
| Problem Framing | Business problem → data question → visual answer |

---

## How to Use This Project in Interviews

**Common interview question:** "Tell me about a project you've built."

**Answer structure using this project:**
1. **Problem** — HR teams struggle to identify attrition patterns until it is too late
2. **Data** — Used IBM's 1,470 employee dataset with 35 features from Kaggle
3. **Approach** — Cleaned in Python, stored in MySQL, built 4-page Power BI dashboard
4. **Insight** — Employees with overtime and salary under $3K/month leave at 3x the rate
5. **Impact** — Dashboard gives HR teams a real-time view so they can intervene early

This structure (Problem → Data → Approach → Insight → Impact) works for every data analyst interview.

---

*Project by Rithika N | Data Analyst | Chennai | rithirenu14@gmail.com*
