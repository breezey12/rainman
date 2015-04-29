import sqlite3

with sqlite3.connect("weather_users.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE user_info(phone_number TEXT, zipcode TEXT, verified INT, subscribed INT)")
