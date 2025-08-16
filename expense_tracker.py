import datetime
import csv
import os

FILE_NAME = "expenses.csv"
expenses = []

def load_expenses():
    """Load expenses from CSV if available"""
    if os.path.exists(FILE_NAME) and os.stat(FILE_NAME).st_size > 0:
        with open(FILE_NAME, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                expenses.append({
                    'date': row['date'],
                    'category': row['category'],
                    'amount': float(row['amount']),  # store as number
                    'note': row['note']
                })

def save_expenses():
    """Save all expenses to CSV"""
    with open(FILE_NAME, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['date', 'category', 'amount', 'note']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
