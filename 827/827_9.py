import json

print("Create your user profile")

user_id = input("Enter your ID:")
nickname = input("Enter your nickname: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
birth_year = input("Enter your birth year: ")
gender = input("Enter your gender (M/F): ")

profile = {
    "id": user_id,
    "nickname": nickname,
    "email": email,
    "phone": phone,
    "birth_year": birth_year,
    "gender": gender
}

print("Your profile created")
print(f"ID:", user_id)
print(f"Nickname:", nickname)
print(f"Email:", email)
print(f"Phone:", phone)
print(f"Birth Year:", birth_year)
print(f"Gender:", "Male" if gender == "m" else "Female")

print(json.dumps(profile, indent=2))

field_to_edit = input("\nEnter the field you want to edit: ")
new_value = input(f"Enter new value for '{field_to_edit}': ")

profile[field_to_edit] = new_value

print(f"\n'{field_to_edit}' updated successfully!")
print("\n[Final profile]")
print(json.dumps(profile, indent=2))
      