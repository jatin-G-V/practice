-- Insight: These queries identify customers from a selected country and the 10 most expensive tracks.

SELECT *
FROM Customer
WHERE Country = 'India';


SELECT Name, UnitPrice
FROM Track
ORDER BY UnitPrice DESC
LIMIT 10;