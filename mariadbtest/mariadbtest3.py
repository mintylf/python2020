import pymysql

conn = pymysql.connect(host='maria',
                        user='root',
                        passwd='qwer1234',
                        db='test',
                        charset='utf8')


c = conn.cursor()

symbol=input('심볼을 입력 :')
sql="select * from stocks where symbol=%s"
# sql="select * from stocks where symbol=?"
c.execute(sql,(symbol,))
print(c.fetchall())
conn.close()