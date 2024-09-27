SELECT MAX(earnings) AS max_earnings, 
       COUNT(employee_id) AS num_employees_with_max_earnings
FROM 
    (SELECT employee_id, months * salary AS earnings 
     FROM Employee) AS EmployeeEarnings
WHERE earnings = (SELECT MAX(months * salary) FROM Employee);
