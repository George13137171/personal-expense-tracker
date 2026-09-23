# Personal Expense Tracker

# --- 1. ΟΡΙΣΜΟΣ ΣΥΝΑΡΤΗΣΕΩΝ ---
import json

def add(expense):
    amount = float(input("Δώσε το ποσό: "))
    category = input("Δώσε την κατηγορία: ")
    expense.append({"amount": amount, "category": category})
    print("Το έξοδος προστέθηκε επιτυχώς!")

def show_expenses(expense):
    if not expense:
        print("Δεν υπάρχουν έξοδα ακόμα.")
    else:
        total = 0
        print("\n--- ΛΙΣΤΑ ΕΞΟΔΩΝ ---")
        for exp in expense:
            print(f"Ποσό: {exp['amount']}€, Κατηγορία: {exp['category']}")
            total += exp["amount"]
        print("-" * 20)
        print(f"Σύνολο εξόδων: {total}€")

def calculate_total(budget, expense):
    total_expense = sum(exp["amount"] for exp in expense)
    remaining_budget = budget - total_expense
    return total_expense, remaining_budget


# --- 2. ΚΥΡΙΩΣ ΠΡΟΓΡΑΜΜΑ (ΜΕΝΟΥ) ---
try:
    with open("expenses.json", "r", encoding="utf-8") as file:
        expense = json.load(file)
        print("Τα έξοδα φορτώθηκαν από το αρχείο.")
except FileNotFoundError:
    expense = []

# Ζητάμε το συνολικό μηνιαίο εισόδημα μία φορά στην αρχή
budget = float(input("Δώσε το συνολικό μηνιαίο εισόδημά σου: "))

while True:
    print("\n--- ΕΛΕΓΧΟΣ ΕΞΟΔΩΝ ---")
    print("1. Προσθήκη νέου εξόδου")
    print("2. Προβολή όλων των εξόδων & συνόλου")
    print("3. Υπολογισμός συνόλου εξόδων & υπολοίπου")
    print("4. Έξοδος")
    
    choice = input("Επιλέξτε μια επιλογή (1-4): ")

    if choice == "1":
        add(expense)
        with open("expenses.json", "w", encoding="utf-8") as file:
            json.dump(expense, file, ensure_ascii=False, indent=4)
        
    elif choice == "2":
        show_expenses(expense)

    elif choice == "3":
        tot_exp, rem_bud = calculate_total(budget, expense)
        print(f"\nΣυνολικά έξοδα: {tot_exp}€")
        print(f"Υπόλοιπο προϋπολογισμού: {rem_bud}€")
        
    elif choice == "4":
        print("Έξοδος από το πρόγραμμα. Γεια σου!")
        break
    else:
        print("Μη έγκυρη επιλογή. Διάλεξε από 1 έως 4.")