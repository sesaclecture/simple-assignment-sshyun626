numbers = [42, 7, 13, 99]

numbers.append(23)
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()

print(f"Final numbers: {numbers}")

languages = ["Python", "Java", "C++", "JavaScript"]

index = languages.index("C++")
print(index)

cart = []
for i in range(3):
    item = input("Add item:")
    cart.append(item)
    print(cart)