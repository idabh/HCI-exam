'''
To pick a color: https://www.w3schools.com/colors/colors_picker.asp
Grid ressource: https://gridbyexample.com/examples/
'''

import streamlit as st
from src.utils import *
from PIL import Image
import numpy as np 
import pandas as pd
from grid import *
import streamlit.components.v1 as components
import csv 
import os.path

#set wide style 
st.set_page_config(layout = "wide")

#define style
local_css("styles.css")

#define data 
candidates = pd.read_csv('Data/applicants250.csv',na_values=['a','b'])
candidates = pd.DataFrame(candidates[0:5])
text_input = [1, len(candidates)]

#define process bar
process_bar = st.progress(50)

#define menu
selected = streamlit_menu(options=["All", "Yes", "Maybe", "No"], icons=["circle", "check-circle", "question-circle", "x-circle"])

#define columns
col1, col2, col3 = st.columns(3)

#initialise session state
rkey_list = [f'radio_{i}' for i in range(0, len(candidates))]
tkey_list = [f'text_{i}' for i in range(0, len(candidates))]

for key in rkey_list: 
    if key not in st.session_state:
        st.session_state[key] = "Not selected"
for key in tkey_list: 
    if key not in st.session_state:
        st.session_state[key] = ""

#define pages
if selected == "All":
    #loop through candidates
    for c in range(0, len(candidates)): 
        #define key for radio 
        radio_key = rkey_list[c]
        text_key = tkey_list[c]

        #redefine session state (because streamlit is stupid)
        st.session_state[radio_key] = st.session_state[radio_key]
        st.session_state[text_key] = st.session_state[text_key]

        #define image
        image = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:300px; position:relative; top:15px;'>".format(
            img_to_bytes('Images/download2.jpg')
            )

        #define info
        Text1 = candidates.iloc[c]['Text1']
        Text2 = candidates.iloc[c]['Text2']

        with col1: 
            st.markdown(image, unsafe_allow_html= True)
            st.write('')
            st.write('')
            st.write('')
            st.write('')
        
        with col2: 
            st.write('')
            st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key=radio_key)
            st.text_input(label = 'Notes', key = text_key)

        with col3: 
            st.markdown(f"<p style = 'position:absolute; top:{c*100+100}px; height: 200px; width: 200px; border: 3px solid #73AD21;'>Text2</p> ", unsafe_allow_html=True)
        
        
if selected == "Yes":
    st.title(f"You have selected {selected}")
    yes_candidates = [int(item[0][-1]) for item in st.session_state.items() if item[1]== 'Yes']
    print(yes_candidates)

    for c in range(0, len(yes_candidates)): 
        #define keys
        radio_key = rkey_list[c]
        text_key = tkey_list[c]

        #load session state
        st.session_state[radio_key] = st.session_state[radio_key]
        st.session_state[text_key] = st.session_state[text_key]

        st.write(st.session_state)

        yes_candidates = candidates.loc[candidates['tag'] == "Yes"]
        st.markdown('hello', unsafe_allow_html=True)

if selected == "Maybe":
    st.title(f"You have selected {selected}")
    for c in range(0, len(candidates)): 
        radio_key = rkey_list[c]
        text_key = tkey_list[c]

        st.title(f"You have selected {selected}")
        yes_candidates = candidates.loc[candidates['tag'] == "Yes"]
        st.markdown('hello', unsafe_allow_html=True)
        #load session state
        st.session_state[radio_key] = st.session_state[radio_key]
        st.session_state[text_key] = st.session_state[text_key]

        st.write(st.session_state)


if selected == "No":
    st.title(f"You have selected {selected}")
    st.write(st.session_state)

