import sqlite3

#define connection
connection = sqlite3.connect('products.db')

cursor = connection.cursor()

#Create product table

command1 = """CREATE TABLE IF NOT EXISTS
products(name TEXT PRIMARY KEY, ingredients TEXT)"""

cursor.execute(command1)


# add to products table
cursor.execute("INSERT INTO products VALUES ('clorox', 'bleach')")

cursor.execute("INSERT INTO products VALUES ('windex', 'ammonia')")

cursor.execute("SELECT * FROM products")

results = cursor.fetchall()
print(results)
