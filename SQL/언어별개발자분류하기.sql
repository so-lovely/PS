WITH ConcatTable AS (
    SELECT d.ID, d.EMAIL, s.CATEGORY, s.NAME, d.SKILL_CODE 
    FROM SKILLCODES s 
    JOIN DEVELOPERS d 
    ON d.SKILL_CODE & s.CODE = s.CODE
)
SELECT 
    (CASE
        WHEN SUM(CASE WHEN CATEGORY = 'Front End' THEN 1 ELSE 0 END) > 0 
             AND SUM(CASE WHEN NAME = 'Python' THEN 1 ELSE 0 END) > 0 THEN 'A'
        WHEN SUM(CASE WHEN NAME = 'C#' THEN 1 ELSE 0 END) > 0 THEN 'B'
        WHEN SUM(CASE WHEN CATEGORY = 'Front End' THEN 1 ELSE 0 END) > 0 THEN 'C'
    END) AS GRADE, 
    ID, 
    EMAIL
FROM ConcatTable
GROUP BY ID, EMAIL
HAVING GRADE IS NOT NULL
ORDER BY GRADE, ID;
