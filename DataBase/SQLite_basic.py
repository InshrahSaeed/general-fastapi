# 1st we generate CONNECTION then create cursor for writing/reading in database then run Query FOR reading , updating, deleting and inserting data in database then COMMIT to save changes then CLOSE the connection and cursor after work is done.
import sqlite3

#connect to the database(ceate database if it doesn't exist)
#step1:Connection banao (database se connect)
connection = sqlite3.connect('database.db')

#create a cursor object to execute SQL commands
# step2:Cursor banao (queries chalane ke liye)
cursor=connection.cursor()

#create a table in the database
#step3:# 3. SQL query execute karo (create / insert / select / update / delete)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL
    )
''')
#Real is used for decimal values

#            CRUD OPERATIONS IN SQLITE_CRUB FILE
#STEP4:commit() karo (changes save karne ke liye)
connection.commit()            

#STEP5:Connection close karo (kaam khatam hone par)
cursor.close()
connection.close()