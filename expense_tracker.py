import datetime
import csv
import os

FILE_NAME = "expenses.csv"
expenses = []

def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            expenses.extend(list(reader))

def save_expenses():
    with open(FILE_NAME, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['date', 'category', 'amount', 'note']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for e in expenses:
            writer.writerow(e)

def add_expense():
    try:
        date_str = input("Date (YYYY-MM-DD, leave blank for today): ").strip()
        if not date_str:
            date_str = datetime.date.today().isoformat()
        else:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")  # validate format

        category = input("Category (Food, Travel, etc.): ").strip().title()
        amount = float(input("Amount (₹): ").strip())
        note = input("Note: ").strip()

        expenses.append({
            'date': date_str,
            'category': category,
            'amount': f"{amount:.2f}",
            'note': note
        })
        save_expenses()
        print(f"✅ Added {category} - ₹{amount:.2f} on {date_str}\n")

    except ValueError:
        print("⚠️ Invalid date or amount. Try again.\n")

def list_expenses():
    if not expenses:
        print("\n(No expenses recorded yet)\n")
        return

    print("\n📒 Your Expenses:")
    for idx, e in enumerate(expenses, 1):
        print(f"{idx}. {e['date']} | {e['category']} | ₹{e['amount']} | {e['note']}")
    print()

def delete_expense():
    list_expenses()
    if not expenses:
        return

    try:
        idx = int(input("Enter expense number to delete: ").strip())
        if 0 < idx <= len(expenses):
            removed = expenses.pop(idx - 1)
            save_expenses()
            print(f"🗑️ Deleted {removed['category']} - ₹{removed['amount']} on {removed['date']}\n")
        else:
            print("⚠️ Invalid number.\n")
    except ValueError:
        print("⚠️ Please enter a number.\n")

def show_summary():
    if not expenses:
        print("\n(No expenses to summarize)\n")
        return

    total = sum(float(e['amount']) for e in expenses)
    by_category = {}
    for e in expenses:
        by_category[e['category']] = by_category.get(e['category'], 0) + float(e['amount'])

    print(f"\n💰 Total Spent: ₹{total:.2f}")
    print("📊 By Category:")
    for cat, amt in by_category.items():
        print(f" - {cat}: ₹{amt:.2f}")
    print()

def menu():
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. List Expenses")
    print("3. Delete Expense")
    print("4. Show Summary")
    print("5. Exit")
    return input("Choose an option: ").strip()

# --- Program starts ---
load_expenses()

while True:
    choice = menu()
    if choice == '1':
        add_expense()
    elif choice == '2':
        list_expenses()
    elif choice == '3':
        delete_expense()
    elif choice == '4':
        show_summary()
    elif choice == '5':
        print("👋 Goodbye! Your expenses have been saved.")
        break
    else:
        print("⚠️ Invalid option. Please choose between 1–5.\n")