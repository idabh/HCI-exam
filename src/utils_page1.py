from turtle import fillcolor
from numpy import mat
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
from src.utils import *
import plotly.io as pio
pio.kaleido.scope.default_format = "png"
from random import randint

#bar radar
def radar_bar(data):
    fig = px.bar_polar(data, r='r', theta='theta',color='grey', template='ggplot2', range_r=[0,10], width=600, height=600)
    fig.update_traces(opacity=0.5, selector=dict(type='barpolar')) 
    fig1 = go.Figure(data = fig.data, 
    layout=go.Layout(
        polar={'radialaxis': {'visible': False}},width=500, height=500,
        showlegend=False
        ))
    fig1.update_polars(radialaxis_range=[0,10]) 
    st.write(fig1)

def applicant_match(data, ID, match_data, education_rank, proficiency_rank):
    d = data.loc[data['Name'] == ID]
    
    r=[ d.iloc[0,3]/10,
        education_rank[d.iloc[0,4]]*2,
        proficiency_rank[d.iloc[0,14]]*2,
        d.iloc[0,15],
        d.iloc[0,18]/10]
    theta=['Python Score','Education Level','English Proficiency','GPA', 'SQL Score']
    color = d.iloc[0,19]
    r = [*r, r[0]]
    individual = go.Scatterpolar(r=r, theta=theta, fill='toself', line_color = color, opacity = 0.3,fillcolor= color) 

    r_match = list(match_data['r'])
    r_match = [*r_match, r_match[0]]
    minimum_demand = go.Barpolar(r=r_match, theta=theta, opacity = 0.2)
    
    match_individual = go.Figure(data = [individual, minimum_demand],
        layout=go.Layout(
        polar={'radialaxis': {'visible': False}},width=600, height=600,
        showlegend=False))
    match_individual.update_polars(radialaxis_range=[0,10]) 
    match_individual.write_image((f"Images/{ID}.png").replace(" ", ""))

@st.cache
def create_plots(): 
    image_files=[]
    color_list = []
    n_colors_to_generate = len(list(st.session_state['temp_df']['Name']))
    for i in range(n_colors_to_generate):
        color_list.append('#%06X' % randint(0, 0xFFFFFF))
    
    st.session_state['temp_df']['unique_color'] =color_list
    for applicant in list(st.session_state['temp_df']['Name']):
        applicant_match(st.session_state['temp_df'], applicant, st.session_state['radar_data'], st.session_state['education_rank'],st.session_state['proficiency_rank'])
        image_files.append(f'{(applicant).replace(" ", "")}.png')
    st.session_state['temp_df']['ano_image'] = image_files    
    st.session_state['temp_df']['ID'] = range(1,len(list(st.session_state['temp_df']['Name']))+1)
    st.session_state['temp_df'].to_csv("Data/applicants-from-page-1.csv")