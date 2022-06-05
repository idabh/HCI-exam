#Page 1
import random
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.utils import *
from src.utils_page1 import * 
import plotly.io as pio
pio.kaleido.scope.default_format = "png"

def page1():
    #load data
    df = pd.read_csv('Data/applicants200.csv')
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
    counting = f'<div data-testid="stMetricValue" class="css-1xarl3l e16fv1kl2"> <div class="css-1ht1j8u e16fv1kl0"> <span style="font-size:20px;"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are  &nbsp;&nbsp;</span> <span <h1 style="text-align: center;font-size:100px;">  {remaining_app} </h1> </span><span style="font-size:20px;">applicants remaining</span> </div></div>'
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

    radar_bar(radar_data)

        
    #show data frame
    #st.dataframe(data=temp_df, width=None, height=None)

    #BUTTON##############################################################################################
    col1, _, _, _, _, _, col7, col8, _, col10 = st.columns(10)
    with col1:
        if st.button ('+joker', help='Click here to add a joker/wildcard to the full pool of applicants that does not meet the requirements you set'):
            wildcard = df.sample()
            
            st.info('added a wildcard')

    return temp_df, radar_data, education_rank

    #page1()