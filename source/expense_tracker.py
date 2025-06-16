#cli tool to track expenses
import json
from datetime import datetime

DATA_FILE = "data/expenses.json"

#load data file
def load_expenses():
    try:
        with open(DATA_FILE, "r") as f:
            expenses = json.load(f)
            return expenses
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(expenses, f, indent=4)
    except FileNotFoundError:
        pass

def add_expense(expenses):
    amount = float(input("Amount: "))
    category = input("Category: ")
    date = input("Date (YYYY-MM-DD) [leave blank for current date]: ")
    if not(date):
        date = datetime.today().strftime("%Y-%m-%d")

    expense = {"amount": amount, "category": category, "date": date}
    expenses.append(expense)
    print("Expense added!")

def view_expenses():
    expenses = load_expenses()
    for expense in expenses:
        print(expense["amount"], expense["category"], expense["date"])

def view_total_expenses(expenses):
    total = sum(e["amount"] for e in expenses)
    print("Total spent: £" + str(total))

def main():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spent")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total_expenses(expenses)
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()



