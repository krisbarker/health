#!/usr/bin/env python3

"""
Creates random data to fill the daily file to test the presentation
"""

import random

import pandas as pd

from genericmodules.get_config import get_config_details


def get_calories_list():
    calories_list = [
        "2100",
        "2050",
        "2070",
        "2150",
        "2130",
    ]

    return calories_list


def get_sleep_list():
    sleep_list = [
        "08:30:00",
        "08:15:00",
        "08:00:00",
        "08:45:00",
        "07:45:00",
    ]

    return sleep_list


def get_alcohol_list():
    alcohol_list = [
        "0",
        "0",
        "0",
        "0",
        "5",
        "7",
    ]

    return alcohol_list


def get_exercise_type_list():
    exercise_type_list = [
        "None",
        "None",
        "Cycling",
        "Running",
        "Walking",
    ]

    return exercise_type_list


def get_exercise_duration_list():
    exercise_duration_list = [
        "32",
        "28",
        "34",
        "40",
        "60",
        "62",
    ]

    return exercise_duration_list


def get_exercise_calories_dict(exercise_duration):
    exercise_calories_dict = {
        "32": "282",
        "28": "265",
        "34": "295",
        "40": "340",
        "60": "552",
        "62": "570",
    }

    exercise_calories = exercise_calories_dict[exercise_duration]

    return exercise_calories


def get_exercise_metres_dict(exercise_type, exercise_duration):
    exercise_metres_dict = {
        "Running": {
            "32": '15',
            "28": "14",
            "34": "16",
            "40": "20",
            "60": "30",
            "62": "31",
        },
        "Cycling": {
            "32": "127",
            "28": "112",
            "34": "131",
            "40": "181",
            "60": "250",
            "62": "257",
        },
        "Walking": {
            "32": "127",
            "28": "112",
            "34": "131",
            "40": "181",
            "60": "250",
            "62": "257",
        },
    }

    exercise_metres_gained = exercise_metres_dict[exercise_type][exercise_duration]

    return exercise_metres_gained


def get_exercise_average_heart_rate_list():
    average_heart_rate_list = [
        "157",
        "163",
        "167",
        "172",
        "159",
        "164"
    ]

    return average_heart_rate_list


def get_mood_score_list():
    mood_score_list = [
        "6",
        "7",
        "5",
        "4",
        "8",
        "7",
    ]

    return mood_score_list


def get_data_file():
    config = get_config_details()
    file = config['health_data_file']['file']
    import_df = pd.read_csv(file)

    return import_df


def get_date_list():
    date_list = [
        "2023-11-20",
        "2023-11-21",
        "2023-11-22",
        "2023-11-23",
        "2023-11-24",
        "2023-11-25",
        "2023-11-26",
        "2023-11-27",
        "2023-11-28",
        "2023-11-29",
    ]

    return date_list


def get_input_dict():
    input_dict = {
        "Date": "-",
        "Weight": "86.6",
        "Calories Consumed": "-",
        "Sleep": "-",
        "Alcohol": "-",
        "Exercise Type": "-",
        "Exercise Duration": "-",
        "Exercise Calories": "-",
        "Exercise Metres Gained": "-",
        "Exercise Average Heart Rate": "-",
        "Mood Score": "-",
    }

    return input_dict


def write_data(import_df, input_dict):

    df_new_row = pd.DataFrame([input_dict])
    import_df = pd.concat([import_df, df_new_row])

    return import_df


def file_write(import_df):
    config = get_config_details()
    target_file = config['health_data_file']['file']

    import_df.to_csv(target_file, encoding="utf-8", index=False)


def return_input_dict(input_dict, date):

    input_dict["Date"] = date
    input_dict["Calories Consumed"] = random.choice(get_calories_list())
    input_dict["Sleep"] = random.choice(get_sleep_list())
    input_dict["Alcohol"] = random.choice(get_alcohol_list())

    exercise_type = random.choice(get_exercise_type_list())
    input_dict["Exercise Type"] = exercise_type

    if exercise_type == "None":
        input_dict["Exercise Duration"] = "0"
        input_dict["Exercise Calories"] = "0"
        input_dict["Exercise Metres Gained"] = "0"
        input_dict["Exercise Average Heart Rate"] = "0"
    else:
        exercise_duration = random.choice(get_exercise_duration_list())
        input_dict["Exercise Duration"] = exercise_duration
        input_dict["Exercise Calories"] = get_exercise_calories_dict(exercise_duration)
        input_dict["Exercise Metres Gained"] = get_exercise_metres_dict(exercise_type, exercise_duration)
        input_dict["Exercise Average Heart Rate"] = random.choice(get_exercise_average_heart_rate_list())

    input_dict["Mood Score"] = random.choice(get_mood_score_list())

    return input_dict


def main():
    date_list = get_date_list()
    import_df = get_data_file()

    for date in date_list:
        input_dict = get_input_dict()
        input_dict = return_input_dict(input_dict, date)
        for key in input_dict:
            print(f"{key}: {input_dict[key]}")

        import_df = write_data(import_df, input_dict)

    file_write(import_df)


if __name__ == "__main__":
    main()
