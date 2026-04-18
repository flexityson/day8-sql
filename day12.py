#subqueries and case when
import sqlite3

conn= sqlite3.connect(':memory:')
cursor= conn.cursor()

cursor.execute('''
    CREATE TABLE employees(
        id INTERGER,
        name TEXT,
        salary INTERGER,
        department_id INTERGER)
    ''')

cursor.execute('''
    CREATE TABLE departments(
        id INTEGER,
        department_name TEXT,
        budget INTEGER)
    ''')

cursor.executemany('INSERT INTO employees VALUES (?,?,?,?)', [
    (1, 'Alice', 5000, 10),
    (2, 'Bob', 6000, 20),
    (3, 'Charlie', 4500, 10),
    (4, 'Diana', 7000, 20),
    (5, 'Eve', 4000, 30),
])

cursor.executemany('INSERT INTO departments VALUES (?,?,?)', [
    (10, 'Sales', 50000),
    (20, 'IT', 80000),
])
conn.commit()
print("Database Ready")
#Query 21 subquery
#cursor.execute('select * from employees where salary > (select avg(salary) from employees)')
#rows=cursor.fetchall()

#for row in rows:
    #print(row)

#Query My way of thinking
#cursor.execute('select departments.id, employees.name, departments.budget from employees inner join departments on employees.department_id=departments.id where budget > 60000')
#rows=cursor.fetchall()

#for row in rows:
    #print(row)

#Query 22 Subquery with in (using in)
#cursor.execute('select * from employees where department_id in (select id from departments where budget > 60000)')
#rows=cursor.fetchall()

#for row in rows:
    #print(row)

#Query 23 Case when 
#cursor.execute("select name, salary, case when salary >= 6000 then 'High' when salary >= 5000 then 'Mid' else 'Low' end as salary_category from employees")
#rows=cursor.fetchall()

#for row in rows:
    #print(row)

#Query 24 combine case when with group by
#cursor.execute("Select salary_category, count(*) from (select name, salary, case when salary >=6000 then 'High' when salary >=5000 then 'Mid' else 'Low' end as salary_category from employees) group by salary_category order by count (*) desc")
#rows=cursor.fetchall()

#for row in rows:
    #print(row)
#Query 25 Final Query 
#Write a query that:
#JOINs employees and departments
#Creates a salary_category column using CASE WHEN
#Only shows High and Mid employees
#Orders by salary descending
cursor.execute("select employees.name, employees.salary, departments.department_name, case when salary >=6000 then 'High' when salary>=5000 then 'Mid' else 'Low' end as salary_category from employees inner join departments on employees.department_id=departments.id where salary>=5000 order by salary desc")
rows=cursor.fetchall()

for row in rows:
    print(row)
