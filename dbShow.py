import mysql.connector as mc

mydb = mc.connect(host='localhost', user='root', password='123456')
mycur = mydb.cursor()
mycur.execute('SHOW DATABASES')
for i in mycur:
    print(i)