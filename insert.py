import mysql.connector

print(mysql.connector.__version__)

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vineet",
    database="company_db"
)

cursor = con.cursor()

print("Add New Employee")

emp_id = int(input("Enter Employee ID: "))
emp_name = input("Enter Employee Name: ")
department = input("Enter Department: ")
salary = int(input("Enter Salary: "))

query = """
INSERT INTO Employee
VALUES (%s, %s, %s, %s)
"""

values = (emp_id, emp_name, department, salary)

cursor.execute(query, values)

con.commit()

print("Employee added successfully!")

cursor.close()
con.close()