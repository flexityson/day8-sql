# Day 9 — SQL Filtering and Limiting
**Author:** Iung Seangchanmony (Tyson)  
**Date:** 2026-04-02  
**Topic:** WHERE with numeric conditions, AND, OR, LIMIT  
**Queries completed:** 10 / 10 ✅  
**Status:** Pushed to GitHub ✅

---

## What We Covered Today

- `WHERE` with numeric operators (`>`, `<`, `>=`, `<=`, `!=`)
- `AND` — both conditions must be true
- `OR` — at least one condition must be true
- `LIMIT` — get only top N rows
- Combining all keywords in one query

---

## The Golden Rule — SQL Keyword Order

Always write SQL keywords in this exact order:

```
SELECT → FROM → WHERE → ORDER BY → LIMIT
```

**Never changes. Memorize this.**

---

## Numeric Operators in WHERE

| Operator | Meaning | Example |
|---|---|---|
| `>` | greater than | `salary > 5000` |
| `<` | less than | `salary < 5000` |
| `>=` | greater than or equal to | `salary >= 5000` |
| `<=` | less than or equal to | `salary <= 5000` |
| `=` | equal to | `salary = 5000` |
| `!=` | not equal to | `city != 'Bangkok'` |

Same operators you already know from Python. ✅

---

## Query 6 — WHERE with numeric condition

```sql
SELECT * FROM employees WHERE salary >= 5000 ORDER BY salary DESC
```

**Output:**
```
(4, 'Diana', 7000, 'IT', 'Jakarta')
(2, 'Bob', 6000, 'IT', 'Bangkok')
(1, 'Alice', 5000, 'Sales', 'Singapore')
```

**Key detail:** Alice with exactly `5000` is included because `>=` means greater than **or equal to**. If you used `>` she would be excluded.

**Pandas equivalent:**
```python
df[df['salary'] >= 5000].sort_values('salary', ascending=False)
```

---

## Query 7 — AND (both conditions must be true)

```sql
SELECT * FROM employees WHERE department = 'IT' AND salary > 5000
```

**Output:**
```
(2, 'Bob', 6000, 'IT', 'Bangkok')
(4, 'Diana', 7000, 'IT', 'Jakarta')
```

- Both conditions must be true for a row to appear
- Bob and Diana are in IT AND have salary > 5000

**Pandas equivalent:**
```python
df[(df['department'] == 'IT') & (df['salary'] > 5000)]
```

---

## Query 8 — OR (at least one condition must be true)

```sql
SELECT * FROM employees WHERE department = 'IT' OR department = 'HR'
```

**Output:**
```
(2, 'Bob', 6000, 'IT', 'Bangkok')
(4, 'Diana', 7000, 'IT', 'Jakarta')
(5, 'Eve', 4000, 'HR', 'Singapore')
```

- At least one condition must be true for a row to appear
- Bob and Diana are in IT, Eve is in HR — all 3 qualify

**Pandas equivalent:**
```python
df[(df['department'] == 'IT') | (df['department'] == 'HR')]
```

---

## Query 9 — LIMIT (get only top N rows)

```sql
SELECT * FROM employees LIMIT 3
```

**Output:**
```
(1, 'Alice', 5000, 'Sales', 'Singapore')
(2, 'Bob', 6000, 'IT', 'Bangkok')
(3, 'Charlie', 4500, 'Sales', 'Singapore')
```

- `LIMIT` always goes at the very end of the query
- Returns only the first N rows

**Pandas equivalent:**
```python
df.head(3)
```

---

## Query 10 — Everything Combined

```sql
SELECT name, salary, city 
FROM employees 
WHERE salary > 4000 AND city != 'Bangkok' 
ORDER BY salary DESC 
LIMIT 3
```

**Output:**
```
('Diana', 7000, 'Jakarta')
('Alice', 5000, 'Singapore')
('Charlie', 4500, 'Singapore')
```

**Why Bob and Eve are excluded:**
- Bob excluded — city is Bangkok (`!=` 'Bangkok' filter)
- Eve excluded — salary is exactly 4000, not **greater than** 4000

---

## Full SQL vs Pandas Cheat Sheet

| Task | Pandas | SQL |
|---|---|---|
| Get all data | `df` | `SELECT * FROM table` |
| Get specific columns | `df[['col1', 'col2']]` | `SELECT col1, col2 FROM table` |
| Filter by text | `df[df['col'] == 'value']` | `WHERE col = 'value'` |
| Filter numeric | `df[df['col'] > 5000]` | `WHERE col > 5000` |
| Not equal | `df[df['col'] != 'value']` | `WHERE col != 'value'` |
| Both conditions | `df[(cond1) & (cond2)]` | `WHERE cond1 AND cond2` |
| Either condition | `df[(cond1) \| (cond2)]` | `WHERE cond1 OR cond2` |
| Sort descending | `sort_values(ascending=False)` | `ORDER BY col DESC` |
| Sort ascending | `sort_values(ascending=True)` | `ORDER BY col ASC` |
| Top N rows | `df.head(3)` | `LIMIT 3` |

---

## AND vs OR — Key Difference

```
AND = BOTH conditions must be true (more restrictive, fewer results)
OR  = AT LEAST ONE condition must be true (less restrictive, more results)
```

**Example:**
```sql
-- Only IT employees with salary > 5000 (must satisfy BOTH)
WHERE department = 'IT' AND salary > 5000

-- IT employees OR HR employees (satisfying EITHER is enough)
WHERE department = 'IT' OR department = 'HR'
```

---

## 10 Queries Complete — Full Summary

| # | Query | Keywords |
|---|---|---|
| 1 | Get all data | `SELECT *` |
| 2 | Get specific columns | `SELECT col1, col2` |
| 3 | Filter by text | `WHERE` |
| 4 | Sort data | `ORDER BY DESC` |
| 5 | Filter + sort | `WHERE` + `ORDER BY` |
| 6 | Numeric filter | `>=` |
| 7 | Multiple conditions | `AND` |
| 8 | Either condition | `OR` |
| 9 | Limit results | `LIMIT` |
| 10 | Everything combined | `WHERE` + `AND` + `!=` + `ORDER BY` + `LIMIT` |

---

## Self Review Questions
Test yourself without looking at notes:

1. What is the correct order of SQL keywords?
2. What is the difference between `>` and `>=`?
3. What is the difference between `AND` and `OR`?
4. Where does `LIMIT` go in a query?
5. How do you write "not equal to" in SQL?
6. Write a query that gets `name` and `salary` from employees where salary is less than 6000, ordered ascending, limited to 2 results.
7. What is the Pandas equivalent of `WHERE col > 5000`?

---

## Coming Up — Day 10
- `COUNT()` — count number of rows
- `SUM()` — add up values
- `AVG()` — calculate average
- `GROUP BY` — group data like Pandas `groupby()`
- Aggregate functions in SQL
