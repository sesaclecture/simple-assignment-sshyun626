seats = [
    [False, True, False, True, False],
    [True, False, True, False, True],
    [False, False, True, False, False],
    [False, False, False, False, False],
    [True, False, True, False, True]
]

row = input("Type row: (A, B, C, D, E) ")
row_idx = 0

if row == "A":
    row_idx = 0
elif row == "B":
    row_idx = 1
elif row == "C":
    row_idx = 2
elif row == "D":
    row_idx = 3
elif row == "E":
    row_idx = 4
else:
    print("Invalid row index")

col = int(input("Type column: (1, 2, 3, 4, 5) "))
col_idx = 0
if 1 <= col <= 5:
    col_idx = col - 1
else:
    print("Invalid column index")

seat = seats[row_idx][col_idx]

print(f"Selected seat: {row}{col}")
print(f"Seat status: ", seat)

if seat == True:
    print("Seat is available")
    print("Booking seat...")
    seats[row_idx][col_idx] = False
    print("Booking complete")
    print(seats[row_idx][col_idx])
else:
    print("Seat is already booked")
    for i in range(len(seats)):
        if seats[row_idx][i] == True:
            print(f"Row {row} Column {i+1} is available")
            break
        else:
            if i == len(seats) - 1:
                print(f"Row {row} is not available")