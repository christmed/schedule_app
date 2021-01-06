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


def print_instructions():
    """Displays the starting instructions of the program."""

    instructions = "\nEnter 'q' at any time to quit."
    instructions += "\nEnter the start time and end time of the activity."
    instructions += "\n'Start time' must be earlier than the 'End time'."
    instructions += "\nE.g. Start: 12:00 PM End: 04:30 PM\n"
    print(instructions)


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


def add_activity(start, end, activity, schedule):
    """Adds activities to the schedule

    **start: indicates the starting time of activity.
    **end: indicates the ending time of activity.
    **activity: to be added to the schedule.
    **schedule: the current version of the schedule.
    """

    # Get the starting hour key.
    for key, value in schedule.items():
        for hour in value:
            if hour.startswith(str(start)):
                start = key

    # Get the ending hour key.
    for key, value in schedule.items():
        for hour in value:
            if hour.endswith(str(end)):
                end = key

    # Update activity
    index = (int(start), int(end + 1))
    for key, value in schedule.items():
        for hour in value:
            if key in range(index[0], index[1]):
                schedule[key][hour] = activity
    return schedule


def show_current_changes(schedule):
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

    **pattern:
    **str:
    """

    matched = re.match(pattern, str)
    is_match = bool(matched)

    return is_match


option_error = 'Please choose a valid option' \
      '\nE.g Start: 07:00 AM End: 02:00 PM'

name = input('Welcome to "The Daily Scheduler", What is your name? ')
today_greeter()
print_instructions()

schedule = create_schedule()
c_schedule = schedule.copy()
print_schedule(c_schedule)

while True:
    start = input('\nStart: ')
    if start == 'q':
        sys.exit()

    # Checks that format matches the schedule hours format.
    pattern = re.compile(r"[0-1][0-9]\W[0-3][0]\s[APM]")
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


    # Adds activity to the schedule.
    print(f"\nYou selected {start} - {end}")
    activity = input(("Which activity would you like "
                      "to add to the schedule?\n "))
    c_schedule = add_activity(start, end, activity, c_schedule)

    # Shows only the changes made to the schedule.
    sim_update()
    show_current_changes(c_schedule)
