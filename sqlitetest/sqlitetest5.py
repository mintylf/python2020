#csv -> DB
import sqlite3,csv


conn = sqlite3.connect('sqlitetest/sup.db')
cur=conn.cursor()
sql='''
    create table if not exists sup
    (
        sup_name varchar(20),
        invoice_number varchar(20),
        part_number varchar(20),
        cost float,
        date date
    )''' #varchar 관련 공부 
#필드이름 데이터타입, <-- 입력형식
cur.execute(sql)



sql='delete from sup'
cur.execute(sql)

input_file='sqlitetest/input.csv'
open_file=open(input_file, 'r')
file_reader = csv.reader(open_file,delimiter=',') #구분자에 대한 업급필요(없을경우 ,가 기본값)
print(next(file_reader)) #next --> 읽어들이는 데이터 파일에서 첫번째줄을 넘기고 읽는다
data=[]
for row in file_reader:
    data.append(row)
sql='insert into sup values(?,?,?,?,?)'    
cur.executemany(sql,data)
conn.commit()
conn.close()