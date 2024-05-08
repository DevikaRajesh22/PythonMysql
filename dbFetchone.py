import mysql.connector as mc

mydb = mc.connect(host='localhost', user='root', password='123456')
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS shops")
mycursor.execute("USE shops")
mycursor.execute("CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price FLOAT)")

sql = "INSERT INTO products (name, price) VALUES (%s, %s)"
val = [
    ("Product 1", 10.99),
    ("Product 2", 20.49),
    ("Product 3", 15.99),
    ("Product 4", 25.99)
]
mycursor.executemany(sql, val)
mydb.commit()

mycursor.execute("SELECT * FROM products")

print("Products:")
while True:
    row = mycursor.fetchone()  # Fetch one row at a time
    if row is None:
        break
    print(row)

mycursor.execute('DROP TABLE products')
mycursor.execute('DROP DATABASE shops')
mycursor.close()
mydb.close()
