from enum import Enum
import datetime
import re

status = False
class Role(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

def val_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

users = {
    "alice123": {
        "name": "Alice",
        "birth": "2000-01-01",
        "ID": "alice123",
        "PW": "abc123",
        "role": Role.ADMIN
    },
    "bob456": {
        "name": "Bob",
        "birth": "2010-01-01",
        "ID": "bob456",
        "PW": "def456",
        "role": Role.EDITOR
    },
    "john789": {
        "name": "John",
        "birth": "2005-01-01",
        "ID": "john789",
        "PW": "ghi789",
        "role": Role.VIEWER
    },
    "a": {
        "name": "a",
        "birth": "2005-01-01",
        "ID": "a",
        "PW": "a",
        "role": Role.ADMIN
    }
}



status = False
username = input("Enter username: ")

if username in users:
    password = input("Enter password: ")
    if password == users[username]["PW"]:
        print("*Login successful*")
        status = True
        
        role = users[username]["role"]
        match role:
            case Role.ADMIN:
                print("Welcome, Admin!")
                print("모든 사용자 수정 및 삭제 가능")       
            case Role.EDITOR:
                print("Welcome, Editor!")
                print("모든 사용자 수정 및 본인 계정 삭제 가능")
            case Role.VIEWER:
                print("Welcome, Viewer!")
                print("본인 계정만 수정 및 삭제 가능")
    else:
        print("Login failed")
        
else:
    print("Username not found")

while status == True:
        act = int(input("Create:1, Update:2, Delete:3, Quit: 4: "))
        match act:
            case 1:
                print("Create")
                create_id = input("생성할 계정을 입력해주세요: ")
                if create_id not in users:
                    c_name = input("name: ")
                    c_birth = input("birth: ")     
                    while val_date(c_birth) == False:
                        c_birth = input("잘못 입력했습니다.\n생일을 다시 입력해주세요: ")
                    c_PW = input("PW(조건: 10자이상 특수문자 포함): ")
                    while len(c_PW)<10 or not re.search(r"[!@#$%^&*()]", c_PW):
                        c_PW = input("다시입력해주세요\nPW(조건: 10자이상, 특수문자 포함): ")

                    users[create_id] = {
                        "name": c_name,
                        "birth": c_birth,
                        "ID": create_id,
                        "PW": c_PW,
                        "role": Role.VIEWER
                    }
                    create_id = input("{create_id} 계정을 생성했습니다!")
                    print(users)
                else:
                    print("ID 중복")
            case 2:
                print("Update")
                mid = input("수정할 계정을 입력하세요: ")
                if mid in users:
                    if (mid == username) | (users[mid]["role"] == "editor") | (users[mid]["role"] == "admin"):
                        info_n = input("수정할 정보를 선택하세요 name, birth, ID, PW, role ")
                        if info_n in users[mid]:
                            info_n = input("수정할 내용 입력하세요: ")
                            users[mid][info_n] = info_n
                            print("수정했습니다.")
                            print(users)
                        else:
                            print("존재하지 않습니다.")
                    else:
                        print("권한이 없습니다.")
                else:
                    print("존재하지 않습니다.")
            case 3:
                print("Delete")
                id_d = input("삭제할 계정을 입력하세요: ")
                if id_d in users:
                    if id_d == username:
                        del users[id_d]
                        print("{id_d} 계정이 삭제되었습니다.")
                        print(users)
                    elif users[id_d]["role"] == "admin":
                        del users[id_d]
                        print("{id_d} 계정이 삭제되었습니다.")
                        print(users)
                    else:
                        print("실행 권한이 없습니다.")
                else:
                    print("존재하지 않습니다.")
            case 4:
                print("Quit")
                break
            case _:
                print("None")
print(users)