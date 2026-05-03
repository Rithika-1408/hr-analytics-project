-- ============================================================
-- File: sql/03_metric_queries.sql
-- Purpose: All KPI queries used in the Power BI dashboard
-- Author: Rithika N | Data Analyst | Chennai
-- Run this THIRD — verify all numbers before connecting Power BI
-- ============================================================

USE hr_analytics;

-- ============================================================
-- PAGE 1: EXECUTIVE OVERVIEW KPIs
-- ============================================================

-- 1. Total Employees
SELECT COUNT(*) AS Total_Employees
FROM employees;

-- 2. Total Attrition Count
SELECT COUNT(*) AS Attrition_Count
FROM employees
WHERE Attrition = 'Yes';

-- 3. Overall Attrition Rate
SELECT
    ROUND(SUM(Attrition_Flag) / COUNT(*) * 100, 1) AS Attrition_Rate_Pct
FROM employees;

-- 4. Average Monthly Income
SELECT
    ROUND(AVG(MonthlyIncome), 0) AS Avg_Monthly_Income
FROM employees;

-- 5. Average Tenure (Years at Company)
SELECT
    ROUND(AVG(YearsAtCompany), 1) AS Avg_Tenure_Years
FROM employees;

-- 6. Headcount by Department
SELECT
    Department,
    COUNT(*) AS Headcount,
    SUM(Attrition_Flag) AS Attrition_Count,
    ROUND(SUM(Attrition_Flag) / COUNT(*) * 100, 1) AS Attrition_Rate_Pct
FROM employees
GROUP BY Department
ORDER BY Attrition_Rate_Pct DESC;

-- 7. Attrition trend by tenure band (for line chart)
SELECT
    TenureBand,
    COUNT(*) AS Total,
    SUM(Attrition_Flag) AS Attritions,
    ROUND(SUM(Attrition_Flag) / COUNT(*) * 100, 1) AS Attrition_Rate_Pct
FROM employees
GROUP BY TenureBand
ORDER BY FIELD(TenureBand, '0-2 Years', '3-5 Years', '6-10 Years', '10+ Years');


-- ============================================================
-- PAGE 2: ATTRITION DEEP DIVE
-- ============================================================

-- 8. Attrition by Age Band
SELECT
    AgeBand,
    COUNT(*) AS Total,
    SUM(Attrition_Flag) AS Attritions,
    ROUND(SUM(Attrition_Flag) / COUNT(*) * 100, 1) AS Attrition_Rate_Pct
FROM employees
GROUP BY AgeBand
ORDER BY FIELD(AgeBand, 'Under 25', '25-34', '35-44', '45+');

-- 9. Attrition by Job Role (top 5 highest)
SELECT
    JobRole,
    COUNT(*) AS Total,
    SUM(Attrition_Flag) AS Attritions,
    ROUND(SUM(Attrition_Flag) / COUNT(*) * 100, 1) AS Attrition_Rate_Pct
FROM employees
GROUP BY JobRole
ORDER BY Attrition_Rate_Pct DESC
LIMIT 5;

-- 10. Attrition by Salary Band
SELECT
    SalaryBand,
    COUNT(*) AS Total,
    SUM(Attrition_Flag) AS Attritions,
    ROUND(SUM(Attrition_Flag) / COUNT(*) * 100, 1) AS Attrition_Rate_Pct
FROM employees
GROUP BY SalaryBand
ORDER BY FIELD(SalaryBand, 'Under $3K', '$3K-$5K', '$5K-$8K', 'Above $8K');

-- 11. Attrition by Gender
SELECT
    Gender,
    COUNT(*) AS Total,
    SUM(Attrition_Flag) AS Attritions,
    ROUND(SUM(Attrition_Flag) / COUNT(*) * 100, 1) AS Attrition_Rate_Pct
FROM employees
GROUP BY Gender;

-- 12. Overtime vs Attrition (key insight)
SELECT
    OverTime,
    COUNT(*) AS Total,
    SUM(Attrition_Flag) AS Attritions,
    ROUND(SUM(Attrition_Flag) / COUNT(*) * 100, 1) AS Attrition_Rate_Pct
FROM employees
GROUP BY OverTime;

-- 13. Attrition heatmap — Department x Salary Band
SELECT
    Department,
    SalaryBand,
    COUNT(*) AS Total,
    SUM(Attrition_Flag) AS Attritions,
    ROUND(SUM(Attrition_Flag) / COUNT(*) * 100, 1) AS Attrition_Rate_Pct
