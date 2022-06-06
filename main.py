
import streamlit as st
from page1 import *
from src.utils_page1 import *
from page2 import *
from page5 import *

st.set_page_config(layout = "wide")

#define style
#local_css("styles.css")

#option_names = ["page1", "page2", "page5"]

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
      temp_df, radar_data, education_rank = page1()
      #image_files=[]
      #for applicant in list(temp_df['Name']):
      #   applicant_match(temp_df, applicant, radar_data, education_rank)
      #   image_files.append(f'{(applicant).replace(" ", "")}.png')
      #   temp_df['ano_image'] = image_files    
      #   temp_df.to_csv("Data/applicants-from-page-1.csv")
      
elif st.session_state["page"] == 'page2':
   with placeholder.container(): 
      yes_candidates = page2(candidates)
      df = candidates.iloc[yes_candidates]
      df.to_csv('Data/yes_candidates.csv') 
elif st.session_state["page"] == 'page5':
   with placeholder.container(): 
      page5()