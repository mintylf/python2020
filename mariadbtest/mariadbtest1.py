import pymysql 

conn = pymysql.connect(host='maria',
                        user='root',
                        passwd='qwer1234',
                        db='test',
                        cursorclass=pymysql.cursors.DictCursor)


c = conn.cursor()
c.execute('''
CREATE TABLE if not exists stocks
(data text, trans text, symbol text, qty real, price real)s
''')

c.execute('''
insert into stocks 
values('2020-01-05','buy','rhat',100,35.14)
''')
conn.commit()
conn.close()