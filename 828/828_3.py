country = input("Enter a country: ")

if country =="Korean":
    language = "Korean"
    greeting = "안녕하세요"
elif country == "Japan":
    language = "Japanese"
    greeting = "こんにちは"
elif country == "USA":
    language = "English"
    greeting = "Hello"
elif country == "China":
    language = "Chinese"
    greeting = "你好"
elif country == "France":
    language = "French"
    greeting = "Bonjour"
else:
    language = None
    greeting = None

if language and greeting:
    print(f"Official language of {country} is {language}.")
    print(f"Greeting in {language} is '{greeting}'.")
else:
    print("Sorry, we don't have information for that country.")

countries = {
    "Korea": {"language": "Korean", "greeting": "안녕하세요"},
    "Japan": {"language": "Japanese", "greeting": "こんにちは"},
    "USA": {"language": "English", "greeting": "Hello"},
    "China": {"language": "Chinese", "greeting": "你好"},
    "France": {"language": "French", "greeting": "Bonjour"}
}

country = input("Enter a country: ")

info = countries.get(country)

if info:
    print(f"Official language of {country}: {info['language']}")
    print(f"Greeting in {info['language']}: {info['greeting']}")
else:
    print("Sorry, we don't have information for that country.")