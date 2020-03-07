import pymysql 

conn = pymysql.connect(host='localhost',
                        user='root',
                        passwd='qwer1234'
                        db='test'
                        cursorclass=pymysql.cursors.DictCursor)


cur=conn.cursors