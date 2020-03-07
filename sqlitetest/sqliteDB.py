import sqlite3

def db_conn():
    return sqlite3.connect('sqlitetest/book.db') #database 연결(생성)
    

def create_table():
    conn=db_conn()      #커넥션 객채 받기
    cur=conn.cursor()   #커서객채
    sql="""
        create table if not exists books(
            title text,
            pub_date text,
            pub text,
            pages integer,
            recommend integer
        )
    """                 #쿼리문
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("테이블 생성")

def insert_data():
    conn=db_conn()
    cur=conn.cursor()
    title=input('책제목: ')
    pub_date=input('출판일 :')
    pub=input('출판사 :')
    pages=int(input('총 페이지 :'))
    recommend=input('비고 :')
    data=[title,pub_date,pub,pages,recommend]

    sql='insert into books values(?,?,?,?,?)'
    cur.execute(sql,data)
    conn.commit()
    conn.close()

def select_data():
    conn=db_conn()
    cur=conn.cursor()
    title=input('제목을 입력 :')    #문자열 받아 title에 입력
    title='%'+title+'%'            #와일드카드, 
    
    sql="select * from books where title like ?"
    c.execute(sql,(title,))
    print(cur.fetchall())
    conn.close()

def update_data():
    pass

