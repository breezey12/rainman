import sqlite3

with sqlite3.connect("weather_users.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE user_info(username TEXT, password TEXT, zipcode INT, phone_number TEXT)")
