# Day 12 — Subqueries & CASE WHEN
**Author:** Iung Seangchanmony (Tyson)
**Date:** 2026-04-05

---

## Subqueries — A Query Inside A Query

Sometimes you don't know the exact value you want to filter by.
Instead of hardcoding a number, you let SQL calculate it for you.

This is a subquery — a query sitting inside another query.

```sql
-- Instead of this (hardcoded)
SELECT * FROM employees WHERE salary > 5300

-- Do this (dynamic)
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)
```

The inner query runs first, returns 5300.0, then the outer query uses it.
If the data changes tomorrow, the average recalculates automatically. You never touch the query.

---

## Subquery with IN

Sometimes you want to filter based on values from another table entirely.

```sql
SELECT * FROM employees
WHERE department_id IN (SELECT id FROM departments WHERE budget > 60000)
```

The inner query finds all department ids with budget over 60000.
The outer query finds employees who belong to those departments.

This is cleaner than a JOIN when you only need data from one table in your result.

---

## JOIN vs Subquery — Which One to Use?

This comes up a lot so remember it:

Use JOIN when you need columns from both tables in your output.
Use subquery with IN when you're only filtering based on another table but don't need its columns.

Both can give the same result — pick whichever is easier to read.

---

## CASE WHEN — If/Else Logic in SQL

SQL can create new columns on the fly, just like feature engineering in Pandas.
CASE WHEN is how you add if/else logic to do it.

```sql
SELECT name, salary,
    CASE
        WHEN salary >= 6000 THEN 'High'
        WHEN salary >= 5000 THEN 'Mid'
        ELSE 'Low'
    END AS salary_category
FROM employees
```

Output:
```
('Alice', 5000, 'Mid')
('Bob', 6000, 'High')
('Charlie', 4500, 'Low')
('Diana', 7000, 'High')
('Eve', 4000, 'Low')
```

AS salary_category gives the new column a name.
SQL checks conditions top to bottom and stops at the first match — just like if/elif/else in Python.

---

## CASE WHEN + GROUP BY — Counting Categories

You can wrap a CASE WHEN inside a subquery and then GROUP BY the result.

```sql
SELECT salary_category, COUNT(*)
FROM (
    SELECT name, salary,
        CASE
            WHEN salary >= 6000 THEN 'High'
            WHEN salary >= 5000 THEN 'Mid'
            ELSE 'Low'
        END AS salary_category
    FROM employees
)
GROUP BY salary_category
ORDER BY COUNT(*) DESC
```

Output:
```
('Low', 2)
('High', 2)
('Mid', 1)
```

---

## The Important Gotcha — WHERE Can't See CASE WHEN

You might think you can filter like this:

```sql
WHERE salary_category = 'High'  -- This will fail
```

It fails because WHERE runs before SELECT — so salary_category doesn't exist yet.

The simple fix is to filter by the raw value instead:

```sql
WHERE salary >= 5000  -- This works
```

Always prefer the simple approach.

---

## Everything Combined — Query 25

JOIN + CASE WHEN + WHERE + ORDER BY in one query.

```sql
SELECT employees.name, employees.salary, departments.department_name,
    CASE
        WHEN salary >= 6000 THEN 'High'
        WHEN salary >= 5000 THEN 'Mid'
        ELSE 'Low'
    END AS salary_category
FROM employees
INNER JOIN departments ON employees.department_id = departments.id
WHERE salary >= 5000
ORDER BY salary DESC
```

Output:
```
('Diana', 7000, 'IT', 'High')
('Bob', 6000, 'IT', 'High')
('Alice', 5000, 'Sales', 'Mid')
```

---

## Pandas vs SQL

| Task | Pandas | SQL |
|---|---|---|
| Filter by calculated value | `df[df['sal'] > df['sal'].mean()]` | `WHERE salary > (SELECT AVG(salary) FROM ...)` |
| Filter using another table | `df[df['id'].isin(other_df['id'])]` | `WHERE id IN (SELECT id FROM ...)` |
| Create category column | `df['cat'] = np.where(...)` | `CASE WHEN ... THEN ... END AS cat` |

---

## Review Questions

Answer these before Day 13 without looking at your notes.

1. What is a subquery and when would you use one?
2. What is the difference between using a subquery with IN vs using a JOIN?
3. Write a CASE WHEN that labels salary above 7000 as 'Top', above 5000 as 'Mid', else 'Entry'
4. Why can't you use WHERE to filter a CASE WHEN column directly?
5. What is the fix when you want to filter by a CASE WHEN result?
6. Write a query that finds all employees earning above the average salary using a subquery

---

## Week 2 SQL Progress

| Day | Topic | Status |
|---|---|---|
| Day 8 | SELECT, WHERE, ORDER BY | ✅ |
| Day 9 | Numeric filters, AND, OR, LIMIT | ✅ |
| Day 10 | COUNT, SUM, AVG, GROUP BY, HAVING | ✅ |
| Day 11 | INNER JOIN, LEFT JOIN, IS NULL | ✅ |
| Day 12 | Subqueries, CASE WHEN | ✅ |

25 queries written and pushed to GitHub.
