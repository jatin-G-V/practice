-- Insight: This query finds the 10 best-selling tracks based on total quantity sold.

SELECT
    t.TrackId,
    t.Name,
    SUM(il.Quantity) AS sold_quantity
FROM InvoiceLine il
JOIN Track t
    ON t.TrackId = il.TrackId
GROUP BY t.TrackId, t.Name
ORDER BY sold_quantity DESC
LIMIT 10;