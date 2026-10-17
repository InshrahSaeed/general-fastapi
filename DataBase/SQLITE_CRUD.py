#  SQLite CRUD with products (insert / read / update / delete / primary key)
import sqlite3

connection = sqlite3.connect("products_crud.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS product")          # start clean each run
cursor.execute("""
    CREATE TABLE product (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        stock INTEGER
    )
""")

# 1. INSERT - values go in column order; TEXT values need quotes
cursor.execute("""
    INSERT INTO product
    VALUES (1001, 'Wireless Mouse', 18.99, 42)
""")
cursor.execute("""
    INSERT INTO product
    VALUES (1002, 'Mechanical Keyboard', 64.99, 18)
""")
cursor.execute("""
    INSERT INTO product
    VALUES (1007, 'External SSD', 89.99, 10)
""")
# Without commit() the change is NOT saved
connection.commit()

# 2. SELECT - execute, then FETCH
cursor.execute("SELECT * FROM product")
print(cursor.fetchall())        # every row     -> list of tuples

cursor.execute("SELECT * FROM product")
print(cursor.fetchmany(2))      # first 2 rows

cursor.execute("SELECT * FROM product")
print(cursor.fetchone())        # one row (a tuple) or None

# WHERE filters; pick only the columns you need
cursor.execute("SELECT id, price FROM product WHERE name = 'USB-C Hub' OR id = 1002")
print(cursor.fetchall())

# 3. UPDATE - ALWAYS use WHERE, otherwise EVERY row changes
cursor.execute("""
    UPDATE product
    SET stock = 8
    WHERE id = 1007
""")
#UPDATE data in the table with values are provided by the clients
# name = input("Enter product name: ")
# price = float(input("Enter product price: "))
# #cursor.execute(f'''UPDATE products SET name='{name}', price={price} WHERE id=202''')   instead of f string we can use parameterized query to prevent SQL injection attacks by using placeholders and passing the values as a tuple
# cursor.execute('''UPDATE products SET name=?, price=? ''', (name, price))


connection.commit()

# 4. DELETE - ALWAYS use WHERE, otherwise the whole table is emptied
cursor.execute("""
    DELETE FROM product
    WHERE id = 1002
""")
connection.commit()

# 5. PRIMARY KEY blocks duplicate ids
try:
    cursor.execute("INSERT INTO product VALUES (1001, 'Duplicate', 1.0, 1)")
except sqlite3.IntegrityError as error:
    print("Blocked:", error)          # UNIQUE constraint failed: product.id

cursor.execute("SELECT * FROM product")
print(cursor.fetchall())

cursor.execute("DROP TABLE product")
connection.close()