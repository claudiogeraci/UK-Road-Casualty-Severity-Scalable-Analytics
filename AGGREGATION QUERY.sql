USE BigData4;
GO

SELECT 
    casualty_type,
    SUM(CASE WHEN casualty_severity = 'Fatal' THEN 1 ELSE 0 END) AS Fatal_Count,
    SUM(CASE WHEN casualty_severity = 'Serious' THEN 1 ELSE 0 END) AS Serious_Count,
    SUM(CASE WHEN casualty_severity = 'Slight' THEN 1 ELSE 0 END) AS Slight_Count,
    COUNT(*) AS Total_Casualties
FROM CASUALTY
WHERE casualty_type IS NOT NULL
GROUP BY casualty_type
ORDER BY Total_Casualties DESC;
GO