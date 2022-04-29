from tabulate import tabulate
#quick interest calculator
def main():
    amount = int(input("Enter the investment amount: "))
    years = int(input("Enter the number of years: "))
    rate = int(input("Enter the rate as a %: "))
    table = []
    start_balance = amount
    interest_total=0
    for i in range (years):
        interest = start_balance * (rate/100)
        end_balance = start_balance + interest
        interest_total = interest_total + interest
        new_year = [str(i + 1), "{:.2f}".format(start_balance), "{:.2f}".format(interest), "{:.2f}".format(end_balance)]
        table.append (new_year)
        start_balance = end_balance
    end_balance = "{:.2f}".format(end_balance)
    interest_total = "{:.2f}".format(interest_total)
    print(tabulate(table, headers=["Year", "Starting balance", "Interest", "Ending Balance"]))
    print("Ending balance: $" + str(end_balance))
    print("Total interest earned: $" + str(interest_total))

if __name__ == '__main__':
    main()