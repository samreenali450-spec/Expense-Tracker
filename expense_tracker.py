total = 0
print("Expense Tracker")

while True:
    try:
        expense = float(input("Enter Expense (0 to stop): "))
        if expense == 0:
            break
        total = total + expense
        print(f"Current Total: {total}")
    except ValueError:
        print("Invalid Data! Please enter only numbers.")

print(f"Total Spent: {total}")