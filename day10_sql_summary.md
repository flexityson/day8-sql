# Day 10 — SQL Aggregate Functions & GROUP BY
**Author:** Iung Seangchanmony (Tyson)  
**Date:** 2026-04-03  
**Topic:** COUNT, SUM, AVG, GROUP BY, HAVING  
**Queries completed:** 15 / 15 ✅  
**Status:** Pushed to GitHub ✅

---

## The 80/20 — What Actually Matters

In real Data Science work, 80% of your SQL will use these 5 things:

```
COUNT  →  how many rows?
SUM    →  what is the total?
AVG    →  what is the average?
GROUP BY → give me results per group
HAVING   → filter those groups
```

Master these and you can answer most business questions with SQL.

---

## Aggregate Functions — One Idea, Four Tools

An aggregate function takes **many rows** and returns **one value**.

```
[5000, 6000, 4500, 7000, 4000]  →  AVG()  →  5300.0
```

| SQL | What it does | Pandas |
|---|---|---|
| `COUNT(*)` | count rows | `len(df)` |
| `SUM(col)` | total of column | `df['col'].sum()` |
| `AVG(col)` | average of column | `df['col'].mean()` |
| `MAX(col)` | highest value | `df['col'].max()` |

---

## The Queries — Clean and Simple

### COUNT — how many employees?
```sql
SELECT COUNT(*) FROM employees
```
```python
# Pandas
len(df)
```
**Output:** `(5,)`

---

### SUM — total salary bill?
```sql
SELECT SUM(salary) FROM employees
```
```python
# Pandas
df['salary'].sum()
```
**Output:** `(26500,)`

---

### AVG — average salary?
```sql
SELECT AVG(salary) FROM employees
```
```python
# Pandas
df['salary'].mean()
```
**Output:** `(5300.0,)`

---

### GROUP BY — average salary per department?
```sql
SELECT department, AVG(salary) FROM employees GROUP BY department
```
```python
# Pandas
df.groupby('department')['salary'].mean()
```
**Output:**
```
('HR', 4000.0)
('IT', 6500.0)
('Sales', 4750.0)
```

---

### HAVING — only departments with avg salary > 4500?
```sql
SELECT department, AVG(salary) 
FROM employees 
GROUP BY department 
HAVING AVG(salary) > 4500 
ORDER BY AVG(salary) DESC
```
```python
# Pandas
result = df.groupby('department')['salary'].mean()
result[result > 4500].sort_values(ascending=False)
```
**Output:**
```
('IT', 6500.0)
('Sales', 4750.0)
```

---

## The Most Important Distinction

| Keyword | Filters | Use after |
|---|---|---|
| `WHERE` | individual rows | `FROM` |
| `HAVING` | grouped results | `GROUP BY` |

**Simple rule:**
- Filtering raw rows → `WHERE`
- Filtering aggregated groups → `HAVING`

```sql
-- WHERE filters BEFORE grouping
SELECT department, AVG(salary) FROM employees
WHERE city = 'Singapore'
GROUP BY department

-- HAVING filters AFTER grouping
SELECT department, AVG(salary) FROM employees
GROUP BY department
HAVING AVG(salary) > 4500
```

---

## Updated Golden Rule — Full Keyword Order

```
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
```

---

## Self Review Questions
Test yourself without notes:

1. What does `COUNT(*)` return?
2. What is the difference between `WHERE` and `HAVING`?
3. Write a query that gets total salary per department
4. What is the Pandas equivalent of `GROUP BY`?
5. Where does `HAVING` go in the keyword order?

---

## Coming Up — Day 11
- `JOIN` — combining two tables together
- The most important SQL concept for real-world Data Science
