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

candidates = pd.read_csv('Data/applicants250.csv',na_values=['a','b'])

candidates = pd.DataFrame(candidates[0:5])

process_bar = st.progress(50)

selected = streamlit_menu(options=["All", "Yes", "Maybe", "No"], icons=["circle", "check-circle", "question-circle", "x-circle"])

#col1, col2, col3 = st.columns(3)

image = Image.open('Images/download2.jpg')

#select_block_container_style()
#add_resources_section()

 # Creating

header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
    img_to_bytes('Images/download2.jpg')
)

if selected == "All":
    st.title(f"You have selected {selected}")
    for c in range(0, len(candidates)): 
        #define image
        image = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:300px; position:relative; top:70px;'>".format(
            img_to_bytes('Images/download2.jpg')
            )

        #define info
        Text1 = candidates.iloc[c]['Text1']
        Text2 = candidates.iloc[c]['Text2']

        #tags
        tags = "<input type='checkbox' id='instagram' name='source' value='instagram' ><span style='color:#FFF'>Pepperoni</span><br>"
        
        #print(info[1])
        with Grid("1 1 1") as grid:
            grid.cell("a", 1, 2, 1, 3).markdown(image)
            grid.cell("b", 2, 3, 1, 2).markdown(f'<font color="#666666">{Text1}</font>')
            grid.cell("c", 2, 3, 2, 3).markdown(Text2)
            grid.cell("d", 3, 4, 2, 3).plotly_chart(get_plotly_fig())
            grid.cell("e", 3, 4, 1, 2).markdown(tags)
        
#    with st.container():
#        st.write("This is inside the container")
#        with col1:
#            # You can call any Streamlit command, including custom components:
#            st.bar_chart(np.random.randn(50, 3))
#        with col2: 
#            st.image(image, caption='Sunrise by the mountains', width=200)
#            st.markdown('<img src="/Images/download2.jpg" width="500" height="600">', unsafe_allow_html=True)

if selected == "Yes":
    st.title(f"You have selected {selected}")
    yes_candidates = candidates.loc[candidates['tag'] == "Yes"]


if selected == "Maybe":
    st.title(f"You have selected {selected}")
if selected == "No":
    st.title(f"You have selected {selected}")