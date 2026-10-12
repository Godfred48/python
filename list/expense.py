expenses = [25.50, -5.00, 12.00, 0, 45.99, 100.00, -12.50, 8.50, 0, 30.00]
valid_expense = []
total = 0
largest = 0

for expense in expenses:
    if expense > 0:
        valid_expense.append(expense)

for ve in valid_expense:
    total = total + ve

    if ve > largest:
        largest = ve
print("")
print(f"Your valid expensees for the week is {valid_expense}")
print(f"Total for expense is {total}")
print(f"Highest expense is {largest}")