FROM employees
GROUP BY Department, SalaryBand
ORDER BY Department, FIELD(SalaryBand, 'Under $3K', '$3K-$5K', '$5K-$8K', 'Above $8K');


-- ============================================================
-- PAGE 3: WORKFORCE PROFILE
-- ============================================================

-- 14. Age distribution (for histogram)
SELECT
    Age,
    COUNT(*) AS Employee_Count
FROM employees
GROUP BY Age
ORDER BY Age;

-- 15. Education field breakdown
SELECT
    EducationField,
    COUNT(*) AS Headcount,
    ROUND(COUNT(*) / (SELECT COUNT(*) FROM employees) * 100, 1) AS Pct
FROM employees
GROUP BY EducationField
ORDER BY Headcount DESC;

-- 16. Gender ratio
SELECT
    Gender,
    COUNT(*) AS Count,
    ROUND(COUNT(*) / (SELECT COUNT(*) FROM employees) * 100, 1) AS Pct
FROM employees
GROUP BY Gender;

-- 17. Overtime % of workforce
SELECT
    ROUND(SUM(CASE WHEN OverTime = 'Yes' THEN 1 ELSE 0 END) / COUNT(*) * 100, 1) AS Overtime_Pct
FROM employees;

-- 18. Department x Job Role headcount (for treemap drill-down)
SELECT
    Department,
    JobRole,
    COUNT(*) AS Headcount
FROM employees
GROUP BY Department, JobRole
ORDER BY Department, Headcount DESC;


-- ============================================================
-- PAGE 4: PERFORMANCE & SATISFACTION
-- ============================================================

-- 19. Job Satisfaction vs Attrition Rate
SELECT
    JobSatisfaction,
    COUNT(*) AS Total,
    SUM(Attrition_Flag) AS Attritions,
    ROUND(SUM(Attrition_Flag) / COUNT(*) * 100, 1) AS Attrition_Rate_Pct
FROM employees
GROUP BY JobSatisfaction
ORDER BY JobSatisfaction;

-- 20. Work-Life Balance vs Attrition (key insight)
SELECT
    WorkLifeBalance,
    COUNT(*) AS Total,
    SUM(Attrition_Flag) AS Attritions,
    ROUND(SUM(Attrition_Flag) / COUNT(*) * 100, 1) AS Attrition_Rate_Pct
FROM employees
GROUP BY WorkLifeBalance
ORDER BY WorkLifeBalance;

-- 21. Performance Rating — leavers vs stayers
SELECT
    Attrition,
    ROUND(AVG(PerformanceRating), 2) AS Avg_Performance_Rating,
    ROUND(AVG(JobSatisfaction), 2) AS Avg_Job_Satisfaction,
    ROUND(AVG(WorkLifeBalance), 2) AS Avg_WLB_Score,
    COUNT(*) AS Count
FROM employees
GROUP BY Attrition;

-- 22. Job Satisfaction heatmap — Dept x Score
SELECT
    Department,
    JobSatisfaction,
    ROUND(SUM(Attrition_Flag) / COUNT(*) * 100, 1) AS Attrition_Rate_Pct,
    COUNT(*) AS Total
FROM employees
GROUP BY Department, JobSatisfaction
ORDER BY Department, JobSatisfaction;

-- 23. Average satisfaction score overall
SELECT
    ROUND(AVG(JobSatisfaction), 2) AS Avg_Job_Satisfaction,
    ROUND(AVG(WorkLifeBalance), 2) AS Avg_Work_Life_Balance,
    ROUND(AVG(EnvironmentSatisfaction), 2) AS Avg_Env_Satisfaction
FROM employees;

-- ============================================================
-- VALIDATION CHECK — Run this last to confirm all data correct
-- ============================================================
SELECT
    COUNT(*) AS Total_Records,
    SUM(Attrition_Flag) AS Total_Attrition,
    ROUND(SUM(Attrition_Flag)/COUNT(*)*100, 1) AS Overall_Attrition_Rate,
    COUNT(DISTINCT Department) AS Departments,
    COUNT(DISTINCT JobRole) AS Job_Roles,
    ROUND(AVG(MonthlyIncome), 0) AS Avg_Monthly_Income,
    ROUND(AVG(Age), 1) AS Avg_Age
FROM employees;
