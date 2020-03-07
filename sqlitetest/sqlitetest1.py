import sqlite3

print(sqlite3.version)
print(sqlite3.sqlite_version)

conn = sqlite3.connect('sqlitetest/example.db')
c = conn.cursor()
c.execute('''
create table if not exists stocks
(date text,trans text,symbol text,qty real,price real)
''')
conn.commit()
conn.close()