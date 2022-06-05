
import streamlit as st
from page1 import *
from src.utils_page1 import *
from page2 import *
from page5 import *

st.set_page_config(layout = "wide")

option_names = ["page1", "page2", "page3"]

placeholder = st.empty()

next = st.button("Next/save")

if next:
   if st.session_state["radio_option"] == 'page1':
        st.session_state.radio_option = 'page2'
   elif st.session_state["radio_option"] == 'page2':
        st.session_state.radio_option = 'page5'
   else: 
       st.session_state["radio_option"] = 'page1'

with st.expander('Navigate'): 
   option = st.radio("Pick an option", option_names , key="radio_option")

if option == 'page1':
   with placeholder.container(): 
      temp_df, radar_data, education_rank = page1()
      #image_files=[]
      #for applicant in list(temp_df['Name']):
      #   applicant_match(temp_df, applicant, radar_data, education_rank)
      #   image_files.append(f'{(applicant).replace(" ", "")}.png')
      #   temp_df['ano_image'] = image_files    
      #   temp_df.to_csv("Data/applicants-from-page-1.csv")
      
elif option == 'page2':
   with placeholder.container(): 
      yes_candidates = page2(candidates)
      df = candidates.iloc[yes_candidates]
      df.to_csv('Data/yes_candidates.csv') 
elif option == 'page5':
   with placeholder.container(): 
      page5()