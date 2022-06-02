'''
Ida testing page session state things
'''
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#
def streamlit_menu():
    selected = option_menu(
        menu_title=None,  # required
        options=["Home", "Counter", "Contact"],  # required
        icons=["house", "book", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected


selected = streamlit_menu()

if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Counter":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")