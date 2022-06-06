
from venv import create
import streamlit as st
from page1 import *
from src.utils_page1 import *
from page2 import *
from page5 import *

st.set_page_config(layout = "wide")

#define style
#local_css("styles.css")

placeholder = st.empty()

next = st.button("Next/save")

if 'page' not in st.session_state: 
   st.session_state["page"] ='page1'

if next:
   if st.session_state["page"] == 'page1':
        st.session_state["page"] = 'page2'
   elif st.session_state["page"] == 'page2':
        st.session_state["page"] = 'page5'
   elif st.session_state["page"] == 'page5':
        st.session_state["page"] = 'page1'

if st.session_state["page"] == 'page1':
   with placeholder.container(): 
      page1()
            
elif st.session_state["page"] == 'page2':
   #Save image output from page1
   create_plots()

   with placeholder.container(): 
      page2()
      df = candidates.iloc[st.session_state['yes_candidates']]
      df.to_csv('Data/yes_candidates.csv') 
elif st.session_state["page"] == 'page5':
   with placeholder.container(): 
      page5()