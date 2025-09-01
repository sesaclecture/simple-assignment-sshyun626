import json
import datetime

print("Create my profile")

name = input("name:")
gender = input("gender (M/F): ")
email = input("email: ")
phone = input("phone number: ")
home = input("home: ")
major = input("major: ")

birth = input("birth: YYYYMMDD: ")

def cal_date() :
    today = datetime.datetime.now().date()
    birth_date = datetime.datetime.strptime(birth, "%Y%m%d")
    age = today.year - birth_date.year
    next_birthday = birth_date.replace(year=today.year+1)
    d_day = next_birthday.date() - today
    return age, d_day



print("My profile:")
print(f"Name:", name)
print(f"Gender:", gender)
print(f"Email:", email)
print(f"Phone:", phone)
print(f"Home:", home)
print(f"Major:", major)
print(f"Birth:", birth, "만 나이:", cal_date()[0], "D-day:", cal_date()[1])
print(f"Gender:", "Male" if gender == "m" else "Female")

my_tech = {"운전면허", "ADsP", "걷기", "자전거 타기"}

project = {
    "project1": {
        "프로젝트명": "탄소배출계산기",
        "주제": "LMM을 활용한 탄소배출량 계산기",
        "사용기술": "프롬프트 기획 및 설계",
        "기간": "2024년 12월 ~ 2025년 1월"
    },
    "project2": {
        "프로젝트명": "별빛 동행 신호등",
        "주제": "교통 약자를 위한 안전 강화 신호등",
        "사용기술": "정책 연구 및 아이디어 도출",
        "기간": "2024년 9월"
    }
}