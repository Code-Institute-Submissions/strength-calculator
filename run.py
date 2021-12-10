import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('strength_calculator')
users = SHEET.worksheet('users')

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def menu():
    print('Hello! Welcome to the strength calculator!\n')
    print('Please chose an option: ')
    print('Type 1 / 2\n')
    print('1. Check your average')
    print('2. View age average')
    menu_input = input()
    validate_menu_input(menu_input)
    
    if menu_input == "1":
        add_new_user()
        
        
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
    

def validate_email(email):
    if(re.fullmatch(regex, email)):
        email = True
        return email
        

def get_all_users():
    """
    Gets worksheet data as a list of dicts and stores
    in all_users variable
    """
    all_users = users.get_all_records()
    user_ids = []
    for user in all_users:
        user_id = user['Id']
        user_ids.append(user_id)
        print(user_ids)

            
        

    # print(all_users)


def add_new_user():
    """
    Creates a new user and gives it an ID. 
    """
    new_user = {}

    while True:
        name = input('Name: ').capitalize()
        if not name.isalpha():
            print('Please only use letters between a-z')
        else:
            break
    new_user['Name'] = name

    while True:
        age = input('Age: ')
        if not age.isnumeric():
            print('Please only use numbers')
        elif len(age) > 2:
            print('Please enter a valid age')
        else:
            break
    new_user['Age'] = age

    while True:
        email = input('Email Adress: ')
        if not validate_email(email):
            print('Please enter a valid email adress')
        else:
            break
    new_user['Email'] = email
        
    print(new_user)


def main():
    get_all_users()
    menu()


main()