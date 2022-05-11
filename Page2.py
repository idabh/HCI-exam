import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd 

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 2

pd.read_csv('Data/applicants250.csv',na_values=['a','b']) # a and b values will be treated as NaN after importing into dataframe.

def streamlit_menu(example=1):
    if example == 2:
            # 2. horizontal menu w/o custom style
            selected = option_menu(
                menu_title=None,  # required
                options=["All", "Yes", "Maybe", "No"],  # required
                icons=["circle", "check-circle", "question-circle", "x-circle"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                orientation="horizontal",
                styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                    #"icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {
                    #    "font-size": "25px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {"background-color": 'darkgrey'},
                }
            )
            return selected

selected = streamlit_menu(example=EXAMPLE_NO)
if selected == "All":
    st.title(f"You have selected {selected}")

if selected == "Yes":
    st.title(f"You have selected {selected}")

if selected == "Maybe":
    st.title(f"You have selected {selected}")
if selected == "No":
    st.title(f"You have selected {selected}")