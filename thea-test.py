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
import plotly.offline as pyo

df = pd.read_csv('/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/Data/applicants-from-page-1.csv')
education_rank = {"high school":1, "bachelor":2, "masters":3, "phd":4, "postdoc":5}
df = df.iloc[:3,]

def applicant_compare(data, individual, color):
    d = data.loc[data['Name'] == individual]
    r=[ d.iloc[0,4]/10,
        education_rank[d.iloc[0,5]]*2,
        d.iloc[0,15]/5,
        d.iloc[0,16],
        d.iloc[0,9]/5]
    theta=['python skills','education_level','factor1',
        'factor2', 'experience']
    color = d.iloc[0,18]
    r = [*r, r[0]]
    individual = go.Scatterpolar(r=r, theta=theta, fill='toself',name=individual, line_color = color,opacity = 0.2,fillcolor= color) 
    return individual

compare_these = list(df['Name'])
individual1 = applicant_compare(df,compare_these[0])
individual2 = applicant_compare(df,compare_these[1])
individual3 = applicant_compare(df,compare_these[2])

match_individual = go.Figure(data=[individual1,individual2,individual3],
layout=go.Layout(polar={'radialaxis': {'visible': False}},width=600, height=600,showlegend=True))
match_individual.update_polars(radialaxis_range=[0,10]) 

st.write(match_individual)



'''
def applicant_match(data, ID, match_data, education_rank):
    d = data.loc[data['Name'] == ID]
    app_data = pd.DataFrame(dict(
    r=[ d.iloc[0,3]/10,
        education_rank[d.iloc[0,4]]*2,
        d.iloc[0,14]/5,
        d.iloc[0,15],
        d.iloc[0,8]/5],
    theta=['python skills','education_level','factor1',
        'factor2', 'experience'],
    color = ["blue","blue","blue","blue","blue"]))
    individual = px.line_polar(app_data, r='r', theta='theta', line_close=True, template='ggplot2', color= "color", range_r=[0,10],width=600, height=600)
    r = [*app_data['r'], app_data['r'][0]]
    #individual = go.Scatterpolar(r=list(app_data['r']), theta=list(app_data['theta']), fill='toself', line_color = color, opacity = 0.2,fillcolor= color) 
    individual.update_traces(fill='toself')
    #if we want to change colors, look at Scatterpolar
    
    minimum_demand = px.bar_polar(match_data, r='r', theta='theta',color='color', template='ggplot2', range_r=[0,10],width=600, height=600)
    minimum_demand.update_traces(opacity=0.5, selector=dict(type='barpolar')) 

    match_individual = go.Figure(data = individual.data + minimum_demand.data,
        layout=go.Layout(
        polar={'radialaxis': {'visible': False}},width=600, height=600,
        showlegend=False))
    match_individual.update_polars(radialaxis_range=[0,10]) 
    match_individual.write_image((f"Images/{ID}.png").replace(" ", ""))
'''