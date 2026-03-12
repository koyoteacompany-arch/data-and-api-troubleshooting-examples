-- Example SQL queries

SELECT *
FROM transactions
WHERE amount > 1000;

SELECT department, SUM(amount)
FROM transactions
GROUP BY department;
