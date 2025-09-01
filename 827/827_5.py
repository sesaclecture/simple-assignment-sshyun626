stocks = [
    "intel",
    "apple",
    "alphabet",
    "amazon",
    "meta"
]

target_stocks = input("Enter the stock you want to find:")
index = stocks.index(target_stocks)

new_stock = input("Enter a new stock to insert: ")
insert_pos = int(input("At which index to insert it?"))
stocks.insert(insert_pos, new_stock)

remove_stock = input("enter a stock to remove: ")
stocks.remove(remove_stock)

print(f"Updated stock list: {stocks}")

