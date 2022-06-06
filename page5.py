import random
from timeit import repeat
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.utils import *
from itertools import cycle


def page5():
    #load data
    df = pd.read_csv('Data/yes_candidates.csv')

    #Add title
    st.markdown("<h1 style='text-align: center;'>STEP 3: Here are your candidates</h1>", unsafe_allow_html=True)

    #define process bar
    process_bar = st.progress(100)

    #Define columns
    col1, col2,col3 = st.columns(3)
    columns = [col1, col2,col3]

    if len(df) < 1: 
        st.warning('You have not choosen any candidates!')
    if len(df) > 1: 
        #Loop through candidates
        for candidate,ncol in zip(list(df['ano_image']), cycle(columns)): 
            with ncol: 
                st.image('Data/Images/download2.jpg')
                current_name = df.loc[df['ano_image']== candidate]
                st.subheader(f'{current_name.iloc[0,2]}')
                st.markdown(f'{current_name.iloc[0,2]} is __{current_name.iloc[0,3]} years old__ and has a __{current_name.iloc[0,6]}__ in __{current_name.iloc[0,7]}__.', unsafe_allow_html=True)
                invite = st.checkbox(f'Invite {current_name.iloc[0,2]} to interview', value=True)

        if st.button(' INVITE CANDIDATES TO INTERVIEW '):
            st.success('Sent e-mail invitations to all selected')

        st.subheader(f'{current_name.iloc[0,1]}:')
        
        st.markdown(f'{current_name.iloc[0,1]} is __{current_name.iloc[0,2]} years old__ and has a __{current_name.iloc[0,5]}__ in __{current_name.iloc[0,6]}__.', unsafe_allow_html=True)

        invite = st.checkbox(f'Invite {current_name.iloc[0,1]} to interview', value=True)

    with col2:
        if st.button(' INVITE CANDIDATES TO INTERVIEW '):
            st.success('Sent e-mail invitations to all selected')