import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
from src.utils import *
import plotly.io as pio
pio.kaleido.scope.default_format = "png"

#bar radar
def radar_bar(data):
    fig = px.bar_polar(data, r='r', theta='theta',color='color', template='ggplot2', range_r=[0,10], width=600, height=600)
    fig.update_traces(opacity=0.5, selector=dict(type='barpolar')) 
    fig1 = go.Figure(data = fig.data, 
    layout=go.Layout(
        polar={'radialaxis': {'visible': False}},width=700, height=700,
        showlegend=False
        ))
    fig1.update_polars(radialaxis_range=[0,10]) 
    st.write(fig1)

def applicant_match(data, ID, match_data, education_rank):
    d = data.loc[data['Name'] == ID]
    app_data = pd.DataFrame(dict(
    r=[ d.iloc[0,3]/10,
        education_rank[d.iloc[0,4]]*2,
        d.iloc[0,14]/5,
        d.iloc[0,15],
        d.iloc[0,8]/5],
    theta=['python skills','education_level','factor1',
        'factor2', 'experience']))
    individual = px.line_polar(app_data, r='r', theta='theta', line_close=True, template='ggplot2', range_r=[0,10],width=600, height=600)
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
