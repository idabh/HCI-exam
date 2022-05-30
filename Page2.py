import streamlit as st
from src.utils import *
process_bar = st.progress(50)

selected = streamlit_menu()

if selected == "All":
    st.title(f"You have selected {selected}")
    st.markdown('<img src="/Images/download2.jpg" width="500" height="600">', unsafe_allow_html=True)

if selected == "Yes":
    st.title(f"You have selected {selected}")

if selected == "Maybe":
    st.title(f"You have selected {selected}")
if selected == "No":
    st.title(f"You have selected {selected}")