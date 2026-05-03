-- ============================================================
-- File: sql/01_create_tables.sql
-- Purpose: Create hr_analytics database and employees table
-- Author: Rithika N | Data Analyst | Chennai
-- Run this FIRST in MySQL Workbench
-- ============================================================

-- Step 1: Create the database
DROP DATABASE IF EXISTS hr_analytics;
CREATE DATABASE hr_analytics;
USE hr_analytics;

-- Step 2: Create the employees table
CREATE TABLE employees (
    Age                      INT,
    Attrition                VARCHAR(5),
    BusinessTravel           VARCHAR(30),
    DailyRate                INT,
    Department               VARCHAR(50),
    DistanceFromHome         INT,
    Education                INT,
    EducationField           VARCHAR(50),
    EnvironmentSatisfaction  INT,
    Gender                   VARCHAR(10),
    HourlyRate               INT,
    JobInvolvement           INT,
    JobLevel                 INT,
    JobRole                  VARCHAR(50),
    JobSatisfaction          INT,
    MaritalStatus            VARCHAR(20),
    MonthlyIncome            INT,
    MonthlyRate              INT,
    NumCompaniesWorked       INT,
    OverTime                 VARCHAR(5),
    PercentSalaryHike        INT,
    PerformanceRating        INT,
    RelationshipSatisfaction INT,
    StockOptionLevel         INT,
    TotalWorkingYears        INT,
    TrainingTimesLastYear    INT,
    WorkLifeBalance          INT,
    YearsAtCompany           INT,
    YearsInCurrentRole       INT,
    YearsSinceLastPromotion  INT,
    YearsWithCurrManager     INT,
    Attrition_Flag           INT,
    AgeBand                  VARCHAR(20),
    SalaryBand               VARCHAR(20),
    TenureBand               VARCHAR(20)
);

ALTER TABLE employees
ADD COLUMN EmployeeNumber INT AFTER EducationField;
select * from employees;

-- Confirm
SHOW TABLES;
SELECT 'Table created successfully' AS Status;
