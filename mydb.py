import mysql.connector

mydb=mysql.connector.connect(
    user='root',
    host='localhost',
    passwd='#@llHer0esAreDead!',
    port='3306'
)

cursor=mydb.cursor()
cursor.execute("Create database Mydb")
print("Done!")