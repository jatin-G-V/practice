# Lab 5 – SQL Fundamentals

## Objective

The objective of this lab is to practice SQL fundamentals using SQLite and the Chinook sample database. The lab focuses on filtering, sorting, aggregation, grouping, joins, and date functions.

---

## Database Used

The **Chinook SQLite database** was used for this lab.

The database represents a digital music store and contains tables such as:

- Customer
- Invoice
- InvoiceLine
- Track
- Album
- Artist
- Genre
- Employee
- Playlist

The database was downloaded and accessed using the SQLite command-line interface.

---

## Tasks Performed

### 1. Customers from a Given Country

Retrieved customers belonging to a selected country using the `WHERE` clause.

Example:

```sql
-- Insight: This query lists customers from a selected country.

SELECT *
FROM Customer
WHERE Country = 'India';
```

---

### 2. Most Expensive Tracks

Retrieved the 10 tracks with the highest unit price using `ORDER BY` and `LIMIT`.

```sql
-- Insight: This query finds the 10 most expensive tracks based on unit price.

SELECT Name, UnitPrice
FROM Track
ORDER BY UnitPrice DESC
LIMIT 10;
```

---
<img width="647" height="405" alt="image" src="https://github.com/user-attachments/assets/3268b38a-dd8d-4172-8e93-3671c3547fd5" />

### 3. Total Revenue per Country

Calculated total revenue for each country by joining the `Invoice` and `Customer` tables.

```sql
-- Insight: This query calculates total revenue for each customer country.

SELECT
    c.Country,
    SUM(i.Total) AS total_revenue
FROM Invoice i
JOIN Customer c
    ON i.CustomerId = c.CustomerId
GROUP BY c.Country
ORDER BY total_revenue DESC;
```

---
<img width="786" height="607" alt="image" src="https://github.com/user-attachments/assets/357daa7e-fc9a-494b-b05c-047d9facb6aa" />

### 4. Best-Selling Tracks

Retrieved the 10 best-selling tracks based on the total quantity sold.

The `InvoiceLine` and `Track` tables were joined using `TrackId`.

```sql
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
```

---
<img width="718" height="391" alt="image" src="https://github.com/user-attachments/assets/17af82af-905a-4c7f-8906-fe9a69b953ac" />

### 5. Monthly Revenue

Calculated monthly revenue for a selected year using SQLite's `strftime()` date function.

```sql
-- Insight: This query calculates total revenue for each month of a selected year.

SELECT
    strftime('%Y-%m', InvoiceDate) AS month,
    SUM(Total) AS total_revenue
FROM Invoice
WHERE strftime('%Y', InvoiceDate) = '2009'
GROUP BY strftime('%Y-%m', InvoiceDate)
ORDER BY month;
```

---
<img width="498" height="423" alt="image" src="https://github.com/user-attachments/assets/2d39844b-880e-4596-9e84-d5b690e4153e" />


## 6. Organizing SQL Queries

All SQL queries were saved as separate `.sql` files inside the `sql/` directory.

Each query file contains a one-line comment above the SQL statement explaining the insight or purpose of the query.

<img width="1550" height="553" alt="image" src="https://github.com/user-attachments/assets/7124ffa4-3ef5-4c9e-803c-031ddca6479f" />

## SQL Concepts Covered

- `SELECT`
- `WHERE`
- `ORDER BY`
- `GROUP BY`
- `LIMIT`
- `SUM()`
- `JOIN`
- Aggregate Functions
- Column Aliases using `AS`
- SQLite `strftime()`
- Date-based grouping
- Foreign Key Relationships

---

## SQL Files


```text
lab5/
├── Chinook_Sqlite.sqlite
├── README.md
├── Code1.sql
├── Code2.sql
├── Code3.sql
├── Code4.sql
└── Code5.sql
```

Each SQL file contains a one-line insight comment above the query.

---

## Running the Queries

The SQL files can be executed directly using the SQLite command-line tool.

Example:

```bash
sqlite3 Chinook_Sqlite.sqlite < Code1.sql
```

Similarly:

```bash
sqlite3 Chinook_Sqlite.sqlite < Code2.sql
sqlite3 Chinook_Sqlite.sqlite < Code3.sql
sqlite3 Chinook_Sqlite.sqlite < Code4.sql
sqlite3 Chinook_Sqlite.sqlite < Code5.sql
```

Alternatively, after opening the database:

```bash
sqlite3 Chinook_Sqlite.sqlite
```

a query file can be executed using:

```sql
.read Code1.sql
```

---

## Learning Outcomes

After completing this lab, I learned how to:

- Work with a SQLite database from the command line.
- Inspect database tables and their schemas.
- Filter records using `WHERE`.
- Sort results using `ORDER BY`.
- Limit query results using `LIMIT`.
- Calculate totals using aggregate functions such as `SUM()`.
- Group data using `GROUP BY`.
- Join related tables using foreign keys.
- Calculate monthly values using SQLite date functions.
- Execute saved SQL files using the SQLite CLI.
