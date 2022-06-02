import streamlit as st 
from grid import *
st.set_page_config(layout = "wide")

col1, col2, col3 = st.columns(3)
with col1: 
  st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key='key1')
with col2: 
  st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key='key2')
with col3: 
  st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key='key3')
    

with Grid("1 1 1") as grid:
        grid.cell(2,3,1,2).markdown("# This is A Markdown Cell")
        grid.cell("b", 2, 3, 2, 3).text("The cell to the left is a dataframe")
        grid.cell("c", 3, 4, 2, 3).plotly_chart(get_plotly_fig())
        grid.cell("d", 1, 2, 1, 3).dataframe(get_dataframe())
        grid.cell("e", 3, 4, 1, 2).markdown("Try changing the **block container style** in the sidebar!")

   
modal = st.expander("Advanced options")

option_1 = modal.checkbox("Option 1")
option_2 = modal.checkbox("Option 2")
option_3 = modal.checkbox("Option 3")
option_4 = modal.checkbox("Option 4")

if option_1:
   st.write("Hello world 1")

if option_2:
   st.write("Hello world 2")

if option_3:
   st.write("Hello world 3")

if option_4:
   st.write("Hello world 4")


'''
To pick a color: https://www.w3schools.com/colors/colors_picker.asp
Grid ressource: https://gridbyexample.com/examples/
'''


import streamlit as st
from src.utils import *
from PIL import Image
import numpy as np 
import pandas as pd
from grid import *

#set wide style 
st.set_page_config(layout = "wide")

#define style
local_css("styles.css")

#define data 
candidates = pd.read_csv('Data/applicants250.csv',na_values=['a','b'])
candidates = pd.DataFrame(candidates[0:5])

#define process bar
process_bar = st.progress(50)

#define menu
selected = streamlit_menu(options=["All", "Yes", "Maybe", "No"], icons=["circle", "check-circle", "question-circle", "x-circle"])


if selected == "All":
    st.title(f"You have selected {selected}")
    for c in range(0, len(candidates)): 
        #define image
        image = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:300px; position:relative; top:15px;'>".format(
            img_to_bytes('Images/download2.jpg')
            )

        #define info
        Text1 = candidates.iloc[c]['Text1']
        Text2 = candidates.iloc[c]['Text2']

        #tags
        tags ='''
        <input type='radio' id='html' name='fav_language' value='HTML'> 
        <label for='html'>HTML</label>
        <br> 
        '''
        '''
        <input type='radio' id='css' name='fav_language' value='CSS'> 
        <label for='css'>CSS</label>
        <br>
        <input type='radio' id='javascript' name='fav_language' value='JavaScript'>
        <label for="javascript">JavaScript</label>
        <br>
        '''
        # "<input type='checkbox'><span> Pepperoni</span><br>"
        

        #print(info[1])
        with Grid("1 1 1") as grid:
            grid.cell("a", 1, 2, 1, 3).markdown(image)
            grid.cell("b", 2, 3, 1, 2).markdown(Text1)
            grid.cell("c", 2, 3, 2, 3).markdown(Text2)
            grid.cell("d", 3, 4, 2, 3).plotly_chart(get_plotly_fig())
            grid.cell("e", 3, 4, 1, 2).markdown(tags)
        
if selected == "Yes":
    st.title(f"You have selected {selected}")
    yes_candidates = candidates.loc[candidates['tag'] == "Yes"]


if selected == "Maybe":
    st.title(f"You have selected {selected}")
if selected == "No":
    st.title(f"You have selected {selected}")