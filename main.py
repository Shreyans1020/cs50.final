#Shreyans Saraogi and Nick Neuber

import cs50
import openpyxl

from investor import Investor
from stocks import Stocks


def main():

    print("Hello! Welcome to Investing Made Simple!")

    firstName = input(str("Enter your first name: "))
    lastName = input(str("Enter your last name: "))
    email = input(str("Enter your email address: "))
    Bday = input(str("Enter your date of birth: "))
    print("Enter the amount of money you wish to simulate:", end = "")
    money = cs50.get_int()



    print("--------------------------------------------")

    while True:
        print("Do you want to 1) Research a Stock or 2) Make a Portfolio")
        print("1 or 2?   ", end = "")
        choice = cs50.get_int()
        if ((choice == 1) or (choice == 2)):
            break
    stock = input(str("Which company's stock are you interested in?   "))
    excel_document = openpyxl.load_workbook('Stock_Information.xlsx')
        #Database linked

    sheet = excel_document.get_sheet_by_name('Sheet1')
    print (type(excel_document))
    Investor(firstName, lastName, email, Bday, money)
    Stocks()





if __name__=="__main__":
    main()


