import mysql.connector

print(mysql.connector.__version__)

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vineet",
    database="company_db"
)

cursor = con.cursor()
emp_id=int(input("enter the ID: "))
emp_name= input("enter the Name :")
department=input("enter the Department ")
salary=input("enter the salary :")

query="""
update employee 
set emp_name=%s,department=%s,salary=%s
where emp_id=%s
"""
values = (emp_id, emp_name, department, salary)
cursor.execute(query, values)

con.commit()
if cursor.rowcount>0:
    print("student updated successfully ")
else:
    print("student id not found ")
cursor.close()
con.close()

