#!/usr/bin/env python3

"""
Daily Details class to capture activity and relate it to external things
"""


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
        self.weight = None
        self.calories_consumed = None
        self.sleep = None
        self.drinking = None
        # TODO need to think about how to handle multiple activities in one day
        self.exercise_type = None
        self.exercise_calories = None
        self.exercise_metres_gained = None
        self.exercise_average_heart_rate = None
        self.mood_score = None
        self.date_file = None

    def __str__(self):
        # TODO Need to populate this for useful data return for an object
        pass

    def get_data_file(self):
        # TODO this should open a dataframe from a stored CSV file
        # This should probably be initiated straight away so that's kept open
        # to be captured under self.data_file
        pass

    def save_data_file(self):
        # TODO this should save the dataframe as a stored CSV file

    def get_activity_details(self):
        # TODO get commandline entries for the details
        pass

