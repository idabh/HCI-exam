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

#st.balloons()

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

        invite = st.checkbox(f'Invite {current_name.iloc[0,1]} to interview', value=True)

with col2:
    if st.button(' INVITE CANDIDATES TO INTERVIEW '):
        st.success('Sent e-mail invitations to all selected')



df = pd.read_csv('/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/Data/applicants-from-page-1.csv')
education_rank = {"high school":1, "bachelor":2, "masters":3, "phd":4, "postdoc":5}
df = df.iloc[:3,]

def applicant_match(data):
    for individual in list(df['Name']):
        print(individual)
        d = data.loc[data['Name'] == individual]
        app_data = pd.DataFrame(dict(
        r=[ d.iloc[0,4]/10,
            education_rank[d.iloc[0,5]]*2,
            d.iloc[0,15]/5,
            d.iloc[0,16],
            d.iloc[0,9]/5],
        theta=['python skills','education_level','factor1',
            'factor2', 'experience']))
        individual = px.line_polar(app_data, r='r', theta='theta', line_close=True, template='ggplot2', range_r=[0,10],width=600, height=600)
        individual.update_traces(fill='toself')
        #if we want to change colors, look at Scatterpolar

    match_individual = go.Figure(data = individual.data,
        layout=go.Layout(
        polar={'radialaxis': {'visible': False}},width=600, height=600,showlegend=False))
    match_individual.update_polars(radialaxis_range=[0,10]) 

    st.write(match_individual)
    #match_individual.write_image((f"/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/Images/{individual}.png").replace(" ", ""))

applicant_match(df)