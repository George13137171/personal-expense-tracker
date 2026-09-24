from datetime import datetime

def get_current_month():
    """Returns the current month and year (e.g., '2026-09')."""
    return datetime.now().strftime("%Y-%m")

def add(data):
    """Adds a new expense to the data list."""
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    data["expenses"].append({"amount": amount, "category": category})
    print("Expense added successfully!")

def show_expenses(data):
    """Displays expenses and the total."""
    expenses = data["expenses"]
    if not expenses:
        print("No expenses recorded yet for this month.")
    else:
        total = 0
        print("\n--- EXPENSE LIST ---")
        for exp in expenses:
            print(f"Amount: {exp['amount']}€, Category: {exp['category']}")
            total += exp["amount"]
        print("-" * 20)
        print(f"Total expenses: {total}€")

def calculate_total(data):
    """Calculates total expenses and remaining balance based on budget."""
    total_expense = sum(exp["amount"] for exp in data["expenses"])
    remaining_budget = data["budget"] - total_expense
    return total_expense, remaining_budget

def update_budget(data):
    """Increases the budget and shows the new actual balance."""
    current_total_budget = data["budget"]
    total_expenses = sum(exp["amount"] for exp in data["expenses"])
    
    print(f"\n--- Budget Management ---")
    print(f"Current Total Budget: {current_total_budget}€")
    print(f"Total Expenses So Far: {total_expenses}€")
    
    try:
        extra_amount = float(input("Enter the added amount (e.g., bonus): "))
        
        if extra_amount > 0:
            new_total_budget = current_total_budget + extra_amount
            new_remaining = new_total_budget - total_expenses
            
            data["budget"] = new_total_budget  # Update budget in data
            
            print(f"\n Budget updated successfully!")
            print(f" ➔ New Total Budget: {new_total_budget}€")
            print(f" ➔ New Available Balance (after expenses): {new_remaining}€")
        else:
            print(" The amount must be greater than 0.")
            
    except ValueError:
        print(" Invalid input. Please enter a valid number.")