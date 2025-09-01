import json

data = {
    "name": "홍길동",
    "age": 25,
    "hobbies": ["reading", "coding", "traveling"]
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("JSON 파일 저장 완료!")
print(data)