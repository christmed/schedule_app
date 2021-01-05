import datetime
import time


def create_schedule():
    """Creates a dict with the hours of the day"""

    schedule_dict = dict()
    for i in range(48):
        if i % 2 == 0:
            x = {i: [f"{int(i / 2)}:00 - {int(i / 2)}:30", [None]]}
        else:
            x = {i: [f"{int((i - 1) / 2)}:30 - {int((i + 1) / 2)}:00", [None]]}

        schedule_dict.update(x)

    return schedule_dict


schedule = create_schedule()
