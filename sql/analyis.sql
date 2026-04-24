use churn_db;

-- =====================================
-- CUSTOMER CHURN ANALYSIS (SQL SERVER)
-- Table: dbo.cleaned_churn
-- =====================================

-- 1. Total Customers
SELECT COUNT(*) AS total_customers
FROM dbo.cleaned_churn;


-- 2. Churn Rate (%)
SELECT ROUND(AVG(churn) * 100, 2) AS churn_rate
FROM dbo.cleaned_churn;


-- 3. Retention Rate (%)
SELECT ROUND((1 - AVG(churn)) * 100, 2) AS retention_rate
FROM dbo.cleaned_churn;


-- 4. Churn by Customer Category
SELECT custcat,
       COUNT(*) AS total_customers,
       SUM(churn) AS churned_customers,
       ROUND(AVG(churn) * 100, 2) AS churn_rate
FROM dbo.cleaned_churn
GROUP BY custcat
ORDER BY churn_rate DESC;


-- 5. Churn by Internet Usage
SELECT internet,
       COUNT(*) AS total_customers,
       ROUND(AVG(churn) * 100, 2) AS churn_rate
FROM dbo.cleaned_churn
GROUP BY internet;


-- 6. Churn by Wireless Usage
SELECT wireless,
       COUNT(*) AS total_customers,
       ROUND(AVG(churn) * 100, 2) AS churn_rate
FROM dbo.cleaned_churn
GROUP BY wireless;


-- 7. Churn by Tenure Group
SELECT 
    CASE 
        WHEN tenure < 12 THEN '0-1 Year'
        WHEN tenure < 24 THEN '1-2 Years'
        ELSE '2+ Years'
    END AS tenure_group,
    COUNT(*) AS total_customers,
    ROUND(AVG(churn) * 100, 2) AS churn_rate
FROM dbo.cleaned_churn
GROUP BY 
    CASE 
        WHEN tenure < 12 THEN '0-1 Year'
        WHEN tenure < 24 THEN '1-2 Years'
        ELSE '2+ Years'
    END
ORDER BY churn_rate DESC;


-- 8. Income Segmentation
SELECT 
    CASE 
        WHEN income < 30 THEN 'Low Income'
        WHEN income < 60 THEN 'Medium Income'
        ELSE 'High Income'
    END AS income_group,
    COUNT(*) AS total_customers,
    ROUND(AVG(churn) * 100, 2) AS churn_rate
FROM dbo.cleaned_churn
GROUP BY 
    CASE 
        WHEN income < 30 THEN 'Low Income'
        WHEN income < 60 THEN 'Medium Income'
        ELSE 'High Income'
    END
ORDER BY churn_rate DESC;


-- 9. High-Risk Customers (Low Tenure + Churn)
SELECT *
FROM dbo.cleaned_churn
WHERE tenure < 12 AND churn = 1;


-- 10. Average Income by Churn
SELECT churn,
       ROUND(AVG(income), 2) AS avg_income
FROM dbo.cleaned_churn
GROUP BY churn;


-- 11. Average Tenure by Churn
SELECT churn,
       ROUND(AVG(tenure), 2) AS avg_tenure
FROM dbo.cleaned_churn
GROUP BY churn;


-- 12. Multi-Factor Segmentation (Advanced)
SELECT custcat, internet, wireless,
       COUNT(*) AS total_customers,
       ROUND(AVG(churn) * 100, 2) AS churn_rate
FROM dbo.cleaned_churn
GROUP BY custcat, internet, wireless
ORDER BY churn_rate DESC;