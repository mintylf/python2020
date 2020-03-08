import project_function


project_function.create_table()

while True():
    print('''
    1. 제퓸입력
    2. 제품목록
    3. 제품검색
    4. 제품수정
    5. 제품삭제
    6. 종료
    ''')
    menu = input()
    if menu == '1':
        project_function.insert_data()
    elif menu == '2':
        project_function.listdata()
    elif menu == '3':
        project_function.select_data()
    elif menu == '4':
        project_function.updatedata()
    elif menu == '5':
        project_function.deletedata()
    elif menu == '6':
        break
    else:
        print("잘못입력")
