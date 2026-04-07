import sqlite3

conn=sqlite3.connect(':memory:')
cursor=conn.cursor()

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

#query 16 Inner join
#cursor.execute('Select employees.name, employees.salary, departments.department_name from employees Inner join departments on employees.department_id=departments.id')
#rows=cursor.fetchall()

#for row in rows:
   # print(row)

#query 17 Left join
#cursor.execute('Select employees.name, employees.salary, departments.department_name from employees left join departments on employees.department_id=departments.id')
#rows=cursor.fetchall()

#for row in rows:
   #print(row)

#query 18 combine join with aggregate function
#cursor.execute('select departments.department_name, avg(salary) from employees inner join departments on employees.department_id=departments.id group by department_name order by avg(salary) desc')
#rows=cursor.fetchall()

#for row in rows:
    #print(row)

#challenge
#cursor.execute('select employees.name, employees.salary, departments.department_name from employees left join departments on employees.department_id=departments.id where departments.department_name is null')
#rows=cursor.fetchall()

#for row in rows:
    #print(row)

#Query 20 challenge
cursor.execute('select departments.department_name, count(*), AVG(salary) from employees left join departments on employees.department_id=departments.id group by departments.department_name having count(*)>1 order by count(*) desc')
rows=cursor.fetchall()

for row in rows:
    print(row)