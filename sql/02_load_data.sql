-- ============================================================
-- File: sql/02_load_data.sql
-- Purpose: Load cleaned CSV into MySQL employees table
-- Author: Rithika N | Data Analyst | Chennai
-- Run this SECOND in MySQL Workbench
-- ============================================================

USE hr_analytics;

-- ⚠️ IMPORTANT: Update the file path below to match where
-- your hr_cleaned.csv file is saved on your computer.
-- Use forward slashes even on Windows.
-- Example: 'F:/Rithika/Projects/hr_analytics/data/processed/hr_cleaned.csv'

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/hr_cleaned.csv'
INTO TABLE employees
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    Age, Attrition, BusinessTravel, DailyRate, Department,
    DistanceFromHome, Education, EducationField,EmployeeNumber, EnvironmentSatisfaction,
    Gender, HourlyRate, JobInvolvement, JobLevel, JobRole,
    JobSatisfaction, MaritalStatus, MonthlyIncome, MonthlyRate,
    NumCompaniesWorked, OverTime, PercentSalaryHike, PerformanceRating,
    RelationshipSatisfaction, StockOptionLevel, TotalWorkingYears,
    TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany,
    YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager,
    Attrition_Flag, AgeBand, SalaryBand, TenureBand
);

SHOW VARIABLES LIKE "secure_file_priv";
-- Verify load
SELECT COUNT(*) AS Total_Rows_Loaded FROM employees;
SELECT * FROM employees LIMIT 5;
