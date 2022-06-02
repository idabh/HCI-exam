#Page 1
import random
import plotly.express as px
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.utils import *
#from streamlit_option_menu import option_menu
st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
# Remove whitespace from the top of the page and sidebar
#st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)

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
#load data
df = pd.read_csv('/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/Data/applicants200.csv')
education_rank = {"high school":1, "bachelor":2, "masters":3, "phd":4}

with st.sidebar:
    st.title("STEP 1: Screening")
    st.header("Filters")
    st.markdown("Narrow down the applicants by manipulating the filters below")
    
    education_level = st.select_slider("Minimum education level", options=["high school", "bachelor", "masters", "phd"],  help="choose minimum education level needed for this position")

        
    python_skills = st.slider("Python skills", min_value=0, max_value=5, value=0, step=1, format=None, key="bachelors", help="The performances of the candidates ", on_change=None, args=None, kwargs=None,  disabled=False)

    fac1 = st.slider('Select value fac1', 0,10,1)
    fac2 = st.slider('Select value fac2',0,10,1)
    
    exp_needed = st.radio("Experience", options= ["Yes", "No"])
    
    academic_prof = st.multiselect("Academic profile", options=["sciences", "engineering", "arts"], default=["sciences", "engineering", "arts"], key=None, help="Check all the relevant profiles for this position", on_change=None, args=None, kwargs=None, disabled=False)


#process bar
process_bar = st.progress(25)

#chosen applicants
temp_df = df.loc[
    (df['Python_score'] >= python_skills) & 
    (df['Faculty'].isin(academic_prof)) & 
    (df['Education_level'].isin([k for k in education_rank.keys() if education_rank[k] >= education_rank[education_level]]))
    ]

#count of remaining applicants

remaining_app = len(temp_df)
diff_app = f"{(remaining_app)-(len(df))} applicants since initial something"
#st.metric("applicants", remaining_app, delta= diff_app, delta_color="normal")

counting = f'<div data-testid="stMetricValue" class="css-1xarl3l e16fv1kl2"> <div class="css-1ht1j8u e16fv1kl0"> <span style="font-size:20px;"> There are  </span> <span <h1 style="text-align: center;font-size:150px;">  {remaining_app} </h1> </span><span style="font-size:20px;">applicants remaining</span></div></div>'
st.markdown(counting, unsafe_allow_html=True)


#RADAR##############################################################################################


temporal_data = pd.DataFrame(dict(
    r=[python_skills/10,
       education_level,
       fac1,
       fac2],
    theta=['python skills','education_level','factor1',
           'factor2']))

def radar_chart(data):  
    df = temporal_data
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    st.write(fig)
#chosen_var = st.radio("Select a variable", options= ['education_level','python skills','minimum education', 'thermal stability'])
#
radar_chart(temp_df)

st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)




#show data frame
st.dataframe(data=temp_df, width=None, height=None)

#BUTTON##############################################################################################
#next_page = '<button kind="primary" class="css-9dpgwh edgvbvh1" {background-color: #4CAF50;}  >Next</button>'
next_page = '''
<html>
<head>
<style>
.button {
  position: relative;
  background-color: #4CAF50;
  border: none;
  font-size: 28px;
  color: #FFFFFF;
  padding: 20px;
  width: 200px;
  text-align: center;
  transition-duration: 0.4s;
  text-decoration: none;
  overflow: hidden;
  cursor: pointer;
}

.button:after {
  content: "";
  background: #f1f1f1;
  display: block;
  position: absolute;
  padding-top: 300%;
  padding-left: 350%;
  margin-left: -20px !important;
  margin-top: -120%;
  opacity: 0;
  transition: all 0.8s
}

.button:active:after {
  padding: 0;
  margin: 0;
  opacity: 1;
  transition: 0s
}
</style>
</head>
<body>

<h2>Animated Button - Ripple Effect</h2>

<button class="button">Click Me</button>

</body>
</html>


'''

left_column, mid_column, right_column = st.columns(3)
with right_column:
    st.button("next")
    if st.markdown(next_page, unsafe_allow_html=True):
        st.markdown("hello there")
#st.balloons()
#st.snow()



'''


#ISOTYPE###############################################################################################

# code for displaying multiple images in one figure
import altair as alt

#data = pd.DataFrame([dict(id=i) for i in range(0, len(temp_df))])
data = pd.DataFrame([dict(id=i) for i in random.sample(range(1,10000),len(temp_df))])

person = (
    "M1.7 -1.7h-0.8c0.3 -0.2 0.6 -0.5 0.6 -0.9c0 -0.6 "
    "-0.4 -1 -1 -1c-0.6 0 -1 0.4 -1 1c0 0.4 0.2 0.7 0.6 "
    "0.9h-0.8c-0.4 0 -0.7 0.3 -0.7 0.6v1.9c0 0.3 0.3 0.6 "
    "0.6 0.6h0.2c0 0 0 0.1 0 0.1v1.9c0 0.3 0.2 0.6 0.3 "
    "0.6h1.3c0.2 0 0.3 -0.3 0.3 -0.6v-1.8c0 0 0 -0.1 0 "
    "-0.1h0.2c0.3 0 0.6 -0.3 0.6 -0.6v-2c0.2 -0.3 -0.1 "
    "-0.6 -0.4 -0.6z"
)

fig1=alt.Chart(data).transform_calculate(
    row="ceil(datum.id/10)"
).transform_calculate(
    col="datum.id - datum.row*10"
).mark_point(
    filled=True,
    size=50/len(temp_df)*100
).encode(
    x=alt.X("col:O", axis=None),

    y=alt.Y("row:O", axis=None),
    opacity=alt.value(0.4),
    shape=alt.ShapeValue(person)
).properties(
    width=650,
    height=400
).configure_view(
    strokeWidth=0
)
st.altair_chart(fig1, use_container_width=False)
#fig = plt.scatter(x= temp_df["Age"], y= temp_df["Python_score"])
#st.pyplot(fig) #display the plot
'''