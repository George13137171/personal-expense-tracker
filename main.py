# Personal Expense Tracker
import json
from fun import get_current_month, add, show_expenses, calculate_total, update_budget

# --- 1. ΦΟΡΤΩΣΗ ΚΑΙ ΕΛΕΓΧΟΣ ΜΗΝΑ ---
current_month = get_current_month()

try:
    with open("expenses.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        
        # Ελέγχουμε αν άλλαξε ο μήνας
        if data.get("month") != current_month:
            print(f"\n Μπήκαμε σε νέο μήνα ({current_month})!")
            new_budget = float(input("Δώσε το νέο μηνιαίο προϋπολογισμό σου: "))
            data = {
                "month": current_month,
                "budget": new_budget,
                "expenses": []
            }
        else:
            print("Τα δεδομένα του τρέχοντος μήνα φορτώθηκαν επιτυχώς.")
            
except FileNotFoundError:
    # Αν δεν υπάρχει το αρχείο, το δημιουργούμε από την αρχή
    print("Δεν βρέθηκε προηγούμενο αρχείο.")
    new_budget = float(input("Δώσε το συνολικό μηνιαίο εισόδημά σου: "))
    data = {
        "month": current_month,
        "budget": new_budget,
        "expenses": []
    }

# Αποθηκεύουμε αμέσως την κατάσταση στο αρχείο
with open("expenses.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


# --- 2. ΚΥΡΙΩΣ ΠΡΟΓΡΑΜΜΑ (ΜΕΝΟΥ) ---
while True:
    print("\n--- ΕΛΕΓΧΟΣ ΕΞΟΔΩΝ ---")
    print(f"Μήνας: {data['month']} | Τρέχον Budget: {data['budget']}€")
    print("1. Προσθήκη νέου εξόδου")
    print("2. Προβολή όλων των εξόδων & συνόλου")
    print("3. Υπολογισμός συνόλου εξόδων & υπολοίπου")
    print("4. Bonus - Αλλαγή προϋπολογισμού")
    print("5. Έξοδος")
    
    choice = input("Επιλέξτε μια επιλογή (1-5): ")

    if choice == "1":
        add(data)
        with open("expenses.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
    elif choice == "2":
       show_expenses(data)

    elif choice == "3":
        tot_exp, rem_bud = calculate_total(data)
        print(f"\nΣυνολικά έξοδα: {tot_exp}€")
        print(f"Υπόλοιπο προϋπολογισμού: {rem_bud}€")

    elif choice == "4":
        update_budget(data)
        with open("expenses.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
          
    elif choice == "5":
        print("Έξοδος από το πρόγραμμα. Γεια σου!")
        break
    else:
        print("Μη έγκυρη επιλογή. Διάλεξε από 1 έως 5.")