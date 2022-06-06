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

def applicant_match(data, individual, color):
    d = data.loc[data['Name'] == individual]
    app_data = pd.DataFrame(dict(
    r=[ d.iloc[0,4]/10,
        education_rank[d.iloc[0,5]]*2,
        d.iloc[0,15]/5,
        d.iloc[0,16],
        d.iloc[0,9]/5],
    theta=['python skills','education_level','factor1',
        'factor2', 'experience'],
    color = [color, color, color, color, color]))
    individual = px.line_polar(app_data, r='r', theta='theta', line_close=True, template='ggplot2', range_r=[0,10],width=600, height=600,color="color")
    individual.update_traces(fill='toself')
    return individual
    #match_individual.write_image((f"/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/Images/{individual}.png").replace(" ", ""))


compare_these = list(df['Name'])
individual1 = applicant_match(df,compare_these[0], 'red')
individual2 = applicant_match(df,compare_these[1], 'blue')
individual3 = applicant_match(df,compare_these[2], 'green')

match_individual = go.Figure(data = individual1.data+individual2.data+individual3.data,
layout=go.Layout(polar={'radialaxis': {'visible': False}},width=600, height=600,showlegend=True))
match_individual.update_polars(radialaxis_range=[0,10]) 

st.write(match_individual)



import plotly.graph_objects as go
import plotly.offline as pyo


categories = ['python skills','education_level','factor1','factor2', 'experience']
categories = [*categories, categories[0]]

restaurant_1 = [4, 4, 5, 4, 3]
restaurant_2 = [5, 5, 4, 5, 2]
restaurant_3 = [3, 4, 5, 3, 5]
restaurant_1 = [*restaurant_1, restaurant_1[0]]
restaurant_2 = [*restaurant_2, restaurant_2[0]]
restaurant_3 = [*restaurant_3, restaurant_3[0]]


fig = go.Figure(
    data=[
        go.Scatterpolar(r=restaurant_1, theta=categories, fill='toself', name='Restaurant 1'),
        go.Scatterpolar(r=restaurant_2, theta=categories, fill='toself', name='Restaurant 2'),
        go.Scatterpolar(r=restaurant_3, theta=categories, fill='toself', name='Restaurant 3')
    ],
    layout=go.Layout(
        title=go.layout.Title(text='Restaurant comparison'),
        polar={'radialaxis': {'visible': True}},
        showlegend=True
    )
)
