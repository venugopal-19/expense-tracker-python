import json
import os
from datetime import datetime


FILE_NAME = "expenses.json"


# -----------------------------
# Load expenses from file
# -----------------------------
def load_expenses():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    return []


# -----------------------------
# Save expenses to file
# -----------------------------
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# -----------------------------
# Add Expense
# -----------------------------
def add_expense(expenses):

    print("\n========== ADD EXPENSE ==========")

    name = input("Enter expense name: ")

    # Amount validation
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    category = input("Enter category: ")

    # Automatically get today's date
    date = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("\nExpense added successfully!")


# -----------------------------
# View Expenses
# -----------------------------
def view_expenses(expenses):

    print("\n========== ALL EXPENSES ==========")

    if len(expenses) == 0:
        print("No expenses added yet.")
        return

    for index, expense in enumerate(expenses, start=1):

        print(f"\nExpense #{index}")
        print("Name:", expense["name"])
        print("Amount: ₹", expense["amount"])
        print("Category:", expense["category"])
        print("Date:", expense["date"])
        print("-----------------------------")


# -----------------------------
# Calculate Total
# -----------------------------
def calculate_total(expenses):

    print("\n========== TOTAL EXPENSE ==========")

    if len(expenses) == 0:
        print("No expenses added yet.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total Expense: ₹{total:.2f}")


# -----------------------------
# Search Expense
# -----------------------------
def search_expense(expenses):

    print("\n========== SEARCH EXPENSE ==========")

    if len(expenses) == 0:
        print("No expenses added yet.")
        return

    search = input("Enter expense name to search: ").lower()

    found = False

    for index, expense in enumerate(expenses, start=1):

        if search in expense["name"].lower():

            print(f"\nExpense #{index}")
            print("Name:", expense["name"])
            print("Amount: ₹", expense["amount"])
            print("Category:", expense["category"])
            print("Date:", expense["date"])

            found = True

    if not found:
        print("No matching expense found.")


# -----------------------------
# Delete Expense
# -----------------------------
def delete_expense(expenses):

    print("\n========== DELETE EXPENSE ==========")

    if len(expenses) == 0:
        print("No expenses to delete.")
        return

    view_expenses(expenses)

    while True:

        try:
            number = int(input("\nEnter expense number to delete: "))

            if number < 1 or number > len(expenses):
                print("Invalid expense number.")
            else:
                deleted = expenses.pop(number - 1)

                save_expenses(expenses)

                print(
                    f"'{deleted['name']}' expense deleted successfully!"
                )

                break

        except ValueError:
            print("Please enter a valid number.")


# -----------------------------
# Edit Expense
# -----------------------------
def edit_expense(expenses):

    print("\n========== EDIT EXPENSE ==========")

    if len(expenses) == 0:
        print("No expenses to edit.")
        return

    view_expenses(expenses)

    while True:

        try:
            number = int(input("\nEnter expense number to edit: "))

            if number < 1 or number > len(expenses):
                print("Invalid expense number.")
            else:
                expense = expenses[number - 1]

                print("\nLeave input empty to keep the old value.")

                new_name = input(
                    f"Enter new name [{expense['name']}]: "
                )

                if new_name:
                    expense["name"] = new_name

                new_amount = input(
                    f"Enter new amount [{expense['amount']}]: "
                )

                if new_amount:
                    try:
                        new_amount = float(new_amount)

                        if new_amount > 0:
                            expense["amount"] = new_amount
                        else:
                            print("Amount must be greater than 0.")

                    except ValueError:
                        print("Invalid amount. Old amount kept.")

                new_category = input(
                    f"Enter new category [{expense['category']}]: "
                )

                if new_category:
                    expense["category"] = new_category

                save_expenses(expenses)

                print("\nExpense updated successfully!")

                break

        except ValueError:
            print("Please enter a valid number.")


# -----------------------------
# Category Summary
# -----------------------------
def category_summary(expenses):

    print("\n========== CATEGORY SUMMARY ==========")

    if len(expenses) == 0:
        print("No expenses added yet.")
        return

    categories = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    for category, amount in categories.items():

        print(f"{category}: ₹{amount:.2f}")


# -----------------------------
# Monthly Summary
# -----------------------------
def monthly_summary(expenses):

    print("\n========== MONTHLY SUMMARY ==========")

    if len(expenses) == 0:
        print("No expenses added yet.")
        return

    months = {}

    for expense in expenses:

        month = expense["date"][:7]
        amount = expense["amount"]

        if month in months:
            months[month] += amount
        else:
            months[month] = amount

    for month, amount in months.items():

        print(f"{month}: ₹{amount:.2f}")


# -----------------------------
# Main Program
# -----------------------------
def main():

    expenses = load_expenses()

    while True:

        print("\n")
        print("======================================")
        print("          💰 EXPENSE TRACKER")
        print("======================================")

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total")
        print("4. Search Expense")
        print("5. Delete Expense")
        print("6. Edit Expense")
        print("7. Category Summary")
        print("8. Monthly Summary")
        print("9. Exit")

        print("======================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            calculate_total(expenses)

        elif choice == "4":
            search_expense(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            edit_expense(expenses)

        elif choice == "7":
            category_summary(expenses)

        elif choice == "8":
            monthly_summary(expenses)

        elif choice == "9":
            print("\nThank you for using Expense Tracker!")
            print("Goodbye! 👋")
            break

        else:
            print("\nInvalid choice! Please select 1-9.")


# Start the program
if __name__ == "__main__":
    main()