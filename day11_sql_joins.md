# Day 11 — SQL JOINs
**Author:** Iung Seangchanmony (Tyson)
**Date:** 2026-04-04

---

## The Big Idea

In real companies, data is never all in one table.
You'll have an employees table, a departments table, an orders table — all separate.

JOIN is how you stitch them together.

---

## The Two JOINs You Actually Need

### INNER JOIN — only show me rows that match in both tables

```sql
SELECT employees.name, employees.salary, departments.department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id
```

Think of it as a strict filter — if a row doesn't have a match in the other table, it gets cut out completely.

In our data, Eve has department_id = 30 but there's no department 30. So Eve disappears.

Output:
```
('Alice', 5000, 'Sales')
('Bob', 6000, 'IT')
('Charlie', 4500, 'Sales')
('Diana', 7000, 'IT')
-- Eve is gone
```

---

### LEFT JOIN — show me everything from the left table, match what you can

```sql
SELECT employees.name, employees.salary, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id
```

Think of it as keeping everyone — if there's no match, just put None there.

Output:
```
('Alice', 5000, 'Sales')
('Bob', 6000, 'IT')
('Charlie', 4500, 'Sales')
('Diana', 7000, 'IT')
('Eve', 4000, None)   -- Eve stays, department is None
```

---

## When to Use Which

Use INNER JOIN when you only want clean, complete data — no gaps.

Use LEFT JOIN when you want to keep everything and find what's missing.

---

## Finding Missing Data — LEFT JOIN + IS NULL

This is a powerful real-world pattern. It finds rows with no match.

```sql
SELECT employees.name, employees.salary, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id
WHERE departments.department_name IS NULL
```

Output:
```
('Eve', 4000, None)
```

In real work you'd use this to find:
- Customers with no orders
- Products with no sales
- Employees with no department

Important: In SQL you never write `WHERE col = NULL`. Always use `IS NULL`.

---

## JOIN + GROUP BY — The Power Combo

This is where SQL gets really useful for Data Science.

```sql
SELECT departments.department_name, COUNT(*), AVG(salary)
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id
GROUP BY departments.department_name
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC
```

Output:
```
('Sales', 2, 4750.0)
('IT', 2, 6500.0)
```

You joined two tables, counted employees per department, calculated average salary, filtered out small departments, and sorted — all in one query.

---

## The JOIN Syntax Pattern

Always follows this structure:

```sql
SELECT columns you want
FROM left table
JOIN right table ON left.common_column = right.common_column
```

The ON part is the glue — it tells SQL which columns connect the two tables.

---

## Pandas vs SQL

| Task | Pandas | SQL |
|---|---|---|
| Combine tables | `pd.merge(df1, df2, on='col')` | `INNER JOIN ... ON ...` |
| Keep all left rows | `pd.merge(df1, df2, how='left')` | `LEFT JOIN ... ON ...` |
| Find unmatched | filter where col is NaN | `WHERE col IS NULL` |

---

## The One Rule to Remember

```
INNER JOIN = matched rows only (strict)
LEFT JOIN  = all left rows + matches (generous)
```

If you remember nothing else from today, remember that.

---

## Self Review Questions

1. What is the difference between INNER JOIN and LEFT JOIN?
2. Why did Eve disappear in the INNER JOIN result?
3. How do you filter for NULL values in SQL?
4. Write a query that joins employees and departments and returns average salary per department
5. When would you use LEFT JOIN over INNER JOIN in real work?

---

## Coming Up — Day 12
- Subqueries — queries inside queries
- CASE WHEN — if/else logic in SQL
- Real world SQL mini project
