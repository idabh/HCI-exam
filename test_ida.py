'''
Grid layout for ELGIGANTEN VIEW

NOTES:
- can't center the images
- html to format text
'''

# packages
import streamlit as st 
from grid import *
from src.utils import * 

# style stuff
st.set_page_config(layout = "wide")
local_css("styles.css")
#process_bar = st.progress(50) #define process bar
col1, col2, col3 = st.columns(3) #define columns

# define image
image = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:300px; position:relative; top:15px;'>".format(
            img_to_bytes('Images/download1.jpg')
            )

image2 = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:300px; position:relative; top:15px;'>".format(
            img_to_bytes('Images/download1.jpg')
            )

image3 = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:300px; position:relative; top:15px;'>".format(
            img_to_bytes('Images/download1.jpg')
            )

# radio buttons at top
with col1: 
  st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key='key1')
with col2: 
  st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key='key2')
with col3: 
  st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key='key3')


with Grid(template_columns="1 1 1", gap='5px', background_color='#0000',font_color='#1f1717') as grid:
    #first two nrs: ACROSS (col start and end), last two nrs: DOWN (row start and end)
    #grid.cell("a",1,2,1,2).markdown('<p align="center"><img src="Images/download1.jpg" /></p>')

    #HTML SYNTAX: style="property1:value1;property2:value2"
    grid.cell("a",1,2,1,2).markdown(image)
    grid.cell("b",2,3,1,2).markdown(image2)
    grid.cell("c",3,4,1,2).markdown(image3)
    grid.cell("d",1,2,3,4).markdown('<p style="color:black;font-weight:bold;text-align:center">Here is some text, hurray!</p>')
    grid.cell("e",2,3,3,4).markdown('<p style="color:black;font-weight:bold;text-align:center">Here is some more text, hurray!</p>')
    grid.cell("f",3,4,3,4).markdown('<p style="color:black;font-weight:bold;text-align:center">Here is even more text, hurray!</p>')
    

    #grid.cell("b",2, 3, 2, 3).text("The cell to the left is a dataframe")
    #grid.cell("c", 3, 4, 2, 3).plotly_chart(get_plotly_fig())
    #grid.cell("d", 1, 2, 1, 3).dataframe(get_dataframe())
    #grid.cell("e", 3, 4, 1, 2).markdown("Try changing the **block container style** in the sidebar!")



