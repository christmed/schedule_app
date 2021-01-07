import datetime
import time
import sys
import re


def today_greeter():
    """Displays a message with the current date."""
    day_of_week = datetime.datetime.today().strftime('%A')
    date = datetime.datetime.today().strftime('%d/%m/%Y')
    print(f"Hi {name}, today is: {day_of_week} | Date: {date}"
          f"\nWhat are you going to do today?")
    time.sleep(2)


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
            if act != '':
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


def continue_options():
    """Displays set of instructions to decide what to do next."""

    msg = "\nEnter 'c' to continue adding activities."
    msg += "\nEnter 'm' to modify existing changes."
    msg += "\nEnter 'd' when you're done adding activities."
    msg += '\nWould you like to continue?'
    print(msg)


def continue_settings():
    """"Displays continue options."""

    while True:
        msg = "\nWould you like to see the instructions once again?"
        msg += "\nChoose an option from menu (1-3)"
        msg += "\n\t1. Yes"
        msg += "\n\t2. No"
        msg += "\n\t3. NO, Never Ask Again!!"

        print(msg)
        setts_resp = input()
        if setts_resp != '1' and setts_resp != '2' and setts_resp != '3':
            print('Invalid option. Please try again.')
            continue
        else:
            break
    return setts_resp


option_error = 'Please choose a valid option' \
      '\nE.g Start: 07:00 AM End: 02:00 PM'

name = input('Welcome to "The Daily Scheduler", What is your name? ')
today_greeter()
print_instructions(5)

schedule = create_schedule()
c_schedule = schedule.copy()
print_schedule(c_schedule)
ask_again = False

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
    matched_pattern = check_format(pattern, start)
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

    continue_options()
    continue_resp = input()

    if continue_resp == 'q':
        sys.exit()
    elif continue_resp == 'c':
        if ask_again:
            continue
        settings = continue_settings()
        if settings == '1':
            print_instructions(3)
            continue
        elif settings == '2':
            continue
        else:
            ask_again = True
            continue
