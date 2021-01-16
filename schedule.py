import datetime
import time
import sys
import re
from create_file import File


def today_greeter():
    """Displays a message with the current date."""
    day_of_week = datetime.datetime.today().strftime('%A')
    date = datetime.datetime.today().strftime('%d/%m/%Y')
    print(f"Hi {name}, today is: {day_of_week} | Date: {date}"
          f"\nWhat are you going to do today?")
    time.sleep(1)


def print_instructions(pause_time):
    """Displays the starting instructions of the program.

    **pause_time: time program will stop before it continues.
    """

    instructions = "\nEnter 'q' at any time to quit."
    instructions += "\nEnter the start time and end time of the activity."
    instructions += "\n'Start time' must be earlier than the 'End time'."
    instructions += "\nE.g. Start: 12:00 PM End: 04:30 PM\n"
    print(instructions)
    time.sleep(pause_time)


def create_schedule():
    """Creates a dict with the hours of the day"""

    s = datetime.datetime.strptime('12:00 AM', '%I:%M %p')
    r = [s.strftime('%I:%M %p')]
    for i in range(30, 60 * 24, 30):
        r.append((s + datetime.timedelta(minutes=i)).strftime('%I:%M %p'))

    schedule = {}
    for i in range(len(r)):
        try:
            hours = {i: {r[i] + " - " + r[i + 1]: ""}}
            schedule.update(hours)
        except IndexError:
            pass

    return schedule


def print_schedule(schedule):
    """Prints only the hours of the schedule."""
    for value in schedule.values():
        for hour in value:
            print(hour)


def get_hour_key(schedule, searched_value, start=True):
    """Looks for the key hour that matches the searched value.

    **schedule: Current version of the schedule.
    **start: determines the match method.
        (startswith - endswith) of searched value.
    **searched_value: The substring to look up in hour options.
    """

    # Get the starting hour key.
    for key, value in schedule.items():
        for hour in value:
            if start:
                if hour.startswith(str(searched_value)):
                    return key
            else:
                if hour.endswith(str(searched_value)):
                    return key


def add_activity(schedule, activity, start_key, end_key):
    """Update activity.

    **schedule: Dict that will be updated.
    **activity: String that will be added to hour key.
    **start_key: starting point of activity.
    **end_key: ending point of activity.
    """

    index = (int(start_key), int(end_key + 1))
    for key, value in schedule.items():
        for hour in value:
            if key in range(index[0], index[1]):
                schedule[key][hour] = activity

    return schedule


def show_current_changes(schedule):
    """Show recent changes made to the schedule.
    **schedule: current version of schedule.
    """

    for value in c_schedule.values():
        for hr, act in value.items():
            if act != '' and not act.isspace():
                print(f"{hr}\t\t{act}")
            else:
                pass


def sim_update():
    """Simulates schedule update."""
    print('\nUpdating schedule...')
    time.sleep(1)
    print('Done\n')


def check_format(pattern, str):
    """Checks if pattern is a valid option.

    **pattern: the substring to match.
    **str: the string to look for the pattern.
    """

    matched = re.match(pattern, str)
    is_match = bool(matched)

    return is_match


def continue_opts():
    """Displays set of instructions to decide what to do next."""

    msg = '\nWould you like to continue?'
    msg += "\nEnter 'c' to continue adding activities."
    msg += "\nEnter 'm' to modify existing changes."
    msg += "\nEnter 'd' when you're done adding activities."
    print(msg)


def continue_menu(schedule, ask_again):
    """Displays main continue menu and checks answer.

    **schedule: current version of schedule
    **ask_again: settings chose by user of function
    cont_sub_menu_instr():
    """

    while True:
        continue_opts()
        continue_resp = input()

        if continue_resp == 'q':
            sys.exit()
        elif continue_resp == 'c':
            if ask_again:
                ask_again = check_subc_setts()
            return schedule, ask_again
        elif continue_resp == 'm':
            schedule_opt = mod_sub_menu(schedule)
            schedule = mod_schedule(schedule, schedule_opt)
            return schedule, ask_again
        # Still working on 'done' menu.
        elif continue_resp == 'd':
            filename = save_file(c_schedule)
            email = get_email(schedule)
            sys.exit()
        else:
            print(invalid_msg)
            continue


def cont_sub_menu_instr():
    """Displays continue sub-menu."""

    msg = "\nWould you like to see the instructions once again?"
    msg += "\nChoose an option from menu (1-3)"
    msg += "\n\t1. Yes"
    msg += "\n\t2. No"
    msg += "\n\t3. NO, Never Ask Again!!"
    print(msg)


def cont_sub_setts():
    """"Displays continue options."""

    while True:
        cont_sub_menu_instr()
        setts_resp = input()

        if setts_resp == 'q':
            sys.exit()
        if setts_resp != '1' and setts_resp != '2' and setts_resp != '3':
            print(invalid_msg)
            continue
        else:
            break
    return setts_resp


def check_subc_setts():
    """Saves continue sub-menu settings chose by user."""

    settings = cont_sub_setts()
    if settings == 'q':
        sys.exit()
    if settings == '1':
        print_instructions(1)
        return True
    elif settings == '2':
        return True
    elif settings == '3':
        return False


def mod_instr():
    """Displays instructions of modify menu"""

    msg = "\nRead the instructions carefully."
    msg += '\nEnter a digit from 0 to 46.'
    msg += "\nTo choose non-continuous options, separate them with a ','."
    msg += "\n\tE.g Option: 7,12,15,24"
    msg += "\nTo choose continuous options, separate them with a '-'."
    msg += "\n\tE.g Option: 24-27"
    msg += "\nTo choose a single option. E.g Option: 40"
    print(msg)
    time.sleep(1)


