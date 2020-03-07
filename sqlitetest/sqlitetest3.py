import sqlite3

conn = sqlite3.connect('sqlitetest/example.db')
c = conn.cursor()

c.execute('select * from stocks')
print(c.fetchall())

symbol=input('심볼을 입력 :')
sql="select * from stocks where symbol = '%s'"%symbol
sql="select * from stocks where symbol=?" #?는 sqlite 전용 라이브러리에서 지원하는 문법(문자열, 수에 상관없이 받아들인다 api 참고 sqlite 쿼리문 물음표)
c.execute(sql,(symbol,)) #symbol의 인자값은 튜플로 들어감(symbol을 튜플로 맞춰줘야함 api 참고) 튜플 또는 리스트로 묶어서 값을 넣는다
                        #튜플은 콤마를 안찍을시 인식을 못할수도 있음 빈튜플 () 1개 튜플 (111,)
print(c.fetchall())
conn.close()