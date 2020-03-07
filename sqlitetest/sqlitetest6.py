import sqliteDB


while True:
    print('''
    1. 테이블 생성
    2. 데어터 입력
    3. 데이터 수정
    4. 데이터 삭제
    5. 데이터 리스트
    6. 종료
    ''')
    menu=input()
    if menu=='1':
        sqliteDB.create_table()
    elif menu=='2':
        sqliteDB.insert_data()
    elif menu=='3':
        sqliteDB.update_data()
    elif menu=='4':
        sqliteDB.delete_data()
    elif menu=='5':
        break
    else:
        print("메뉴를 잘못 선택하셨습니다")