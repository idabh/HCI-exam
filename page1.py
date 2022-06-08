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
    
    c1,c2 = st.columns([20,5])    
    #load data
    df = pd.read_csv('Data/applicants200.csv')
    education_rank = {"High School":1, "Bachelor":2, "Masters":3, "Ph.d.":4, "Postdoc":5}
    proficiency_rank = {"No Proficiency":1, "Limited":2, "Professional":3, "Advanced":4, "Native":5}

    # DEFINE SIDEBAR #####################
    with st.sidebar:
        st.image('logo.png')
        #st.title("STEP 1: Screening")
        #st.header("Filters")
        #st.markdown("Narrow down the applicants by manipulating the filters below")
        st.expander
        education_level = st.select_slider("Education level", options=["High School", "Bachelor", "Masters", "Ph.d.", "Postdoc"],  help="Choose minimum education level needed")
            
        python_skills = st.slider("Python test score", min_value=0, max_value=100, value=0, step=1, format=None,  help="The performances of the candidates on the python test", on_change=None, args=None, kwargs=None,  disabled=False)

        sql = st.slider("SQL test score", min_value=0, max_value=100, value=0, step=1, format=None,  help="The performances of the candidates on the SQL test", on_change=None, args=None, kwargs=None,  disabled=False)
        
        grade = st.slider('GPA', 0,10,0)
        english = st.select_slider('English Proficiency', options=["No Proficiency", "Limited", "Professional", "Advanced", "Native"],  help="Choose minimum English proficiency level needed")
        
        #academic_prof = st.multiselect("Academic profile", options=["sciences", "engineering", "arts"], default=["sciences", "engineering", "arts"], key=None, help="Check all the relevant profiles for this position", on_change=None, args=None, kwargs=None, disabled=False)

    #process bar
    #st.image('progress1.png')

    #chosen applicants
    temp_df = df.loc[
        (df['Python Score'] >= python_skills) & 
        (df['SQL Score'] >= sql) & 
        (df['Education Level'].isin([k for k in education_rank.keys() if education_rank[k] >= education_rank[education_level]])) &
        (df['English Proficiency'].isin([k for k in proficiency_rank.keys() if proficiency_rank[k] >= proficiency_rank[english]])) &
        ((df['GPA'] >= grade))
        ]

    #count of remaining applicants
    remaining_app = len(temp_df)

    counting = f'<div data-testid="stMetricValue" class="css-1xarl3l e16fv1kl2"> <div class="css-1ht1j8u e16fv1kl0"> <span <h1 style="text-align: center;font-size:80px;"> <br><br> {remaining_app} </h1> </span><span style="font-size:14px;"><br> applicants remaining</span> </div></div>'
    with c2:
        st.markdown(counting, unsafe_allow_html=True)

    #RADAR##############################################################################################

    radar_data = pd.DataFrame(dict(
        r=[python_skills/10,
        education_rank[education_level]*2,
        proficiency_rank[english]*2,
        grade,
        sql/10],
        theta=['Python Score','Education Level','English Proficiency','GPA', 'SQL Score'],
        color = ['#006a4e', '#2e856e', '#5ca08e', '#8abaae', '#b8d5cd']))

    with c1:
        radar_bar(radar_data)

    #BUTTON##############################################################################################

    if st.checkbox('Add a wildcard', help='Click here to add a wildcard to the full pool of applicants that does not meet the requirements you set'):
        wildcard = df.sample()
        st.info('Added a wildcard')

    st.session_state.temp_df = temp_df
    st.session_state.radar_data= radar_data
    st.session_state.education_rank = education_rank
    st.session_state.proficiency_rank = proficiency_rank

