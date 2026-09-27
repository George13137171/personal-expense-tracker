# 💰 CLI Personal Expense Tracker

A clean, lightweight, and interactive command-line personal finance manager built in Python.

---

## ✨ Key Features

* **Modular Architecture:** Clean separation between core logic (`fun.py`) and interface control (`main.py`).

* **Automated Monthly Reset:** Tracks month changes via `datetime` and prompts for a fresh budget.

* **Expense Management:** Add expenses with custom amounts and categories; view a full detailed history.

* **Dynamic Budgeting:** Instantly compute remaining balances or boost your budget mid-month.

* **Terminal Visualizations:** Category percentage breakdowns with vibrant, colorful progress bars (`colorama`).

* **Data Persistence:** Automatic local saving and loading using structured JSON (`expenses.json`).

---

## 📸 Application Preview

Here is how the application looks in action, including expense entry and the interactive terminal breakdown:

| Adding an Expense | Category Analysis & Progress Bars |
| :---: | :---: |
| ![Add Expense](https://via.placeholder.com/400x250?text=Add+Expense) | ![Category Bars](https://via.placeholder.com/400x250?text=Category+Analysis) |

---

## 🚀 Quick Start

1. Make sure Python is installed on your system.

2. Download `main.py` and `fun.py` into your project folder.

3. Open your terminal in the project directory and install dependencies:
   `pip install colorama`

4. Run the application using:
   `python main.py`

---

## 🛠️ Tech Stack

* **Language:** Python (Functions, File Handling, Control Flow, `datetime`)

* **Styling:** Colorama (Cross-platform terminal styling & progress bars)

* **Storage:** JSON (Structured data serialization)

---

## 👤 Author

Created by a 2nd-year Computer Science student at the Athens University of Economics and Business (AUEB).