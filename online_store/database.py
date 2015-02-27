__author__ = 'Matt Borgman'


import sqlite3
import store

conn = sqlite3.connect('user_db')

c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS users
              (name text, email text)''')


conn.commit()

# def get_users():
#     for len(store.better_buy.list_of_customers):
#         user_info = store.better_buy.list_of_customers.pop()
#         return user_info

# user_info = store.better_buy.list_of_customers
user_info = [['matt','mgborgman@gmail.com'],['ashley','ashley@gmail.com']]


c.executemany('INSERT INTO users VALUES (?,?)', user_info)

c.execute('SELECT * FROM users')
rows = c.fetchall()
for row in rows:
    print(row)

conn.close()