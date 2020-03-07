import sqlite3

conn = sqlite3.connect('sqlitetest/example.db')
c = conn.cursor()
c.execute('''
insert into stocks 
values('2020-01-05','buy','rhat',100,35.14)
''')
conn.commit()
conn.close()