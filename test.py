import streamlit as st 
from grid import *
from src.utils import * 
st.set_page_config(layout = "wide")

col1, col2, col3 = st.columns(3)
with col1: 
  st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key='key1')
with col2: 
  st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key='key2')
with col3: 
  st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key='key3')
    
image = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:300px; position:relative; top:15px;'>".format(
            img_to_bytes('Images/download2.jpg')
            )

with Grid("1 1 1") as grid:
        grid.cell(2,3,1,2).markdown(image)
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

