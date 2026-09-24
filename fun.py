from datetime import datetime

def get_current_month():
    """Επιστρέφει τον τρέχοντα μήνα και έτος (π.χ. '2026-09')."""
    return datetime.now().strftime("%Y-%m")

def add(data):
    """Προσθέτει νέο έξοδο στη λίστα δεδομένων."""
    amount = float(input("Δώσε το ποσό: "))
    category = input("Δώσε την κατηγορία: ")
    data["expenses"].append({"amount": amount, "category": category})
    print("Το έξοδο προστέθηκε επιτυχώς!")

def show_expenses(data):
    """Εμφανίζει τα έξοδα και το σύνολο."""
    expenses = data["expenses"]
    if not expenses:
        print("Δεν υπάρχουν έξοδα ακόμα για αυτόν τον μήνα.")
    else:
        total = 0
        print("\n--- ΛΙΣΤΑ ΕΞΟΔΩΝ ---")
        for exp in expenses:
            print(f"Ποσό: {exp['amount']}€, Κατηγορία: {exp['category']}")
            total += exp["amount"]
        print("-" * 20)
        print(f"Σύνολο εξόδων: {total}€")

def calculate_total(data):
    """Υπολογίζει τα συνολικά έξοδα και το υπόλοιπο βάσει του budget."""
    total_expense = sum(exp["amount"] for exp in data["expenses"])
    remaining_budget = data["budget"] - total_expense
    return total_expense, remaining_budget

def update_budget(data):
    """Αυξάνει τον προϋπολογισμό και δείχνει το νέο πραγματικό υπόλοιπο."""
    current_total_budget = data["budget"]
    total_expenses = sum(exp["amount"] for exp in data["expenses"])
    
    print(f"\n--- Διαχείριση Προϋπολογισμού ---")
    print(f"Τρέχων Συνολικός Προϋπολογισμός: {current_total_budget}€")
    print(f"Συνολικά Έξοδα έως τώρα: {total_expenses}€")
    
    try:
        extra_amount = float(input("Βάλτε το ποσό που προστέθηκε (π.χ. μπόνους): "))
        
        if extra_amount > 0:
            new_total_budget = current_total_budget + extra_amount
            new_remaining = new_total_budget - total_expenses
            
            data["budget"] = new_total_budget  # Ενημερώνουμε το budget στα δεδομένα
            
            print(f"\n Επιτυχία ενημέρωσης!")
            print(f" ➔ Νέος Συνολικός Προϋπολογισμός: {new_total_budget}€")
            print(f" ➔ Νέο Διαθέσιμο Υπόλοιπο (μετά τα έξοδα): {new_remaining}€")
        else:
            print(" Το ποσό πρέπει να είναι μεγαλύτερο από το 0.")
            
    except ValueError:
        print(" Λάθος εισαγωγή. Παρακαλώ πληκτρολογήστε έναν έγκυρο αριθμό.")