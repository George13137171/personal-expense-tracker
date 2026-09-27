# 💰 Personal Expense Tracker
A clean, lightweight, and interactive command-line Personal Expense Tracker built with Python, featuring a modular multi-file architecture, automated monthly state transitions, and colorful terminal visualizations.

✨ Current Features
Modular Architecture: Clean separation of concerns with main.py handling the menu and flow control and fun.py managing the business logic and calculations.

Automatic Month Detection: Uses Python's datetime module to track month changes and automatically prompt for a fresh budget when a new month begins.

Expense Management & History: Add new expenses with custom amounts and categories, and view a detailed history along with grand totals.

Dynamic Budget Tracking: Input your monthly budget, instantly calculate your remaining balance, and update/boost your budget mid-month with automatic balance recalculation.

Category Analysis & Visual Bars: Automatically calculates percentages per category and renders vibrant, colorful progress bars directly in the terminal using Colorama.

Data Persistence: Automatically saves and loads your financial records locally using a structured JSON file (expenses.json).

🚀 How to Run
Make sure you have Python installed on your system.

Clone the repository or download the source files (main.py and fun.py).

Open your terminal or command prompt inside the project folder.

Install the required dependencies:
pip install colorama

Run the application using:
python main.py

Follow the on-screen menu prompts to manage your budget and expenses.

🛠️ Technologies Used
Python (Core logic, file handling, control flow, functions, datetime)

Colorama (Cross-platform terminal styling and colored progress bars)

JSON (Structured local data storage and serialization)

👤 Author
Created by a 2nd-year Computer Science student at the Athens University of Economics and Business (AUEB).
