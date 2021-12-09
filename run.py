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


def validate_menu_input(data):
    """
    Checks if the user input is a number between 1 and 2.
    """
    try:
        if int(data) != 1 and int(data) != 2:
            raise ValueError(
                f'A number between 1 or 2 is required. You entered {data}'
            )
    except ValueError as e:
        print(f'Invalid input: {e}, please try again. \n')


def menu():
    print('Hello! Welcome to the strength calculator!\n')
    print('Please chose an option: ')

    print('Type 1 / 2\n')
    print('1. Check your average')
    print('2. View age average')
    menu_input = input()
    validate_menu_input(menu_input)


menu()