#Page 1
import random
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.utils import *

#PAGE SETUP #######################################################
#from streamlit_option_menu import option_menu
st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
# Remove whitespace from the top of the page and sidebar
st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
#condense the space
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

#define style
local_css("/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/styles.css")

########################

#load data
df = pd.read_csv('/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/Data/applicants200.csv')
education_rank = {"high school":1, "bachelor":2, "masters":3, "phd":4, "postdoc":5}

# DEFINE SIDEBAR #####################
with st.sidebar:
    st.title("STEP 1: Screening")
    st.header("Filters")
    #st.markdown("Narrow down the applicants by manipulating the filters below")
    
    education_level = st.select_slider("Minimum education level", options=["high school", "bachelor", "masters", "phd", "postdoc"],  help="choose minimum education level needed for this position")
        
    python_skills = st.slider("Python skills", min_value=0, max_value=100, value=0, step=1, format=None,  help="The performances of the candidates ", on_change=None, args=None, kwargs=None,  disabled=False)

    fac1 = st.slider('Select value fac1', 0,10,1)
    fac2 = st.slider('Select value fac2',0,10,1)
    
    exp = st.slider("Years exp", min_value=0, max_value=50, value=0, step=1, format=None,  help="The performances of the candidates ", on_change=None, args=None, kwargs=None,  disabled=False)
    #exp_needed = st.radio("Experience", options= ["Yes", "No"])
    
    #academic_prof = st.multiselect("Academic profile", options=["sciences", "engineering", "arts"], default=["sciences", "engineering", "arts"], key=None, help="Check all the relevant profiles for this position", on_change=None, args=None, kwargs=None, disabled=False)


#process bar
process_bar = st.progress(25)

#chosen applicants
temp_df = df.loc[
    (df['Python_score'] >= python_skills) & 
    (df['Years_experience'] >= exp) & 
    (df['Education_level'].isin([k for k in education_rank.keys() if education_rank[k] >= education_rank[education_level]]))
    ]

#count of remaining applicants

remaining_app = len(temp_df)
diff_app = f"{(remaining_app)-(len(df))} applicants since initial something"
counting = f'<div data-testid="stMetricValue" class="css-1xarl3l e16fv1kl2"> <div class="css-1ht1j8u e16fv1kl0"> <span style="font-size:20px;"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are  &nbsp;&nbsp;</span> <span <h1 style="text-align: center;font-size:100px;">  {remaining_app} </h1> </span><span style="font-size:20px;">applicants remaining</span></div></div>'
st.markdown(counting, unsafe_allow_html=True)

#RADAR##############################################################################################

radar_data = pd.DataFrame(dict(
    r=[python_skills/10,
       education_rank[education_level]*2,
       fac1,
       fac2,
       exp/5],
    theta=['python skills','education_level','factor1',
           'factor2', 'experience'],
    color = ["#E4FF87", '#709BFF', '#719BFF', '#FFAA70', '#B6FFB4']
    ))

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

radar_bar(radar_data)

def applicant_match(data, ID, match_data):
    
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
    
    minimum_demand = px.bar_polar(match_data, r='r', theta='theta',color='color', template='ggplot2', range_r=[0,10],width=600, height=600)
    minimum_demand.update_traces(opacity=0.5, selector=dict(type='barpolar')) 

    match_individual = go.Figure(data = individual.data + minimum_demand.data,
        layout=go.Layout(
        polar={'radialaxis': {'visible': False}},width=600, height=600,
        showlegend=False
    ))
    match_individual.update_polars(radialaxis_range=[0,10]) 
    #st.write(match_individual)
    match_individual.write_image((f"Images/{ID}.png").replace(" ", ""))
    
    
#applicant_match(ID, radar_data)
#show data frame
#st.dataframe(data=temp_df, width=None, height=None)

#BUTTON##############################################################################################
_, _, _, _, _, _, _, _, _, col10 = st.columns(10)



with col10: 
    if st.button('   Next   '):
        for applicant in list(temp_df['Name']):
            applicant_match(temp_df, applicant, radar_data)
            st.write(applicant)
            temp_df[temp_df.Name == applicant, "Image"] = (f"Images/{applicant}.png").replace(" ", "")
        st.markdown(f"writing csv for {len(temp_df)} applicants")
            
        temp_df.to_csv("Data/applicants-from-page-1.csv")

#st.balloons()
#st.snow()

#def radar_chart(data):  
#    fig = px.line_polar(data, r='r', theta='theta', line_close=True, template='ggplot2', range_r=[0,10], #width=600, height=600)
#    st.write(fig)
#radar_chart(radar_data)
