# Power BI DAX Measures Reference
## HR Analytics Dashboard
### Author: Rithika N | Data Analyst | Chennai

---

## How to Add DAX Measures in Power BI

1. Open Power BI Desktop
2. Go to **Home → New Measure** (or right-click your table in Fields pane)
3. Copy-paste each measure below
4. Press **Enter** to save
5. Use the measure in your visuals by dragging it to Values

---

## Page 1 — Executive Overview Measures

```dax
Total Employees =
COUNTROWS(employees)
```

```dax
Attrition Count =
COUNTROWS(FILTER(employees, employees[Attrition_Flag] = 1))
```

```dax
Attrition Rate =
DIVIDE(
    COUNTROWS(FILTER(employees, employees[Attrition_Flag] = 1)),
    COUNTROWS(employees),
    0
)
```
> Format this measure as **Percentage** in the Format pane → Display as %

```dax
Active Employees =
COUNTROWS(FILTER(employees, employees[Attrition_Flag] = 0))
```

```dax
Avg Monthly Income =
AVERAGE(employees[MonthlyIncome])
```
> Format as **Currency** with 0 decimal places

```dax
Avg Tenure Years =
AVERAGE(employees[YearsAtCompany])
```

---

## Page 2 — Attrition Deep Dive Measures

```dax
Dept Attrition Rate =
DIVIDE(
    CALCULATE(COUNTROWS(employees), employees[Attrition_Flag] = 1),
    COUNTROWS(employees),
    0
)
```

```dax
Overtime Attrition Rate =
CALCULATE(
    [Attrition Rate],
    employees[OverTime] = "Yes"
)
```

```dax
Non-Overtime Attrition Rate =
CALCULATE(
    [Attrition Rate],
    employees[OverTime] = "No"
)
```

```dax
Low Salary Attrition Rate =
CALCULATE(
    [Attrition Rate],
    employees[SalaryBand] = "Under $3K"
)
```

---

## Page 3 — Workforce Profile Measures

```dax
Overtime Employee % =
DIVIDE(
    COUNTROWS(FILTER(employees, employees[OverTime] = "Yes")),
    COUNTROWS(employees),
    0
)
```
> Format as Percentage

```dax
Male Employee % =
DIVIDE(
    COUNTROWS(FILTER(employees, employees[Gender] = "Male")),
    COUNTROWS(employees),
    0
)
```

```dax
Female Employee % =
DIVIDE(
    COUNTROWS(FILTER(employees, employees[Gender] = "Female")),
    COUNTROWS(employees),
    0
)
```

---

## Page 4 — Performance & Satisfaction Measures

```dax
Avg Job Satisfaction =
AVERAGE(employees[JobSatisfaction])
```

```dax
Avg Work Life Balance =
AVERAGE(employees[WorkLifeBalance])
```

```dax
Avg Performance Rating =
AVERAGE(employees[PerformanceRating])
```

```dax
Avg Environment Satisfaction =
AVERAGE(employees[EnvironmentSatisfaction])
```

```dax
Satisfaction Score (Leavers) =
CALCULATE(
    AVERAGE(employees[JobSatisfaction]),
    employees[Attrition_Flag] = 1
)
```

```dax
Satisfaction Score (Stayers) =
CALCULATE(
    AVERAGE(employees[JobSatisfaction]),
    employees[Attrition_Flag] = 0
)
```

---

## Recommended Slicers to Add

Add these as Slicer visuals on each page for interactivity:

| Slicer | Column | Type |
|--------|--------|------|
| Department | Department | Dropdown |
| Gender | Gender | List |
| Age Band | AgeBand | List |
| Salary Band | SalaryBand | List |
| Overtime | OverTime | List |
| Job Role | JobRole | Dropdown |

---

## Power BI Colour Theme

Use these hex colours for consistent, professional styling:

| Colour | Hex | Use |
|--------|-----|-----|
| Teal | `#0F6E56` | Primary charts, KPI positive |
| Coral/Red | `#D85A30` | Attrition bars, KPI negative |
| Amber | `#EF9F27` | Mid-range, warnings |
| Blue | `#185FA5` | Informational, secondary |
| Light Teal | `#E1F5EE` | Card backgrounds |
| Dark Gray | `#1a1a1a` | Text |

To apply: Go to **View → Themes → Customise current theme** and enter hex values.

---

## Recommended Visual Types Per Page

### Page 1 — Executive Overview
- KPI Card × 5 (Total Employees, Attrition Count, Attrition Rate, Avg Income, Avg Tenure)
- Line Chart: Attrition by TenureBand
- Donut Chart: Active vs Attrited employees
- Bar Chart: Headcount by Department

### Page 2 — Attrition Deep Dive
- Clustered Bar: Attrition Rate by Department
- Stacked Bar: Attrition by AgeBand
- Bar: Attrition by JobRole (top 5)
- Matrix Heatmap: Department × SalaryBand → Attrition Rate
- Slicer: Gender, OverTime

### Page 3 — Workforce Profile
- Histogram (Bar): Age Distribution
- Treemap: Department → JobRole headcount
- Donut: Gender split
- Bar: EducationField breakdown
- KPI Card: Overtime %

### Page 4 — Performance & Satisfaction
- Scatter Plot: JobSatisfaction (X) vs Attrition Rate (Y), size = headcount
- Matrix Heatmap: WorkLifeBalance × Department → Attrition Rate
- Clustered Bar: Avg Performance Rating — Leavers vs Stayers
- Gauge: Overall Avg Job Satisfaction (min 1, max 4, target 3)

---

*Power BI reference file — HR Analytics Dashboard | Rithika N*
