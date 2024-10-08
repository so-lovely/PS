SELECT d.DEPT_ID DEPT_ID, d.DEPT_NAME_EN DEPT_NAME_EN,
ROUND(AVG(SAL), 0) AVG_SAL
FROM HR_DEPARTMENT d JOIN HR_EMPLOYEES e
ON d.DEPT_ID = e.DEPT_ID
GROUP BY DEPT_ID, DEPT_NAME_EN
ORDER BY AVG_SAL DESC