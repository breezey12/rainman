import sqlite3

with sqlite3.connect("todos.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE todos(date TEXT, description TEXT)")
