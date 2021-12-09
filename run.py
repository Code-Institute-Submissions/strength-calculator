import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('strength_calculator')

answers = SHEET.worksheet('answers')



def main():
    print('Hello! Welcome to the strength calculator!\n')
    print('Please chose an option: ')
    print('Type 1 / 2\n')
    print('1. Check your average')
    print('2. View age average')
    menu_input = input()
    

    print(menu_input)


main()


