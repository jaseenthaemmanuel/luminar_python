import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database = "djangoexample"
)

cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql="""CREATE TABLE EMPLOYEE(
        FIRSTNAME VARCHAR(20),
        LASTNAME VARCHAR(20),
        AGE INT,
        SEX VARCHAR(10),
        INCOME INT)"""
cursor.execute(sql)
db.close()