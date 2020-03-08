import pymysql


def conndb():
    conn = pymysql.connect(host='maria', user='root', passwd='qwer1234', db='test', cursorclass=pymysql.cursors.DictCursor)
    return conn

def create_table():
    conn=conndb()
    c = conn.cursor()
    sql=('''
    CREATE TABLE if not exists products(
        products_id int,
        products_name varchar(50),
        price int default 0,
        description text,
        picture_url varchar(500),
        CONSTANT PRIMARYKEY (product_id) 
    ''')
    c.execute(sql)
    conn.commit()
    conn.close()
    
def insert_data():
    data=[]
    conn=conndb()
    c = conn.cursur()
    input("")
    sql = 'insert into products values(%s,%s,%s,%s,%s,%s)'
    c.executemany(sql)
    


def listdata():
    pass

def select_data():
    conn=conndb
    c=conn.cursor()
    sql='select * from stocks'
    c.execute(sql)
    print(c.fetchall())
    conn.close()

def     update_data():
    pass


def deletedata():
    input_file=''
    conn=conndb()
    cur=conn.cursor()
    sql = "delete from products"
    cur.execute(sql)
