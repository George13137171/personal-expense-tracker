# Personal Expense Tracker - Main File
import json
from fun import (
    get_current_month, 
    add, 
    show_expenses, 
    calculate_total, 
    update_budget, 
    show_categories_percentage
)
from colorama import Fore, Style

# --- 1. LOAD AND MONTH CHECK ---
current_month = get_current_month()

try:
    with open("expenses.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        
        # Check if the month has changed
        if data.get("month") != current_month:
            print(Fore.YELLOW + f"\n New month detected ({current_month})!")
            new_budget = float(input("Enter your new monthly budget: "))
            data = {
                "month": current_month,
                "budget": new_budget,
                "expenses": []
            }
        else:
            print(Fore.GREEN + "Current month data loaded successfully.")
            
except FileNotFoundError:
    # If the file doesn't exist, create it from scratch
    print(Fore.YELLOW + "Previous file not found.")
    new_budget = float(input("Enter your total monthly income/budget: "))
    data = {
        "month": current_month,
        "budget": new_budget,
        "expenses": []
    }

# Save the current state immediately to the file
with open("expenses.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


# --- 2. MAIN PROGRAM (MENU) ---
while True:
    print(Fore.CYAN + "\n--- EXPENSE TRACKER ---")
    print(f"Month: {data['month']} | Current Budget: {data['budget']}€")
    print("1. Add new expense")
    print("2. View all expenses & total")
    print("3. Calculate total expenses & balance")
    print("4. Bonus - Update budget")
    print("5. Category analysis & percentages (Bars)")
    print("6. Exit")
    
    choice = input("Select an option (1-6): ")

    if choice == "1":
        add(data)
        with open("expenses.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
    elif choice == "2":
       show_expenses(data)

    elif choice == "3":
        tot_exp, rem_bud = calculate_total(data)
        print(f"\nTotal expenses: {tot_exp}€")
        print(f"Remaining budget: {rem_bud}€")

    elif choice == "4":
        update_budget(data)
        with open("expenses.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    elif choice == "5":
        show_categories_percentage(data)
          
    elif choice == "6":
        print(Fore.GREEN + "Exiting program. Goodbye!")
        break
    else:
        print(Fore.RED + "Invalid option. Choose between 1 and 6.")