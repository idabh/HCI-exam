#Page 1

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#from streamlit_option_menu import option_menu

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu


#load data
df = pd.read_csv('/Users/thearolskovsloth/Documents/MASTERS_I_COGSCI/second_sem/HCI/HCI-exam/Data/applicants250.csv')




with st.sidebar:
    st.title("STEP 1: Screening")
    st.header("Filters")
    
    education_level = st.select_slider("Highest education level", options=["High School", "Bachelor's", "Master's", "phd"], value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
    
    python_skills = st.slider("Python skills", min_value=0, max_value=100, value=100, step=None, format=None, key="bachelors", help="The performances of the candidates ", on_change=None, args=None, kwargs=None,  disabled=False)
    
    sql_skills = st.slider("SQL skills", min_value=0, max_value=100, value=100, step=None, format=None, key="bachelors", help="The performances of the candidates ", on_change=None, args=None, kwargs=None,  disabled=False)
    
    academic_prof = st.multiselect("Academic profile", options=["sciences", "engineering", "arts"], default=["sciences", "engineering", "arts"], key=None, help="Check all the relevant profiles for this position", on_change=None, args=None, kwargs=None, disabled=False)


#process bar
process_bar = st.progress(25)

#chosen applicants
temp_df = df.loc[
    (df['Python_score'] >= python_skills) & 
    (df['Faculty'].isin(academic_prof))
    ]

#count of remaining applicants
remaining_app = len(temp_df)
diff_app = f"{(remaining_app)-(len(df))} applicants since initial something"
st.metric("applicants", remaining_app, delta= diff_app, delta_color="normal")

#show data frame
st.dataframe(data=temp_df, width=None, height=None)

arr = temp_df["Python_score"]
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

#fig = plt.scatter(x= temp_df["Age"], y= temp_df["Python_score"])
#st.pyplot(fig) #display the plot




#st.balloons()
#st.snow()
