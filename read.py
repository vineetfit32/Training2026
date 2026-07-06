import mysql.connector

print(mysql.connector.__version__)

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vineet",
    database="company_db"
)

cursor = con.cursor()
query="select * from employee "
cursor.execute(query)
records=cursor.fetchall()

print("\n   students record ")

for row in records :
    print("id:",row[0])
    print("name:",row[1])
    print("department:",row[2])
    print("salary",row[3])
    print("_________________________________________")

cursor.close()
con.close()

