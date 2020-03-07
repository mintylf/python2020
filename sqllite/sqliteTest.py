import sqlite3

conn = sqlite3.connect('sqliteTest/example.db')
c = conn.cursor()
c.execute('''
create table if not exists stocks
(date text,trans text,symbol text,qty real,price real)
''')
conn.commit()
conn.close()