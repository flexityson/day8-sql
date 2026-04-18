import sqlite3

conn=sqlite3.connect(':memory:')
cursor=conn.cursor()

cursor.execute(
    '''CREATE TABLE sales(
        id INTEGER,
        product TEXT,
        category TEXT,
        quantity INTEGER,
        price INTEGER,
        city TEXT)
''')

cursor.executemany('INSERT INTO sales VALUES (?,?,?,?,?,?)', [
    (1, 'Laptop', 'Electronics', 2, 1200, 'Singapore'),
    (2, 'Phone', 'Electronics', 5, 800, 'Bangkok'),
    (3, 'Shirt', 'Clothing', 10, 50, 'Singapore'),
    (4, 'Shoes', 'Clothing', 3, 120, 'Jakarta'),
    (5, 'Headphones', 'Electronics', 4, 150, 'Bangkok'),
    (6, 'Pants', 'Clothing', 7, 80, 'Singapore'),
    (7, 'Tablet', 'Electronics', 1, 600, 'Jakarta'),
    (8, 'Jacket', 'Clothing', 2, 200, 'Bangkok'),
])
conn.commit()
print("Database Ready")

#Q1 "What is the total revenue per category?"
#cursor.execute("Select category, SUM(quantity*price) As total_revenue from sales group by category")
#rows=cursor.fetchall()

#for row in rows:
    #print(row)
#Q2 "Which city has the highest number of total items sold?"
#cursor.execute("Select city, sum(quantity) as total_sold from sales group by city order by total_sold desc limit 1")
#rows=cursor.fetchall()

#for row in rows:
    #print(row)

#Q3 "Show me all products that generated more revenue than the average revenue across all products."

#cursor.execute("Select product from sales where quantity*price >(select avg(quantity*price) from sales)")
#rows=cursor.fetchall()

#for row in rows:
    #print(row)

#Q4 "Label each product as 'Premium' if price is above 500, otherwise 'Budget'. Show me the count of products in each label."

#cursor.execute("select sales_category, count(*) from (select category, price, case when price>500 then 'Premium' else 'Budget' end as sales_category from sales) group by sales_category")
#rows=cursor.fetchall()

#for row in rows:
    #print(row)

#Q5 "Which category has the highest average price per item, and what is it?"
cursor.execute("select category, avg(price) from sales group by category order by avg(price) desc limit 1")
rows=cursor.fetchall()

for row in rows:
    print(row)