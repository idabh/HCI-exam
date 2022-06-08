import random
from timeit import repeat
from click import progressbar
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.utils import *
from itertools import cycle
import os

#df = pd.read_csv('Data/yes_candidates.csv',na_values=['a','b'])


def page5():
    #load data
    df = st.session_state['output_from_page2']

    if 'invited' not in st.session_state: 
        st.session_state.invited = 0

    #define process bar
    progress3_path = 'Data/progress/progress3.png'
    progress4_path = 'Data/progress/progressdone.png'
    progress3 = "<img src='data:image/png;base64,{}' class='img-fluid' style= 'height:100px; padding-bottom: 30px; padding-left: 100px;'>".format(
        img_to_bytes(progress3_path)
        )
    progress4 = "<img src='data:image/png;base64,{}' class='img-fluid' style= 'height:100px; padding-bottom: 30px; padding-left: 100px;'>".format(
        img_to_bytes(progress4_path)
        ) 

    progressbar = st.empty()
    with progressbar.container():
        st.markdown(progress3, unsafe_allow_html= True)

    #Define columns
    col1, col2,col3 = st.columns(3)
    columns = [col1, col2,col3]

    if len(df) < 1: 
        st.warning('You have not choosen any candidates!')
    if len(df) > 1: 
        #Loop through candidates
        for candidate,ncol in zip(list(df['ano_image']), cycle(columns)): 
            with ncol: 
                current_name = df.loc[df['ano_image']== candidate]
                if current_name.iloc[0,2] == 'female':
                    path="Data/Images/female/"
                    files=os.listdir(path)
                    female_img=random.choice(files)
                    st.image(os.path.join(path,female_img))
                if current_name.iloc[0,2] == 'male':
                    path="Data/Images/male/"
                    files=os.listdir(path)
                    male_img=random.choice(files)
                    st.image(os.path.join(path,male_img))
                
                st.subheader(f'{current_name.iloc[0,0]}')
                st.markdown(f'{current_name.iloc[0,0]} is __{current_name.iloc[0,1]} years old__ and has a __{current_name.iloc[0,4]}__ in __{current_name.iloc[0,5]}__.', unsafe_allow_html=True)
                st.checkbox(f'Invite {current_name.iloc[0,0]} to interview', value=True, key = current_name)

    st.write('')
    col1, col2,col3 = st.columns(3)
    if col2.button('Invite candidates to interview'): 
        st.session_state.invited = 1

    if st.session_state.invited == 1:
        st.success('Sent e-mail invitations to all selected candidates')
        with progressbar.container():
            st.markdown(progress4, unsafe_allow_html= True)
        st.write('')
        st.markdown("<div style = ' position:relative; left:300px; '> <b> Write your email to receive the applicants' full profiles </b></div>", unsafe_allow_html=True)
        input = st.text_input(label = 'Email:')
        if len(input) > 0:
            st.success('The profiles is sent to your e-mail')


#page5()
