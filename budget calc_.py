# Budget Calculator

def get_income():
    income = float(input("Enter your total income for the month: "))
    return income

def get_expenses():
    expenses = []
    print("Enter your expenses for the month (type 'done' when finished):")
    while True:
        expense = input("Enter an expense (or 'done' to finish): ")
        if expense.lower() == 'done':
            break
        try:
            expenses.append(float(expense))
        except ValueError:
            print("Please enter a valid number.")
    return expenses

def calculate_balance(income, expenses):
    total_expenses = sum(expenses)
    balance = income - total_expenses
    return total_expenses, balance

def display_results(income, total_expenses, balance):
    print("\n--- Monthly Budget Summary ---")
    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${balance:.2f}")
    if balance < 0:
        print("You are over budget!")
    elif balance == 0:
        print("You are breaking even.")
    else:
        print("You are within your budget. Good job!")

def main():
    income = get_income()
    expenses = get_expenses()
    total_expenses, balance = calculate_balance(income, expenses)
    display_results(income, total_expenses, balance)

if __name__ == "__main__":
    main()
