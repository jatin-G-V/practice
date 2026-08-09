-- Insight: This query calculates total revenue for each month of a selected year.

SELECT
    strftime('%Y-%m', InvoiceDate) AS month,
    SUM(Total) AS total_revenue
FROM Invoice
WHERE strftime('%Y', InvoiceDate) = '2021'
GROUP BY strftime('%Y-%m', InvoiceDate)
ORDER BY month;