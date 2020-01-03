import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123"

)

cursor=db.cursor()
cursor.execute("SELECT VERSION()")

data=cursor.fetchone()
print("database version: 0", data)
db.close()