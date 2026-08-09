-- Insight: This query calculates total revenue for each customer country by joining invoices with customers.

SELECT
    c.Country,
    SUM(i.Total) AS total_revenue
FROM Invoice i
JOIN Customer c
    ON i.CustomerId = c.CustomerId
GROUP BY c.Country
ORDER BY total_revenue DESC;