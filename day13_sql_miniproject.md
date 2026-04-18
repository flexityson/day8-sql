# Day 13 — SQL Mini Project
**Author:** Iung Seangchanmony (Tyson)
**Date:** 2026-04-06

---

## What Today Was About

No new syntax today. Today was about thinking like a Data Analyst.

You were given a real business scenario and had to figure out which SQL tools to use to answer each question. That's the actual job.

The 80/20 of SQL is not memorizing syntax — it's knowing which tool to reach for when a business question lands in front of you.

---

## The 5 Business Questions and What They Taught You

### Question 1 — Total revenue per category
> "What is the total revenue per category?"

Revenue didn't exist in the table. You had to create it with math inside SQL.

```sql
SELECT category, SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY category
```

The lesson: SQL can do math inside SELECT just like Pandas. You don't need a separate column — calculate it on the fly.

---

### Question 2 — City with most items sold
> "Which city has the highest number of total items sold?"

```sql
SELECT city, SUM(quantity) AS total_sold
FROM sales
GROUP BY city
ORDER BY total_sold DESC
LIMIT 1
```

The lesson: When you GROUP BY, always use an aggregate function on the other columns. You can't use a raw column that hasn't been aggregated.

---

### Question 3 — Products above average revenue
> "Show me products that generated more revenue than the average."

```sql
SELECT product FROM sales
WHERE quantity * price > (SELECT AVG(quantity * price) FROM sales)
```

The lesson: When you don't know the exact number to filter by, use a subquery to calculate it dynamically. The inner query runs first, returns one value, then the outer query uses it.

---

### Question 4 — Premium vs Budget products
> "Label each product and count how many are in each label."

```sql
SELECT sales_category, COUNT(*)
FROM (
    SELECT price,
        CASE
            WHEN price > 500 THEN 'Premium'
            ELSE 'Budget'
        END AS sales_category
    FROM sales
)
GROUP BY sales_category
```

The lesson: CASE WHEN creates a new column on the fly. To GROUP BY that new column you wrap it in a subquery — because WHERE and GROUP BY run before SELECT finishes.

---

### Question 5 — Highest average price category
> "Which category has the highest average price?"

```sql
SELECT category, AVG(price)
FROM sales
GROUP BY category
ORDER BY AVG(price) DESC
LIMIT 1
```

The lesson: Always GROUP BY before ORDER BY and LIMIT when working with aggregate functions. Without GROUP BY you get one number for the whole table, not per group.

---

## The One Rule That Saved You Today

When you're stuck on a SQL question, break it into two questions:

1. What do I want to see? → that goes in SELECT
2. How do I want to filter or group it? → that goes in WHERE, GROUP BY, HAVING

Every business question can be broken down this way.

---

## Common Mistake to Remember

```sql
-- WRONG — missing GROUP BY
SELECT city, SUM(quantity)
FROM sales
ORDER BY SUM(quantity) DESC
LIMIT 1

-- CORRECT — always GROUP BY when using aggregate functions
SELECT city, SUM(quantity)
FROM sales
GROUP BY city
ORDER BY SUM(quantity) DESC
LIMIT 1
```

If you use SUM, COUNT, AVG, MAX — you almost always need GROUP BY with it.

---

## Week 2 SQL Progress

| Day | Topic | Status |
|---|---|---|
| Day 8 | SELECT, WHERE, ORDER BY | ✅ |
| Day 9 | Numeric filters, AND, OR, LIMIT | ✅ |
| Day 10 | COUNT, SUM, AVG, GROUP BY, HAVING | ✅ |
| Day 11 | INNER JOIN, LEFT JOIN, IS NULL | ✅ |
| Day 12 | Subqueries, CASE WHEN | ✅ |
| Day 13 | SQL Mini Project — 5 business questions | ✅ |

---

## What Comes Next — Week 3: Machine Learning

Next week you move into Scikit-learn. Here is what's coming:

- Day 15: What is machine learning — supervised vs unsupervised
- Day 16: Your first ML model — Linear Regression
- Day 17: Classification with Logistic Regression
- Day 18: Model evaluation — accuracy, precision, recall
- Day 19: Decision Trees and Random Forests
- Day 20: ML mini project — end to end pipeline

Everything you learned in Pandas, data cleaning, and feature engineering feeds directly into this. Week 3 is where it all comes together.

---

## Review Questions

Answer these before Week 3 starts without looking at notes.

1. What is the difference between WHERE and HAVING?
2. When do you need GROUP BY?
3. What is a subquery and when do you use one?
4. Why can't you GROUP BY a CASE WHEN column directly without a subquery?
5. Write a query that finds the product with the highest total revenue
