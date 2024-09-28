WITH Temp AS (
    SELECT h.hacker_id, h.name, COUNT(C.challenge_id) AS challenge_count_
    FROM Hackers AS h
    INNER JOIN Challenges AS C
    ON h.hacker_id = C.hacker_id
    GROUP BY h.hacker_id, h.name
)
SELECT * 
FROM Temp 
WHERE challenge_count_ IN (
    SELECT challenge_count_ 
    FROM Temp 
    GROUP BY challenge_count_ 
    HAVING COUNT(challenge_count_) = 1
) 
OR challenge_count_ = (SELECT MAX(challenge_count_) FROM Temp)
ORDER BY challenge_count_ DESC, hacker_id;
