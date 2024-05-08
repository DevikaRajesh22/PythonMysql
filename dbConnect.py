import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
)

if mydb.is_connected()==True:
    print('connected')
else:
    print('error')
mydb.close()