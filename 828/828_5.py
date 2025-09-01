users = {
    "alice123": {
        "ID": "alice123",
        "PW": "abc123"
    }
}

status = False
username = input("Enter username: ")
if username in users:
    password = input("Enter password: ")
    if password == users[username]["PW"]:
        print("*Login successful*")
        status = True
    else:
        print("Login failed")
else:
    print("Username not found")

while status == True:
    todolist = {
        "20250828":{
            "item1":"",
            "item2":""
        }
    }
    while True:
        act = int(input("Create:1, Update:2, Delete:3, Quit: 4: "))
        match act:
            case 1:
                print("Create")
                date = input("생성할 날짜를 입력하세요 형식:YYYYMMDD: ")
                text1 = input("item1: ")
                text2 = input("item2: ")
                todolist[date] = {
                    "item1":text1,
                    "item2":text2
                }
            case 2:
                print("Update")
                date_u = input("수정할 날짜를 입력하세요 형식:YYYYMMDD: ")
                if date_u in todolist:
                    item_n = input("수정할 item을 입력하세요 형식:item#: ")
                    if item_n in todolist[date_u]:
                        text_n = input("수정할 text를 입력하세요: ")
                        todolist[date_u][item_n] = text_n
                        print("수정했습니다.")
                    else:
                        print("존재하지 않습니다.")
                else:
                    print("존재하지 않습니다.")
            case 3:
                print("Delete")
                date_d = input("삭제할 날짜를 입력하세요 형식:YYYYMMDD: ")
                if date_d in todolist:
                    item_d = input("삭제할 item을 입력하세요 형식:item#: ")
                    if item_d in todolist[date_d]:
                        del todolist[date_d][item_d]
                        print("삭제되었습니다.")
                    else:
                        print("존재하지 않습니다.")
                else:
                    print("존재하지 않습니다.")
            case 4:
                print("Quit")
                break
            case _:
                print("None")
    break
print(todolist)