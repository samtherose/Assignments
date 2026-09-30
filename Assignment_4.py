# Level #04 Assignment: Personal Expense Analyzer
# Create a Python program that analyzes a series of personal expenses.

# Create list of expenses starting empty
expenses = []

# ask user to add an expense until the number is "0"
while True:
    entry=input("Enter an expense amount (or type '0' to finish): ")

    # Verify if the input is a valid number
    try:
        expense = float(entry)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # stop the loop if the user enters "0"
    if expense == 0:
        break

    # no negative expenses allowed
    if expense < 0:
        print("Negative expenses are not allowed. Please enter a positive number.")
        continue

    # add the expense to the list
    expenses.append(expense)

# clasify the expenses into categories
small_count = 0
medium_count = 0
large_count = 0

# add the expenses to the appropriate category
for expense in expenses:
    if expense < 25:
        small_count += 1
    elif expense <= 100:
        medium_count += 1
    else:
        large_count += 1

# count and calculate the total expenses
count = len(expenses)
total = sum(expenses)
average = total / count
smallest = min(expenses)
largest = max(expenses)

# display the results
print("====================")
print("Expense Summary:")
print("====================")
print(f"Total number of expenses: {count}")
print(f"Total amount spent: ${total:.2f}")
print(f"Average expense amount: ${average:.2f}")
print(f"Small expenses (< $25): {small_count}")
print(f"Medium expenses ($25 - $100): {medium_count}")
print(f"Large expenses (> $100): {large_count}")
