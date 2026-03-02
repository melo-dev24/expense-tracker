import json
import os
from datetime import datetime

# Name of the file  where expenses will be stored
FILE_NAME = 'expenses.json'


# Load expenses from the JSON file
def load_expenses():
    # Check if file exists
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                # Return the data inside the file
                return json.load(file)
            except json.JSONDecodeError:
                # If file is empty or corrupted, return empty list
                return []
    # If file does not exist, return empty list
    return []


# Save expenses to the JSON file
def save_expenses(expenses):
    with open(FILE_NAME, "w")as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expenses(expenses):
    description = input("Enter expense description: ").strip()
    amount_input = input("Enter amount: ").strip()
    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add new expense to list
    expenses.append({"description": description,
                    "amount": amount, "date": date})

    print("Expense added successfully!\n")


# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    total = 0
    print("\n--- Expense List ---")
    # Loop through expenses and display them
    for i, expense in enumerate(expenses, 1):
        print(
            f"[{i}]. {expense['description']} - "
            f"₱ {expense['amount']:,.2f}"
            f" ({expense['date']})")
        total += expense["amount"]
    print(f"\n Total Expenses: ₱ {total:,.2f}")
    print("------------------------------\n")


# Delete an expense
def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return
    try:
        choice = int(input("Enter expense number to delete: "))

        # Check if number is valid
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            print(f"Deleted: {removed['description']}")
        else:
            print("Invalid Number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program


def main():
    # Load existing expenses
    expenses = load_expenses()

    while True:
        # Display menu
        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Delete Expense")
        print("4. Exit")

        # Get user choice
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            # Save expenses before exiting
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

            input("\n Press Enter to continue... \n")


# Run the program
if __name__ == "__main__":
    main()
