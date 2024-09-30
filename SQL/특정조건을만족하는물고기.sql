SELECT COUNT(ID) FISH_COUNT, MAX(LENGTH) MAX_LENGTH, FISH_TYPE 
FROM (SELECT ID, FISH_TYPE, CASE
                             WHEN LENGTH IS NULL THEN 10
                             WHEN LENGTH <= 10 THEN 10 ELSE LENGTH 
                            END AS LENGTH
                            FROM FISH_INFO) i
GROUP BY 3
HAVING AVG(LENGTH) >= 33
ORDER BY 3