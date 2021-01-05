import datetime
import time
import sys


def today_greeter():
    """Displays a message with the current date."""
    day_of_week = datetime.datetime.today().strftime('%A')
    date = datetime.datetime.today().strftime('%d/%m/%Y')
    print(f"Hi {name}, today is: {day_of_week} | Date: {date}"
          f"\nWhat are you going to do today?")


def create_schedule():
    """Creates a dict with the hours of the day"""

    schedule_dict = dict()
    for i in range(47):
        if i % 2 == 0:
            x = {i: [f"{int(i / 2)}:00 - {int(i / 2)}:30", [None]]}
        else:
            x = {i: [f"{int((i - 1) / 2)}:30 - {int((i + 1) / 2)}:00", [None]]}

        schedule_dict.update(x)

    return schedule_dict


def print_schedule(schedule):
    """Displays the schedule"""
    for key, values in schedule.items():
        print(f"{key}. {values[0]}")


def sim_update():
    """Simulates schedule update."""
    print('\nUpdating schedule...')
    time.sleep(1)
    print('Done\n')


name = input('Welcome to "The Daily Scheduler", What is your name? ')
today_greeter()
print("\nEnter 'q' at any time to quit.")
print('Select an option from 1 to 24 to add activities.')
print('Begin hour must be earlier than the End hour.\n')
time.sleep(7)

schedule = create_schedule()
c_schedule = schedule.copy()
print_schedule(schedule)

begins, ends = [], []