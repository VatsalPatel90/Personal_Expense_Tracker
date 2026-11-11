# Personal Expense Tracker

A Python-based Personal Expense Tracker that helps users manage, organize, and track their daily expenses.

The application uses JSON for storing expense records, allowing users to access their saved data even after closing and restarting the program.

## Features

- **Add Expense:** Add expenses with category, amount, description, and date.
- **View Expenses:** Display all saved expenses.
- **Search Expenses:** Search expenses by category.
- **Filter Expenses:** View expenses belonging to a selected category.
- **Calculate Total Expenses:** Calculate the total amount spent.
- **Monthly Expense Summary:** View the total expenses for the current month.
- **Delete Expense:** Delete one or multiple expense records.
- **Input Validation:** Handle invalid amounts, empty descriptions, and invalid menu choices.
- **JSON Storage:** Automatically save and load expense records using a JSON file.

## Technologies Used

- Python
- JSON
- Git
- GitHub

## Project Structure

```text
Personal_Expense_Tracker/
│
├── main.py
├── expense_practice.py
├── .gitignore
└── README.md
```

**Note:** `expenses.json` is generated locally when the application saves expense records. It is excluded from GitHub using `.gitignore`.

## Requirements

- Python 3.x
- No external Python libraries are required.

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/VatsalPatel90/Personal_Expense_Tracker.git
```

2. Open the project folder:

```bash
cd Personal_Expense_Tracker
```

3. Run the application:

```bash
python3 main.py
```

## Application Menu

The application provides the following options:

1. Add Expense
2. View Expenses
3. Search Expenses
4. Filter Expenses
5. Monthly Expense Summary
6. Delete Expense
7. Exit

## Data Storage

Expense records are stored locally in `expenses.json` using JSON format.

Each expense contains:

- Category
- Amount
- Description
- Date

The application loads previously saved expenses when it starts and saves changes to the JSON file.

## Learning Outcomes

Through this project, I practiced:

- Python functions and loops
- Lists and dictionaries
- File handling
- CSV and JSON operations
- Exception handling
- Input validation
- Searching and filtering data
- Git and GitHub version control

## Project Status

Core application features have been implemented and tested. Documentation, screenshots, project report, and final demo preparation are in progress.

## Author

Vatsal Thumar

**GitHub Repository:**  
https://github.com/VatsalPatel90/Personal_Expense_Tracker
