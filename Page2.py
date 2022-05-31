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



def update_first():
    st.session_state.second = st.session_state.first


if selected == "All":
    for c in range(0, len(candidates)): 

    #save session state
        if f'notes{c}' not in st.session_state:
            st.session_state.notes = ''

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
            tag = st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key=c, index = 0)
            st.session_state.notes = st.text_input(label = 'Noter', key = c)


        with col3: 
            st.markdown(f"<p style = 'position:absolute; top:{c*100+100}px; height: 200px; width: 200px; border: 3px solid #73AD21;'>Text2</p> ", unsafe_allow_html=True)
        
        #save tag
        if tag != 'Not selected': 
            candidates.at[c, 'tag'] = tag

        
if selected == "Yes":
    st.title(f"You have selected {selected}")
    yes_candidates = candidates.loc[candidates['tag'] == "Yes"]
    st.markdown('hello', unsafe_allow_html=True)
    





if selected == "Maybe":
    st.title(f"You have selected {selected}")
if selected == "No":
    st.title(f"You have selected {selected}")


