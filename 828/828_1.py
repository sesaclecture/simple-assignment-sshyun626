users = {
    "이동현": {
        "password": "abcd1234",
        "phone": "010-5438-7567",
        "email": "eastsae@mensakorea.org"

    },
    "홍길동": {
        "password": "qwer5678",
        "phone": "010-1234-5678",
        "email": "honggildong@gmail.com"
    }
}

username = input("아이디: ")

if username in users:
    password = input("비밀번호: ")
    if password == users[username]["password"]:
        print("로그인")
        print(f"--- {username}'s 프로필 ---")
        print(f"전화번호: {users[username]['phone']}")
        print(f"이메일: {users[username]['email']}")