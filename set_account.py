import json
import re


def get_info():
    """Gets info from user and checks that is properly formatted."""

    print("To create your account, enter the following information.")
    name = input('Name: ')
    email = input('Email: ')
    username = input('Username: ')
    password = input('Password: ')
    return None


def check_name_fmt(name):
    """Checks name format."""

    # Create name regex.
    name_regex = re.compile(r'^[a-zA-Z]+(\s)?[a-zA-Z]+$')
    is_match = re.match(name_regex, name)
    return bool(is_match)


def check_email_fmt(email):
    """Verify email format."""

    # Create email regex.
    email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+   # username
        @                   # @ symbol
        [a-zA-Z0-9.-]+      # domain name
        (\.[a-zA-Z]{2,4})   # dot-something 
        )''', re.VERBOSE)

    is_match = re.match(email_regex, email)
    return bool(is_match)


def check_user_fmt(username):
    """Verify username format."""

    # Create username regex.
    user_regex = re.compile(r'''
    ^(?=[a-zA-Z0-9._]
    {6,20}$)
    (?!.*[_.]{2})
    [^_.].*[^_.]$
    ''', re.VERBOSE)

    is_match = re.match(user_regex, username)
    return bool(is_match)


username = 'chris_med'
is_valid = check_user_fmt(username)
print(is_valid)

# not_valid = True
# while not_valid:
#     welcome_msg = "Welcome, please choose an option from the menu"
#     user_opts = input('1. Sign up\n2.Log in\n3.Log in as guest')
#
#     if user_opts == '1':
#         pass
#     elif user_opts == '2':
#         pass
#     elif user_opts == '3':
#         pass
#     else:
#         print("Option not in menu. Try again (Only numeric values).")
#         continue
