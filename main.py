import json
from datetime import date
import os

# GET THE CURRENT PROJECT FOLDER PATH
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# JSON FILE PATH
FILE_PATH = os.path.join(BASE_DIR, "expenses.json")


print("================================")
print("     PERSONAL EXPENSE TRACKER")
print("================================")


# LOAD EXISTING EXPENSES FROM JSON FILE
try:
    with open(FILE_PATH, "r") as file:
        expenses = json.load(file)

except FileNotFoundError:
    expenses = []


while True:

    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expenses")
    print("4. Filter Expenses")
    print("5. Monthly Expense Summary")
    print("6. Delete Expense")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")


    # ADD EXPENSE
    if choice == "1":

        print("\nSelect Expense Category:")
        print("1. Food")
        print("2. Travel")
        print("3. Shopping")
        print("4. Bills")
        print("5. Entertainment")
        print("6. Other")

        category_choice = input("Choose category (1-6): ")

        if category_choice == "1":
            category = "Food"
        elif category_choice == "2":
            category = "Travel"
        elif category_choice == "3":
            category = "Shopping"
        elif category_choice == "4":
            category = "Bills"
        elif category_choice == "5":
            category = "Entertainment"
        elif category_choice == "6":
            category = "Other"
        else:
            category = None

        if category is None:
            print("Invalid category! Please try again.")
            continue

        try:
            amount = float(input("Enter amount: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        description = input("Enter description: ")

        if description.strip() == "":
            print("Description cannot be empty!")
            continue

        expense = {
            "category": category,
            "amount": amount,
            "description": description,
            "date": str(date.today())
        }

        expenses.append(expense)

        # SAVE EXPENSES TO THE SAME JSON FILE
        with open(FILE_PATH, "w") as file:
            json.dump(expenses, file, indent=4)

        print("\nExpense added successfully!")


    # VIEW EXPENSES
    elif choice == "2":

        print("\n-------- ALL EXPENSES --------")

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            total = 0

            for expense in expenses:

                print("\nCategory:", expense["category"])
                print("Amount:", expense["amount"])
                print("Description:", expense["description"])

                if "date" in expense:
                    print("Date:", expense["date"])

                total = total + expense["amount"]

            print("\nTotal Expenses:", total)


    # SEARCH EXPENSES
    elif choice == "3":

        search_category = input("Enter category to search: ")

        found = False

        for expense in expenses:

            if expense["category"].lower() == search_category.lower():

                print("\nCategory:", expense["category"])
                print("Amount:", expense["amount"])
                print("Description:", expense["description"])

                if "date" in expense:
                    print("Date:", expense["date"])

                found = True

        if found == False:
            print("No expenses found in this category.")


    # FILTER EXPENSES
    elif choice == "4":

        print("\nSelect Category to Filter:")
        print("1. Food")
        print("2. Travel")
        print("3. Shopping")
        print("4. Bills")
        print("5. Entertainment")
        print("6. Other")

        filter_choice = input("Choose category (1-6): ")

        if filter_choice == "1":
            filter_category = "Food"
        elif filter_choice == "2":
            filter_category = "Travel"
        elif filter_choice == "3":
            filter_category = "Shopping"
        elif filter_choice == "4":
            filter_category = "Bills"
        elif filter_choice == "5":
            filter_category = "Entertainment"
        elif filter_choice == "6":
            filter_category = "Other"
        else:
            filter_category = None

        if filter_category is None:
            print("Invalid category!")
            continue

        found = False

        for expense in expenses:

            if expense["category"] == filter_category:

                print("\nCategory:", expense["category"])
                print("Amount:", expense["amount"])
                print("Description:", expense["description"])

                if "date" in expense:
                    print("Date:", expense["date"])

                found = True

        if found == False:
            print("No expenses found in this category.")


    # MONTHLY EXPENSE SUMMARY
    elif choice == "5":

        current_month = date.today().strftime("%Y-%m")

        monthly_total = 0

        print("\n-------- MONTHLY EXPENSE SUMMARY --------")
        print("Month:", date.today().strftime("%B %Y"))

        for expense in expenses:

            if "date" in expense:

                if expense["date"].startswith(current_month):

                    monthly_total = monthly_total + expense["amount"]

        print("Total Monthly Expenses:", monthly_total)


    # DELETE MULTIPLE EXPENSES
    elif choice == "6":

        print("\n-------- DELETE EXPENSE --------")

        if len(expenses) == 0:
            print("No expenses available to delete.")

        else:

            for i in range(len(expenses)):

                print("\nExpense Number:", i + 1)
                print("Category:", expenses[i]["category"])
                print("Amount:", expenses[i]["amount"])
                print("Description:", expenses[i]["description"])

            delete_choices = input(
                "\nEnter expense numbers to delete (example: 1,3,5): "
            )

            try:
                numbers = delete_choices.split(",")

                delete_numbers = []

                for number in numbers:

                    number = number.strip()

                    if number == "":
                        continue

                    delete_numbers.append(int(number))

            except ValueError:
                print("Please enter valid expense numbers.")
                continue

            if len(delete_numbers) == 0:
                print("Please enter at least one expense number.")
                continue

            # CHECK FOR DUPLICATE NUMBERS
            if len(delete_numbers) != len(set(delete_numbers)):
                print("Duplicate expense numbers are not allowed.")
                continue

            # CHECK VALID EXPENSE NUMBERS
            valid = True

            for number in delete_numbers:

                if number < 1 or number > len(expenses):
                    valid = False

            if valid == False:
                print("Invalid expense number!")
                continue

            print("\nYou selected", len(delete_numbers), "expenses.")

            confirm = input("Are you sure? (yes/no): ")

            if confirm.lower() == "yes":

                deleted_count = 0

                for number in sorted(delete_numbers, reverse=True):

                    deleted_expense = expenses[number - 1]

                    expenses.remove(deleted_expense)

                    deleted_count = deleted_count + 1

                # SAVE UPDATED EXPENSES TO THE SAME JSON FILE
                with open(FILE_PATH, "w") as file:
                    json.dump(expenses, file, indent=4)

                print(deleted_count, "expenses deleted successfully!")

            else:
                print("Delete operation cancelled.")


    # EXIT
    elif choice == "7":

        print("\nThank you for using Personal Expense Tracker!")
        break


    else:
        print("Invalid choice! Please select between 1 and 7.")
