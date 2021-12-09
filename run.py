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


def menu():
    get_all_users()
    print('Hello! Welcome to the strength calculator!\n')
    print('Please chose an option: ')
    print('Type 1 / 2\n')
    print('1. Check your average')
    print('2. View age average')
    menu_input = input()
    validate_menu_input(menu_input)
    
    if menu_input == "1":
        print('Enter a number between 1-5 to confirm your age')
        print('''
        1. 17 or younger
        2. 18-25
        3. 26-35
        4. 36-50
        5. 51+
        ''')
        user_age = input()
        

def validate_menu_input(data):
    """
    Try statement convert user input to integer. Raise ValueError
    if input aren't either 1 or 2. Or if string cannot be converted 
    into an integer.
    """

    try:
        data = int(data)
        if data not in [1, 2]:
            raise ValueError(
                f'A number between 1 or 2 is required. You entered {data}'
            )
    except ValueError as e:
        print(f'Invalid input: {e}, please try again. \n')
    

def get_all_users():
    """
    Gets worksheet data as a list of dicts and stores
    in all_users variable
    """
    all_users = answers.get_all_records()
    print(all_users)
    



    return all_users


menu()