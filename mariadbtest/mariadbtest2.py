# import pymysql

# conn = pymysql.connect(host='localhost',
#                         user='root',
#                         password='qwer1234',
#                         db='test',
#                         charset='utf8',
#                         cursorclass=pymysql.cursors.DictCursor)

# c=conn.cursor()
# sql='select * from stocks'
# c.excute(sql)
# print(c.fetchall())
# conn.close()