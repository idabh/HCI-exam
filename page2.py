'''
To pick a color: https://www.w3schools.com/colors/colors_picker.asp
Grid ressource: https://gridbyexample.com/examples/
'''

from xml.dom.xmlbuilder import Options
import streamlit as st
from src.utils import *
from PIL import Image
import numpy as np 
import pandas as pd
import csv 
import os.path
from elgiganten_view import * 
from src.utils_page2 import * 

#st.set_page_config(layout="wide",page_title="ScreenAid", page_icon="🔍")
#candidates = pd.read_csv('Data/applicants-from-page-1.csv',na_values=['a','b'])

def page2(): 
    candidates = st.session_state.temp_df2

    #define candidates
    IDs = [candidate.replace(' ', '') for candidate in candidates['ID']]
    candidates['IDs'] = [candidate.replace(' ', '') for candidate in candidates['ID']]

    #initialise session state
    rkey_list = [f'radio_{i}' for i in IDs]
    tkey_list = [f'text_{i}' for i in IDs]
    #ckey_list = [f'compare_{i}' for i in IDs]
    ckey_list = [f'compare_{i}' for i in range(0, len(candidates))] # with index instead of ID again!

    #reload session states
    for key in st.session_state: 
        st.session_state[key] = st.session_state[key]

    for key in rkey_list + tkey_list + ckey_list: 
        if key not in st.session_state and 'radio_' in key:
            st.session_state[key] = "Not selected"
        elif key not in st.session_state and 'text_' in key:
            st.session_state[key] = ""
        elif key not in st.session_state and 'compare_' in key:
            st.session_state[key] = False
        else: 
            st.session_state[key] = st.session_state[key]

    #Define comparison: 
    compare_candidates = [key for key, value in st.session_state.items() if 'compare_' in key and value == True]

    # columns for progress bar and info icon
    c1,c2 = st.columns([25,1])

    # progress bar
    with c1:
        progress2_path = 'Data/progress/progress2.png'
        progress2 = "<img src='data:image/png;base64,{}' class='img-fluid' style= 'height:100px; padding-bottom: 30px; padding-left: 240px;'>".format(
            img_to_bytes(progress2_path)
            ) 
        st.markdown(progress2, unsafe_allow_html= True)

    # help button
    help_p2 = '''
    STEP 2: COMPARE & SORT\n
    Learn more about your applicants by reading their profiles. Each profile picture is the applicant’s skill plot overlaid on your thresholds from Step 1. Use the radio buttons to sort applicants into ‘yes’, ‘maybe’, and ‘no’ piles as you go. You can navigate the piles by clicking at the tabs at the top. You can also write notes to yourself about each applicant. Click the ‘+’ icon below an applicant to read their motivational letter.\n
    To compare 2-3 applicants, check the ‘Compare’ box next to each of them and click the ‘+’ icon next to ‘Compare candidates’ at the top of the page. To the left, you can compare their skill plots (click on a name to toggle on and off). To the right, you can compare their information in a table.\n
    When you press ‘Next’, all applicants in the ‘yes’ pile are chosen and will be revealed in the final step.

    '''
    with c2:
        st.download_button(label='?',data='blabla',help=help_p2,disabled=True)

    #Add comparison
    with st.expander("Compare candidates"):
        elgiganten_view(candidates, compare_candidates)

    if len(compare_candidates) > 3:
        st.warning('You can only compare 3 candidates at a time!')
    
    if 'selected' not in st.session_state: 
        st.session_state.selected = f'All ({len(candidates)})'

    #define menu place
    menu = st.container()
    menu_box = menu.empty()

    #define columns
    col1, col2, col3, col4 = st.columns(4)

    #define candidates
    st.session_state.yes_candidates = [str(item[0]).partition("_")[2] for item in st.session_state.items() if  'radio_' in item[0] and item[1]== 'Yes']
    st.session_state.maybe_candidates = [str(item[0]).partition("_")[2] for item in st.session_state.items() if 'radio_' in item[0] and item[1]== 'Maybe']
    st.session_state.no_candidates = [str(item[0]).partition("_")[2] for item in st.session_state.items() if  'radio_' in item[0] and item[1]== 'No']

    #define indexes for candidates
    st.session_state.yes_indexes = [int(IDs.index(i)) for i in st.session_state.yes_candidates]
    st.session_state.maybe_indexes = [int(IDs.index(i)) for i in st.session_state.maybe_candidates]
    st.session_state.no_indexes = [int(IDs.index(i)) for i in st.session_state.no_candidates]

    #sort candidates
    #candidates['index_column'] = 0

#    for i in candidates['IDs'].index:
#        if candidates['IDs'][i] in st.session_state.yes_candidates:
#            candidates['index_column'][i] = 1 
#        elif candidates['IDs'][int(i)] in st.session_state.maybe_candidates:
#            candidates['index_column'][i] = 2 
#        elif candidates['IDs'][int(i)] in st.session_state.no_candidates:
#            candidates['index_column'][i] = 3

#    candidates = candidates.sort_values('index_column')


    #show pages
    if st.session_state.selected.partition(" ")[0] == 'All':
        #loop through candidates
        for c in range(0, len(candidates)): 
            #show page
            show_page2(ckey_list, rkey_list, tkey_list, index = c, df = candidates)   
            st.write('---')
        

    if st.session_state.selected.partition(" ")[0] == 'Yes':
        #loop through candidates
        for c in st.session_state.yes_indexes: 
            #show page
            show_page2(ckey_list, rkey_list, tkey_list, index = c, df = candidates)   
            st.write('---')

    if st.session_state.selected.partition(" ")[0] == 'Maybe':
        #loop through candidates
        for c in st.session_state.maybe_indexes: 
            #show page
            show_page2(ckey_list, rkey_list, tkey_list, index = c, df = candidates)   
            st.write('---')

    if st.session_state.selected.partition(" ")[0] == 'No':
        #loop through candidates 
        for c in st.session_state.no_indexes: 
            #show page
            show_page2(ckey_list, rkey_list, tkey_list, index = c, df = candidates)
            st.write('---')


    #save number of candidates
    st.session_state['no_yes_candidates'] = len(st.session_state.yes_candidates)
    st.session_state['no_maybe_candidates'] = len(st.session_state.maybe_candidates)
    st.session_state['no_no_candidates'] = len(st.session_state.no_candidates)

    #define menu
    options = [f'All ({len(candidates)})', f'Yes ({st.session_state.no_yes_candidates})', f'Maybe ({st.session_state.no_maybe_candidates})', f'No ({st.session_state.no_no_candidates})']
    options_short = ['All', 'Yes', 'Maybe', 'No']
    with menu_box.container(): 
        streamlit_menu(options=options, icons=["circle", "check-circle", "question-circle", "x-circle"], key = 'selected', default_index=options_short.index(st.session_state.selected.partition(" ")[0]))

#page2()
