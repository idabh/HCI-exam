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