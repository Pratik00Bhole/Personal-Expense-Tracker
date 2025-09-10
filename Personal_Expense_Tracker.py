# Personal Expense Tracker
import csv
from datetime import datetime
import os

FILENAME = "expenses.csv"

# Ensure the CSV file exists with headers
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter Category (Food, Travel, Shopping, etc.): ")
    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")
        return
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("✅ Expense Added Successfully!\n")

def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            print("\n--- Expense Records ---")
            for row in reader:
                print(f"Date: {row[0]}, Category: {row[1]}, Amount: ₹{row[2]}")
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

def summary():
    total = 0
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                total += float(row[2])
        print(f"\n💰 Total Expenses: ₹{total}\n")
    except FileNotFoundError:
        print("No expenses recorded yet.\n")

def main():
    initialize_file()
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary()
        elif choice == "4":
            print("👋 Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
