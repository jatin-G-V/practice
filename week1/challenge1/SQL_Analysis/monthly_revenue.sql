SELECT
    strftime('%Y-%m', InvoiceDate) AS Month,
    SUM(Total) AS Revenue
FROM Invoice
WHERE strftime('%Y', InvoiceDate) = '2025'
GROUP BY Month
ORDER BY Month;