SELECT b.CATEGORY AS CATEGORY, SUM(s.SALES) TOTAL_SALES 
FROM BOOK b JOIN BOOK_SALES s
ON b.BOOK_ID = s.BOOK_ID
WHERE s.SALES_DATE LIKE '2022-01%'
GROUP BY 1
ORDER BY 1