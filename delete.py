import mysql.connector

print(mysql.connector.__version__)

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vineet",
    database="company_db"
)

cursor = con.cursor()

emp_id=int(input("enter the ID to be deleted : "))
query="delete from employee  where emp_id=%s"
cursor.execute(query,(emp_id,))

con.commit()

if cursor.rowcount>0:
    print("student Deleted successfully ")
else:
    print("student id not found ")
cursor.close()
con.close()

