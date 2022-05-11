#Page 1

import streamlit as st
#from streamlit_option_menu import option_menu

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu


with st.sidebar:
    st.title("STEP 1: Screening")
    st.header("Filters")
    st.select_slider("Highest education level", options=["High School", "Bachelor's", "Master's", "phd"], value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)
    st.slider("Python skills", min_value=0, max_value=100, value=100, step=None, format=None, key="bachelors", help="The performances of the candidates ", on_change=None, args=None, kwargs=None,  disabled=False)
    st.slider("SQL skills", min_value=0, max_value=100, value=100, step=None, format=None, key="bachelors", help="The performances of the candidates ", on_change=None, args=None, kwargs=None,  disabled=False)
    st.multiselect("Academic profile", options=["Natural Sciences", "Business", "Data Science", "Economics"], default=None, key=None, help="Check all the relevant profiles for this position", on_change=None, args=None, kwargs=None, disabled=False)

st.balloons()
#st.snow()