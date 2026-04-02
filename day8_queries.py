import sqlite3

conn = sqlite3.connect(':memory:')
cursor =conn.cursor()

cursor.execute('''
    CREATE TABLE employees(
        id INTEGER,
        name TEXT,
        salary INTEGER,
        department TEXT,
        city TEXT
               )''')

cursor.executemany('INSERT INTO employees values (?,?,?,?,?)', [
   (1, 'Alice', 5000, 'Sales', 'Singapore'),
    (2, 'Bob', 6000, 'IT', 'Bangkok'),
    (3, 'Charlie', 4500, 'Sales', 'Singapore'),
    (4, 'Diana', 7000, 'IT', 'Jakarta'),
    (5, 'Eve', 4000, 'HR', 'Singapore'),
])

conn.commit()
print("Database Ready")

cursor.execute("select name, salary, city from employees where salary>4000 and city != 'Bangkok' order by salary desc limit 3")
rows=cursor.fetchall()

for row in rows:
    print(row)

