#Page 1
import random
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.utils import *
import plotly.io as pio
pio.kaleido.scope.default_format = "png"

#PAGE SETUP #######################################################

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

    fac1 = st.slider('Select value fac1', 0,50,1)
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
    (df['Education_level'].isin([k for k in education_rank.keys() if education_rank[k] >= education_rank[education_level]])) &
    ((df['factor1'] >= fac1)) &
    ((df['factor2'] >= fac2))
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
       fac1/5,
       fac2,
       exp/5],
    theta=['python skills','education_level','factor1','factor2', 'experience'],
    color = ["#E4FF87", '#709BFF', '#719BFF', '#FFAA70', '#B6FFB4']))

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
        showlegend=False))
    match_individual.update_polars(radialaxis_range=[0,10]) 
    match_individual.write_image((f"/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/Images/{ID}.png").replace(" ", ""))
    
#show data frame
#st.dataframe(data=temp_df, width=None, height=None)

#BUTTON##############################################################################################
_, _, _, _, _, _, _, _, _, col10 = st.columns(10)

image_files=[]
with col10: 
    if st.button('   Next   '):
        for applicant in list(temp_df['Name']):
            applicant_match(temp_df, applicant, radar_data)
            st.write(applicant)
            image_files.append(f'{(applicant).replace(" ", "")}.png')
        temp_df['image'] = image_files    
        temp_df.to_csv("Data/applicants-from-page-1.csv")

#st.balloons()
#st.snow()