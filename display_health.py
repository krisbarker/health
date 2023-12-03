#!/usr/bin/env python3

"""
This is the first attempt at display health
"""

import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px

from genericmodules.get_config import get_config_details


def get_input_data():
    config = get_config_details()
    target_file = config['health_data_file']['file']

    input_data = pd.read_csv(target_file)

    return input_data


def get_activity_list():
    activity_list = [
        "None",
        "Cycling",
        "Running",
        "Walking"
    ]

    return activity_list


def get_region_list(device, input_data):

    region_df = input_data.loc[input_data["Device Name"] == device]
    region_list = region_df["Region"].unique()

    return region_list, region_df


def get_page_list(region_choice, region_df):

    page_df = region_df.loc[region_df["Region"] == region_choice]
    page_list = page_df["Page"].unique()

    return page_list, page_df


def page_build():

    with st.sidebar:
        st.sidebar.title(':blue[Selection Panel]')

        st.write("---")
        activity_choice = st.radio(
            "Customer to view:",
            (activity for activity in get_activity_list()))

        st.write('You selected', activity_choice)

    tab1, tab2, tab3 = st.tabs(["Graph", "% Table", "Values Table"])

    with tab1:
        # st.write('This is some random text for Tab 1')
        col1, col2 = st.columns(2)
        with col1:
            st.subheader(":blue[Cycling Days in the last Week]")
            st.header(":green[4]")
        with col2:
            st.subheader(":rainbow[Cycling Days in the 30 days]")
            st.header(":green[19]")

    with tab2:
        st.write('This is some random text for Tab 2')

    with tab3:
        st.write('This is some random text for Tab 3')


def write_data(export_data, row_entry_data):
    """
    :param export_data:
    :param row_entry_data:
    :return:
    """
    df_new_row = pd.DataFrame([row_entry_data])
    export_data = pd.concat([export_data, df_new_row])

    return export_data


def main():

    page_build()


if __name__ == "__main__":
    main()
