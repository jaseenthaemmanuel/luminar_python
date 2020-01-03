import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database = "djangoexample"
)

cursor=db.cursor()
query="""INSERT INTO EMPLOYEE(FIRSTNAME,LASTNAME,AGE,SEX,INCOME) VALUES('FATHIMA','SHEREEF',22,'F',15000)"""
try:
    cursor.execute(query)
    db.commit()
    print("data inserted successfully")
except Exception as e:
    print(e.args)

db.close()