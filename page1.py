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
    # columns for progress bar and info icon
    c1,c2 = st.columns([25,1])

    # progress bar
    progress1_path = 'Data/progress/progress1.png'
    progress1 = "<img src='data:image/png;base64,{}' class='img-fluid' style= 'height:100px; padding-bottom: 30px; padding-left: 50px;'>".format(
        img_to_bytes(progress1_path)
        ) 
    with c1:
        st.markdown(progress1, unsafe_allow_html= True)

    # info hover button
    help_p1 = '''
    STEP 1: FILTER\n
    Use the sliders to the left to define minimum requirements for the job position. The plot shows your chosen minimum requirements. The number shows how many applicants meet your chosen requirements. When you press ‘Next’, only these applicants will move on to the next step.\n
    If you check the ‘Add a wildcard’ box before you press ‘Next’, ScreenAid will automatically add one applicant that does not meet all minimum requirements, but that might still be a good fit for the position.
    '''

    with c2:
        st.download_button(label='?',data='blabla',help=help_p1,disabled=True)


    c1,c2 = st.columns([20,5])
    
    #load data
    df = pd.read_csv('Data/applicants200.csv')
    education_rank = {"High School":1, "Bachelor":2, "Masters":3, "Ph.d.":4, "Postdoc":5}
    proficiency_rank = {"No Proficiency":1, "Limited":2, "Professional":3, "Advanced":4, "Native":5}

    #Define session states
    if 'education_level' not in st.session_state: 
        st.session_state.education_level = "High School"
    if 'python_skills' not in st.session_state: 
        st.session_state.python_skills = 0
    if 'sql' not in st.session_state: 
        st.session_state.sql = 0
    if 'grade' not in st.session_state: 
        st.session_state.grade = 0
    if 'english' not in st.session_state: 
        st.session_state.english = "No Proficiency"
    if 'wildcard' not in st.session_state: 
        st.session_state.wildcard = False

    # DEFINE SIDEBAR #####################
    with st.sidebar:
        st.image('logo.png')
        st.session_state.education_level = st.select_slider("Education level", options=["High School", "Bachelor", "Masters", "Ph.d.", "Postdoc"],  help="Choose minimum education level", value = st.session_state.education_level)
        st.session_state.python_skills = st.slider("Python test score", min_value=0, max_value=100, value=st.session_state.python_skills, step=1, format=None,  help="Choose minimum Python test performance", on_change=None, args=None, kwargs=None,  disabled=False)
        st.session_state.sql = st.slider("SQL test score", min_value=0, max_value=100, value=st.session_state.sql, step=1, format=None,  help="Choose minimum SQL test performance", on_change=None, args=None, kwargs=None,  disabled=False)
        st.session_state.grade = st.slider('GPA', 0,10, value=st.session_state.grade, help="Choose minimum grade point average")
        st.session_state.english = st.select_slider('English Proficiency', options=["No Proficiency", "Limited", "Professional", "Advanced", "Native"], help="Choose minimum level of English proficiency", value = st.session_state.english)
        
        #academic_prof = st.multiselect("Academic profile", options=["sciences", "engineering", "arts"], default=["sciences", "engineering", "arts"], key=None, help="Check all the relevant profiles for this position")

    #chosen applicants
    temp_df = df.loc[
        (df['Python Score'] >= st.session_state.python_skills) & 
        (df['SQL Score'] >= st.session_state.sql) & 
        (df['Education Level'].isin([k for k in education_rank.keys() if education_rank[k] >= education_rank[st.session_state.education_level]])) &
        (df['English Proficiency'].isin([k for k in proficiency_rank.keys() if proficiency_rank[k] >= proficiency_rank[st.session_state.english]])) &
        ((df['GPA'] >= st.session_state.grade))
        ]
    
    #not chosen applicants
    unchosen_temp_df = df[~df.ID.isin(temp_df.ID)]

    #count of remaining applicants
    remaining_app = len(temp_df)

    counting = f'<div data-testid="stMetricValue" class="css-1xarl3l e16fv1kl2"> <div class="css-1ht1j8u e16fv1kl0"> <span <h1 style="text-align: center;font-size:80px; position: relative; top: -100px;"> <br><br> {remaining_app} </h1> </span><span style="font-size:20px; position: relative; top: -120px; left: 0px;"><br> applicants remaining </span> </div></div>'
    with c2:
        st.markdown(counting, unsafe_allow_html=True)

    #RADAR##############################################################################################

    radar_data = pd.DataFrame(dict(
        r=[st.session_state.python_skills/10,
        education_rank[st.session_state.education_level]*2,
        proficiency_rank[st.session_state.english]*2,
        st.session_state.grade,
        st.session_state.sql/10],
        theta=['Python Score','Education Level','English Proficiency','GPA', 'SQL Score'],
        color = ['#006a4e', '#2e856e', '#5ca08e', '#8abaae', '#b8d5cd']))

    with c1:
        radar_bar(radar_data)

    #save output
    st.session_state.temp_df = temp_df
    st.session_state.radar_data= radar_data
    st.session_state.education_rank = education_rank
    st.session_state.proficiency_rank = proficiency_rank

    #BUTTON##############################################################################################

    col1, col2 = st.columns(2)
    with col2: 
        wildcard_box = st.checkbox('Add a wildcard', help='Click here to automatically add a "wildcard" applicant that does not meet all minimum requirements', key = 'wildcard', value= st.session_state.wildcard)
        if wildcard_box:
            wildcard = unchosen_temp_df.sample()
            st.session_state.temp_df = temp_df.append(wildcard, ignore_index = True)
            st.info('Added a wildcard to the pool of filtered applicants. Click "Next" to move on to Step 2.')


#page1()