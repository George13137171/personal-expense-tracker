from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama for cross-platform support
init(autoreset=True)

def get_current_month():
    """Returns the current month and year (e.g., '2026-09')."""
    return datetime.now().strftime("%Y-%m")

def add(data):
    """Adds a new expense to the data list."""
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    data["expenses"].append({"amount": amount, "category": category})
    print(Fore.GREEN + "Expense added successfully!")

def show_expenses(data):
    """Displays expenses and total."""
    expenses = data["expenses"]
    if not expenses:
        print(Fore.YELLOW + "No expenses recorded yet for this month.")
    else:
        total = 0
        print(Fore.CYAN + "\n--- EXPENSE LIST ---")
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
    """Increases the budget and shows the new actual remaining balance."""
    current_total_budget = data["budget"]
    total_expenses = sum(exp["amount"] for exp in data["expenses"])
    
    print(f"\n{Fore.CYAN}--- Budget Management ---")
    print(f"Current Total Budget: {current_total_budget}€")
    print(f"Total Expenses so far: {total_expenses}€")
    
    try:
        extra_amount = float(input("Enter the added amount (e.g., bonus): "))
        
        if extra_amount > 0:
            new_total_budget = current_total_budget + extra_amount
            new_remaining = new_total_budget - total_expenses
            
            data["budget"] = new_total_budget  # Update budget in data structure
            
            print(Fore.GREEN + "\n Update successful!")
            print(f" ➔ New Total Budget: {new_total_budget}€")
            print(f" ➔ New Remaining Balance (after expenses): {new_remaining}€")
        else:
            print(Fore.RED + " The amount must be greater than 0.")
            
    except ValueError:
        print(Fore.RED + " Invalid input. Please type a valid number.")

def show_categories_percentage(data):
    """Calculates percentages per category and displays colored bars."""
    expenses = data["expenses"]
    if not expenses:
        print(Fore.YELLOW + "No expenses recorded yet to calculate percentages.")
        return

    category_totals = {}
    grand_total = 0

    for exp in expenses:
        cat = exp["category"]
        amount = exp["amount"]
        grand_total += amount
        category_totals[cat] = category_totals.get(cat, 0) + amount

    print(Fore.CYAN + "\n--- CATEGORY & PERCENTAGE ANALYSIS ---")
    
    colors = [Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.YELLOW, Fore.RED]
    i = 0
    
    for cat, total in category_totals.items():
        percentage = (total / grand_total) * 100
        color = colors[i % len(colors)]
        
        # Create a visual progress bar (1 character '█' per 5%)
        bar_length = int(percentage / 5)
        bar = "█" * bar_length
        
        print(f"{color}{cat}: {total}€ ({percentage:.1f}%)")
        print(f"{color}{bar}")
        i += 1
        
    print(Style.RESET_ALL + f"\nTotal expenses so far: {grand_total}€")