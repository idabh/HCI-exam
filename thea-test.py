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
'''
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
'''
def applicant_match(data, individual, color):
    d = data.loc[data['Name'] == individual]
    
    r=[ d.iloc[0,4]/10,
        education_rank[d.iloc[0,5]]*2,
        d.iloc[0,15]/5,
        d.iloc[0,16],
        d.iloc[0,9]/5]
    theta=['python skills','education_level','factor1',
        'factor2', 'experience']
    r = [*r, r[0]]
    individual = go.Scatterpolar(r=r, theta=theta, fill='toself',name=individual, line_color = color,opacity = 0.2,fillcolor= color) 
    
    return individual
    #match_individual.write_image((f"/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/Images/{individual}.png").replace(" ", ""))

compare_these = list(df['Name'])
individual1 = applicant_match(df,compare_these[0], "orange")
individual2 = applicant_match(df,compare_these[1], "red")
individual3 = applicant_match(df,compare_these[2], "yellow")

match_individual = go.Figure(data=[individual1,individual2,individual3],
layout=go.Layout(polar={'radialaxis': {'visible': False}},width=600, height=600,showlegend=True))
match_individual.update_polars(radialaxis_range=[0,10]) 

st.write(match_individual)