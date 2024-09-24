from datetime import datetime

# These functions provide the framework for how the data will be entered by the user and their formats

def get_date(prompt, allow_default=False) -> str:
    while True:
        date_str = input(prompt)
        if allow_default and not date_str:
            return datetime.today().strftime("%d-%m-%Y")
        try:
            valid_date = datetime.strptime(date_str, "%d-%m-%Y")
            return valid_date.strftime("%d-%m-%Y")
        except ValueError:
            print("This date format is not valid, please enter the date in dd-mm-yyyy")


def get_amount()->float:
    try:
        amount=float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a positive value")
        return amount
    except ValueError as error:
        print(error)
        return get_amount()


def get_category()->str:
    categories_dict={'I': 'Income',
                     'E': 'Expense'}
    category = input("Enter the category ('I' for Income or 'E' for Expense) ").upper()
    if category in categories_dict:
        return categories_dict[category]
    else:
        print("Invalid category, please enter 'I' for Income and 'E' for Expense")
        return get_category()


def get_description()->str:
    return input("Enter a description (optional, press Enter to skip): ")