def mod_sub_menu(f_schedule):
    """Displays modify menu.

    **f_schedule: Complete version of schedule.
    """

    print('Here is your schedule.\n')
    for key, value in f_schedule.items():
        for hr, act in value.items():
            print(f"{key}. {hr}\t\t{act}")
    time.sleep(1)
    mod_instr()

    while True:
        print('\nWhich option(s) you wish to modify?')
        mod_resp = input('Option(s): ')
        mod_resp, is_valid = check_mod_resp(mod_resp, f_schedule)

        if is_valid:
            break

    return mod_resp


def check_mod_resp(mod_resp, schedule):
    """Checks if option is valid.

    **mod_resp: Response
    **schedule:
    """

    if mod_resp == 'q':
        sys.exit()

    if not mod_resp.isdigit():
        print(invalid_msg)
        return None, False

    if 1 < len(mod_resp) <= 2:
        if int(mod_resp) in schedule.keys():
            return mod_resp, True
        else:
            print(invalid_msg)
            return None, False

    if len(mod_resp) > 2:
        if ',' in mod_resp:
            mod_resp = mod_resp.split(',')
            n_continuous = check_mod_opts(mod_resp, schedule)
            if n_continuous:
                return mod_resp, True
            else:
                return None, False
        else:
            mod_resp = tuple(mod_resp.split('-'))
            continuous = check_mod_opts(mod_resp, schedule)
            if continuous:
                return mod_resp, True
            else:
                return None, False


def check_mod_opts(mod_resp, schedule):
    """Checks if all selected (continuous, non-continuous)
    options are in schedule options.

    **mod_response: The options to look for.
    **schedule: the dict to look for the mod_response elements.
    """

    val_opt = []
    for i in mod_resp:
        if int(i) in schedule.keys():
            val_opt.append(True)
        else:
            val_opt.append(False)

    if all(val_opt):
        return True
    else:
        return False


def mod_schedule(schedule, sch_opts):
    """Modifies schedule.

    **schedule: current version of schedule.
    **sch_options: options to be modified.
    """

    print("\nPress 'Enter' on your keyboard to delete activities.")
    n_activity = input('New activity: ')

    if sch_opts is list:
        for i in sch_opts:
            for key, value in schedule.items():
                for hr, act in value.items():
                    if key == int(i):
                        schedule[key][hr] = n_activity
    else:
        for i in range(int((sch_opts[0])), int((sch_opts[1])) + 1):
            for key, value in schedule.items():
                for hr, act in value.items():
                    if key == i:
                        schedule[key][hr] = n_activity
    sim_update()

    return schedule


def get_file_fmt():
    """Gets file format to save it later."""

    while True:
        format = input('\nSave schedule as (format):\n'
                       '- txt\n'
                       '- xlsx\n'
                       '- csv\n'
                       )
        if format != 'txt' and format != 'xlsx' and format != 'csv':
            print(invalid_msg)
            continue
        else:
            break

    return format


def save_file(schedule):
    """Save file as: format.

    **returns filename to then send it to user's email."""

    while True:
        date = datetime.datetime.today().strftime('%d-%m-%Y')
        format = get_file_fmt()
        filename = f"{date} schedule.{format}"

        if format == 'txt':
            save_file = File(filename, schedule)
            save_file.txt_file()
        elif format == 'xlsx':
            save_file = File(filename, schedule)
            save_file.xlsx_file()
        elif format == 'csv':
            save_file = File(filename, schedule)
            save_file.csv_file()
        elif format == 'q':
            sys.exit()

        return filename


def get_email(schedule):
    """Gets user email.

    **schedule: final version of schedule.
    """

    valid_email = False
    while valid_email:
        rcv_email = input('Would you like to receive the schedule on your email? (y/n)')
        if rcv_email == 'y':
            email = input('Enter email: ')
            valid_email = verify_email(email)
        elif rcv_email == 'n':
            print_schedule(schedule)
            sys.exit()
        else:
            print(invalid_msg)
            continue

    return email


def verify_email(email):
    """Verify emails format."""

    # Create email regex.
    email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something 
    )''', re.VERBOSE)

    is_match = re.match(email_regex, email)
    return bool(is_match)


option_error = 'Please choose a valid option' \
               '\nE.g Start: 07:00 AM End: 02:00 PM'
invalid_msg = 'Invalid option Please try again'

name = input('Welcome to "The Daily Scheduler", What is your name? ')
today_greeter()
print_instructions(1)

schedule = create_schedule()
c_schedule = schedule.copy()
print_schedule(c_schedule)
ask_again = True

while True:
    start = input('\nStart: ')
    if start == 'q':
        sys.exit()

    # Checks that format matches the schedule hours format.
    pattern = re.compile(r"[0-1][0-9]\W[03][0]\s[APM]")
    matched_pattern = check_format(pattern, start)
    if not matched_pattern:
        print(option_error)
        continue

    end = input('End: ')
    if end == 'q':
        sys.exit()
    matched_pattern = check_format(pattern, end)
    if not matched_pattern:
        print(option_error)
        continue

    print(f"\nYou selected {start} - {end}")
    activity = input(("Which activity would you like "
                      "to add to the schedule?\n "))

    # Adds activity to the schedule.
    s_index = get_hour_key(c_schedule, start, True)
    e_index = get_hour_key(c_schedule, end, False)
    c_schedule = add_activity(c_schedule, activity, s_index, e_index)

    # Shows only the changes made to the schedule.
    sim_update()
    show_current_changes(c_schedule)
    time.sleep(1.5)

    c_schedule, ask_again = continue_menu(c_schedule, ask_again)
