SELECT COUNT(ID) AS COUNT
FROM ECOLI_DATA
WHERE RIGHT(BIN(GENOTYPE), 3) = 100 
OR 
RIGHT(BIN(GENOTYPE), 3) = 001
OR
RIGHT(BIN(GENOTYPE), 3) = 101