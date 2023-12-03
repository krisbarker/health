#!/usr/bin/env python3

"""
Daily Details class to capture activity and relate it to external things
"""


import pandas as pd

from datetime import datetime

from genericmodules.get_config import get_config_details


class DailyDetails:
    """
    - weight
    - calories consumed
    - sleep hours / minutes
    - drinking (alcohol) the night before
    - exercise - type
    - exercise - calories burned
    - exercise - meters gained
    - exercise - heart rate
    - resting heart rate
    - Mood score (out of 10.  10 very good, 1 very poor)
    """

    def __init__(self, name):
        self.name = name # probably a date
        self.date = None
        self.weight = None
        self.calories_consumed = None
        self.sleep = None
        self.drinking = None
        # TODO need to think about how to handle multiple activities in one day
        self.exercise_type = None
        self.exercise_duration = None
        self.exercise_calories = None
        self.exercise_metres_gained = None
        self.exercise_average_heart_rate = None
        self.mood_score = None
        self.date_file = None

    def __str__(self):
        return "Need to put something better in the str method than just the name: " + self.name

    def __repr__(self):
        return "Need to put something better in the repr than just the name: " + self.name

    def get_data_file(self):
        # This should probably be initiated straight away so that's kept open
        # to be captured under self.data_file
        config = get_config_details()
        file = config['health_data_file']['file']
        import_df = pd.read_csv(file)
        self.date_file = import_df

    def save_data_file(self):
        # TODO this should save the dataframe as a stored CSV file
        pass

    def get_activity_details(self):
        # TODO get commandline entries for the details
        pass


def setup_input_object():
    activity_input = DailyDetails("Today's Activity")
    activity_input.get_data_file()
    return activity_input


def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%d/%m/%Y").strftime('%d/%m/%Y'):
            raise ValueError
        return True
    except ValueError:
        return False


def get_input_data(activity_input):

    right_date = False
    while right_date is False:
        print("Please input activity date in format dd/mm/yyyy")
        input_date = input("Please input date: ")
        if validate(input_date):
            right_date = True
        else:
            print("That format isn't right")
    activity_input.date = input_date

    

    return activity_input


def main():
    activity_input = setup_input_object()
    activity_input = get_input_data(activity_input)
    print(activity_input.date)


if __name__ == "__main__":
    main()
