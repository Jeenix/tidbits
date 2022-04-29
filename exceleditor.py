import pandas as pd

def main():

    df1 = pd.read_excel(input(""))
    dfahfg = pd.read_excel(input("AHFG "))
    print("The average number of orders per customer is : ", df1["Order History"].mean())

if __name__ == '__main__':
    main()
