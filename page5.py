import random
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.utils import *
from itertools import cycle

#set wide style 
st.set_page_config(layout = "wide")

#define style
local_css("/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/styles.css")

#load yes candidates - for now I just take the ones from page 1
#load data
df = pd.read_csv('/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/Data/applicants-from-page-1.csv')

#Add title
st.markdown("<h1 style='text-align: center;'>STEP 3: Here are your candidates</h1>", unsafe_allow_html=True)

#define process bar
process_bar = st.progress(100)

st.balloons()

col1, col2,col3 = st.columns(3)
columns = [col1, col2,col3]
#for candidate,ncol in list(df['ano_image']):
for candidate,ncol in zip(list(df['ano_image']), cycle(columns)): 
    with ncol: 
        st.image('/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/Data/Images/download2.jpg')
        #st.image(f'/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/Images/{candidate}')
        current_name = df.loc[df['ano_image']== candidate]

        st.subheader(f'{current_name.iloc[0,1]}:')
        
        st.markdown(f'{current_name.iloc[0,1]} is __{current_name.iloc[0,2]} years old__ and has a __{current_name.iloc[0,5]}__ in __{current_name.iloc[0,6]}__.', unsafe_allow_html=True)
        

st.markdown(f'<div class="box-3"><div class="btn btn-one"><span>INVITE CANDIDATES TO INTERVIEW</span></div></div>', unsafe_allow_html=True)