'''
To pick a color: https://www.w3schools.com/colors/colors_picker.asp
Grid ressource: https://gridbyexample.com/examples/
'''

import streamlit as st
from src.utils import *
from PIL import Image
import numpy as np 
import pandas as pd
import csv 
import os.path
from elgiganten_view import * 
from src.utils_page2 import * 

st.set_page_config(layout="wide",page_title="ScreenAid", page_icon="🔍")
candidates = pd.read_csv('Data/applicants-from-page-1.csv',na_values=['a','b'])
local_css("styles.css")

def page2(): 
    #candidates = st.session_state.temp_df

    
    #initialise session state
    rkey_list = [f'radio_{i}' for i in range(0, len(candidates))]
    tkey_list = [f'text_{i}' for i in range(0, len(candidates))]
    ckey_list = [f'compare_{i}' for i in range(0, len(candidates))]

    for key in rkey_list: 
        if key not in st.session_state:
            st.session_state[key] = "Not selected"
        else: 
            st.session_state[key] = st.session_state[key]
    for key in tkey_list: 
        if key not in st.session_state:
            st.session_state[key] = ""
        else:
            st.session_state[key] = st.session_state[key]
    for key in ckey_list: 
        if key not in st.session_state:
            st.session_state[key] = False
        else:
            st.session_state[key] = st.session_state[key]

    for candidate in ['no_yes_candidates', 'no_maybe_candidates', 'no_no_candidates']:
        if candidate not in st.session_state: 
            st.session_state[candidate] = 0
        else: 
            st.session_state[candidate] = st.session_state[candidate]

    #Define comparison: 
    compare_candidates = [key for key, value in st.session_state.items() if 'compare_' in key and value == True]

    #define process bar
    progress2_path = 'Data\progress\progress2.png'
    progress2 = "<img src='data:image/png;base64,{}' class='img-fluid' style= 'padding-bottom: 30px; padding-left: 260px;'>".format(
        img_to_bytes(progress2_path)
        ) 
    st.markdown(progress2, unsafe_allow_html= True)


    #Add comparison
    with st.expander("Compare candidates"):
        elgiganten_view(candidates, compare_candidates)

    if len(compare_candidates) > 3:
        st.warning('You can only compare 3 candidates at the time!')

    #define menu
    placeholder2 = st.empty()
    with placeholder2.container():
        selected = streamlit_menu(options=[f'All ({len(candidates)})', f'Yes ({st.session_state.no_yes_candidates})', f'Maybe ({st.session_state.no_maybe_candidates})', f'No ({st.session_state.no_no_candidates})'], icons=["circle", "check-circle", "question-circle", "x-circle"], key = 'original')

    #define columns
    col1, col2, col3, col4 = st.columns(4)

    #define candidates
    yes_candidates = [int(item[0][-1]) for item in st.session_state.items() if  'radio_' in item[0] and item[1]== 'Yes']
    st.session_state['no_yes_candidates'] = len(yes_candidates)
    maybe_candidates = [int(item[0][-1]) for item in st.session_state.items() if 'radio_' in item[0] and item[1]== 'Maybe']
    st.session_state['no_maybe_candidates'] = len(maybe_candidates)
    no_candidates = [int(item[0][-1]) for item in st.session_state.items() if  'radio_' in item[0] and item[1]== 'No']
    st.session_state['no_no_candidates'] = len(no_candidates)

    #define pages
    if selected == f'All ({len(candidates)})':
        #loop through candidates
        for c in range(0, len(candidates)): 
            #show page
            show_page2(ckey_list, rkey_list, tkey_list, index = c, df = candidates)   
            st.write('---')
    
    if selected == f'Yes ({st.session_state.no_yes_candidates})':
        #loop through candidates
        for c in yes_candidates: 
            #show page
            show_page2(ckey_list, rkey_list, tkey_list, index = c, df = candidates)   
            st.write('---')

    if selected == f'Maybe ({st.session_state.no_maybe_candidates})':
        #loop through candidates
        for c in maybe_candidates: 
            #show page
            show_page2(ckey_list, rkey_list, tkey_list, index = c, df = candidates)   
            st.write('---')

    if selected == f'No ({st.session_state.no_no_candidates})':
        #loop through candidates 
        for c in no_candidates: 
            #show page
            show_page2(ckey_list, rkey_list, tkey_list, index = c, df = candidates)
            st.write('---')

    
    st.session_state.yes_candidates = yes_candidates

    #update menu
    placeholder2.empty()
    with placeholder2.container():
        streamlit_menu(options=[f'All ({len(candidates)})', f'Yes ({st.session_state.no_yes_candidates})', f'Maybe ({st.session_state.no_maybe_candidates})', f'No ({st.session_state.no_no_candidates})'], icons=["circle", "check-circle", "question-circle", "x-circle"], key = 'updated')


page2()
