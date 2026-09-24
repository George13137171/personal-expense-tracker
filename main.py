# Personal Expense Tracker
import json
from fun import get_current_month, add, show_expenses, calculate_total, update_budget

# --- 1. LOAD AND CHECK MONTH ---
current_month = get_current_month()

try:
    with open("expenses.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        
        # Check if the month has changed
        if data.get("month") != current_month:
            print(f"\n New month started ({current_month})!")
            new_budget = float(input("Enter your new monthly budget: "))
            data = {
                "month": current_month,
                "budget": new_budget,
                "expenses": []
            }
        else:
            print("Current month data loaded successfully.")
            
except FileNotFoundError:
    # If the file does not exist, create it from scratch
    print("Previous file not found.")
    new_budget = float(input("Enter your total monthly income/budget: "))
    data = {
        "month": current_month,
        "budget": new_budget,
        "expenses": []
    }

# Save state immediately to the file
with open("expenses.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


# --- 2. MAIN PROGRAM (MENU) ---
while True:
    print("\n--- EXPENSE TRACKER ---")
    print(f"Month: {data['month']} | Current Budget: {data['budget']}€")
    print("1. Add new expense")
    print("2. View all expenses & total")
    print("3. Calculate total expenses & remaining balance")
    print("4. Bonus - Update budget")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")

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
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose from 1 to 5.")