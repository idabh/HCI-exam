
from venv import create
import streamlit as st
from page1 import *
from src.utils_page1 import *
from page2 import *
from page5 import *

# --- MARKDOWN:
# Setting main page configurations
st.set_page_config(layout="wide",page_title="(COOL NAME)", page_icon="🔍")

# Setting main page configurations
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 1rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
                .css-1a7jz76 h3{
                    padding: 0rem 0px 0rem;
                }

                .css-1xv07vx hr{
                margin: 0.5em 0px;
                }

        </style>
        """, unsafe_allow_html=True)

# Setting button configurations

st.markdown(
      """
<style>

.css-1a7jz76 {
   padding: 4rem 1rem;
}

div[data-testid="stToolbar"] {
   visibility: hidden;
   height: 0%;
   position: fixed;
   }
div[data-testid="stDecoration"] {
   visibility: hidden;
   height: 0%;
   position: fixed;
   }
div[data-testid="stStatusWidget"] {
   visibility: hidden;
   height: 0%;
   position: fixed;
   }

#MainMenu {
   visibility: hidden;
   }
footer {
   visibility: hidden;
   height: 0%
   }
header {
   visibility: hidden;
   height: 0%;
   }

div.stButton > button:first-child {
   box-shadow:inset 0px 1px 0px 0px #54a3f7;
   background:linear-gradient(to bottom, #0975b0 5%, #0061a7 100%);
   background-color:#0975b0;
   border-radius:5px;
   border:1px solid #124d77;
   display: flex;
   flex-direction: column;
   cursor:pointer;
   color:#ffffff;
   height: 3.3em;
   margin: auto;
   width: 100%;

   }
div.stButton > button:hover {
   background:linear-gradient(to bottom, #0061a7 80%, #0a6da3 100%);
   background-color:#0061a7;
   }

div.stButton > button:active {
   position:relative;
   top:2px;
   }

div.stDownloadButton > button:first-child {
   background-color: #007429;
   color:#ffffff;
   border-color: #006eaf;
   height: 3.7em;
   width: 16em;
   margin: auto;
   display: block;
   }
div.stDownloadButton > button:hover {
   background-color: #1e9047;
   color:#ffffff;
   border-color: #006eaf;
   height: 3.7em;
   width: 16em;
   }

</style>""", unsafe_allow_html=True)

# ------

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