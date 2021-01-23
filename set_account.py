import json
import re

def sign_up():
    """Creates a new account for user."""

    name = input('Name: ')
    email = input('Email: ')

    return None


not_valid = True
while not_valid:
    welcome_msg = "Welcome, please choose an option from the menu"
    user_opts = input('1. Sign up\n2.Log in\n3.Log in as guest')

    if user_opts == '1':
        pass
    elif user_opts == '2':
        pass
    elif user_opts == '3':
        pass
    else:
        print("Option not in menu. Try again (Only numeric values).")
        continue
