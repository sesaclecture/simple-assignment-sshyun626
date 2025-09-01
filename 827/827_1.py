total = 0
shirt = 20000
jeans = 49000
jacket = 85000

products = ["Shirt", "Jeans", "Jacket"]
products_price = [shirt, jeans, jacket]

product1 = int(input("Choose a product (Shirt-0 / Jeans-1 / Jacket-2):"))
total += products_price[product1]

product2 = int(input("Choose another product (Shirt-0 / Jeans-1 / Jacket-2):"))
total += products_price[product2]

discount = 10000
total -= discount

print(f"You purchased {products[product1]} and {products[product2]}.")
print(f"Discount applied: {discount} won")
print(f"Total price after discount: {total} won")