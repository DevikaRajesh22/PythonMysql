import mysql.connector as mc

mydb=mc.connect(host='localhost',user='root',password='123456')
mycur=mydb.cursor()
mycur.execute('CREATE DATABASE AUDITORIUM')
mydb.close()