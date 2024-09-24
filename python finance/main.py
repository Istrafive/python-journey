import pandas
import csv
from datetime import datetime
import matplotlib.pyplot
from input_data import get_amount, get_category, get_date, get_description

# This code creates a csv file where data can be entered by the user

class Csv:
    csv_file='finance_data.csv'
    Columns=['date',
            'amount',
            'category',
            'description']

    @classmethod
    def initialize_csv(cls)->None:
        try:
            pandas.read_csv(cls.csv_file) 
        except FileNotFoundError:
            DataFrame = pandas.DataFrame(columns=cls.Columns)
            DataFrame.to_csv(cls.csv_file, index=False)
    
    # This function allows the user to add data and then write that data into the file and opens
    # the csv file in append mode

    @classmethod
    def add_data(cls,date:str,amount:float,category:str,description:str)->None:
        new_data = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        with open(cls.csv_file, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.Columns)
            writer.writerow(new_data)
        print("Data was successfully added")

    # This function gives the user all the transactions within a date range

    @classmethod
    def get_transactions(cls, start_date, end_date)->str:
        DataFrame = pandas.read_csv(cls.csv_file)
        DataFrame['date'] = pandas.to_datetime(DataFrame['date'], format="%d-%m-%Y")
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")

        mask = (DataFrame['date'] >= start_date) & (DataFrame['date'] <= end_date)
        filtered_DataFrame = DataFrame.loc[mask]

        if filtered_DataFrame.empty:
            print("There were no transactions found in that given date range")
        else:
            print(
                f"Transactions from {start_date.strftime("%d-%m-%Y")} to {end_date.strftime("%d-%m-%Y")}"
            )
            print(
                filtered_DataFrame.to_string(
                    index=False, formatters={'date': lambda x: x.strftime("%d-%m-%Y")}
                    )
                )
            
            total_income = filtered_DataFrame[filtered_DataFrame['category'] == "Income"]['amount'].sum()
            total_expense = filtered_DataFrame[filtered_DataFrame['category'] == "Expense"]['amount'].sum()
            print("\nSummary:")
            print(f"Total Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Current Net Total: ${(total_income - total_expense):.2f}")

        return filtered_DataFrame
    
# This function will call the other functions in the proper order to collect the data

def add()->None:
    Csv.initialize_csv()
    date = get_date(
        ("Enter the date of the transaction (DD-MM-YYYY) or 'enter' for today's date: "),
        allow_default = True
    )
    amount = get_amount()
    category = get_category()
    description = get_description()

    Csv.add_data(date, amount, category, description)

# This function generates a plot of the total income and total expenses

def plot_transactions(DataFrame, start_date, end_date)->None:
    if DataFrame.index.name != "date":
        DataFrame.set_index("date", inplace=True)

    income_DataFrame = (
        DataFrame[DataFrame["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(DataFrame.index, fill_value=0)
    )

    matplotlib.pyplot.figure(figsize=(10,5))
    matplotlib.pyplot.plot(income_DataFrame.index, income_DataFrame["amount"], label="Income", color='g')
    matplotlib.pyplot.title(f"Income and Expenses from {start_date} to {end_date}")
    matplotlib.pyplot.ylabel("Amount")
    matplotlib.pyplot.xlabel("Date")
    matplotlib.pyplot.legend()
    matplotlib.pyplot.board(True)
    matplotlib.pyplot.show()


# This function allows the code to run in an ordered way while carrying out the instructions that the
# user requires

def main()->None:
    while True:
        print("\n1. Add a new transaction")
        print("2. View transaction and summary within a date range")
        print("3. Exit")
        user_choice = input("Enter your choice (1-3): ")

        if user_choice == '1':
            add()
        elif user_choice == '2':
            start_date = get_date("Enter the start date (DD-MM-YYYY): ")
            end_date = get_date("Enter the end date (DD-MM-YYYY): ")
            print()
            DataFrame = Csv.get_transactions(start_date, end_date)
            while True:
                graph_question = input("Do you want to see a graph? (Y/N) ")
                if graph_question.upper() == 'Y':
                    plot_transactions(DataFrame, start_date, end_date)
                    break
                if graph_question.upper() == 'N':
                    break
                continue
        elif user_choice == '3':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Choose either 1, 2 or 3")
            continue

if __name__ == '__main__':
    main()