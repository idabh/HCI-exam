'''
Elgiganten overview!
(IDA WORKING ON THIS)
Noter:
- add text felter
- vis kun forskelle funktion (ligesom elgiganten)
'''
# load packages
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly import express as px
from src.utils_page2 import *
from typing import List, Optional
import markdown

#set styles + define streamlit things
st.set_page_config(layout = "wide")
local_css("styles.css")
process_bar = st.progress(50) #define process bar (?)
col1, col2, col3 = st.columns(3) #define columns

# load data
comparing = pd.read_csv('Data/applicants200.csv')[:3]
to_show = ['Name','Python_score', 'Education_level', 'Faculty', 'Years_experience',  'factor1', 'factor2']
no_name = ['Python_score', 'Education_level', 'Faculty', 'Years_experience', 'factor1', 'factor2']

show = comparing[to_show]
show_no_name = comparing[no_name]

# change data format
df = pd.DataFrame([row for row in no_name]) # first column with variable
df.rename(columns={0: 'VARIABLE'}, inplace=True)
column_names = show['Name']
for idx, name in enumerate(column_names):
    df[name] = list(show_no_name.iloc[idx])

# ---- TRYING OUT GRIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIID ---








# ------------------

# IMAGES
image_path = 'download1.jpg'
def show_img(img_name):
    image = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:230px; height:207px; position:relative; top:0px;'>".format(
            img_to_bytes(f'Images/{img_name}')
            )
    st.markdown(image, unsafe_allow_html= True)

# THE TABLE

# show only differences?
df_plot = df
#if st.checkbox('Only show differences'):
#    df_novar = df_plot.drop('VARIABLE', axis=1)
#    df_plot = df_plot[~df_novar.eq(df_novar.iloc[:, 0], axis=0).all(1)] # only rows where not all column values are equal

# show the table
colorscale = [[0, '#073c87'],[.5, '#d9e9ff'],[1, '#fafcff']]
fig =  ff.create_table(df_plot, colorscale = colorscale, height_constant=50)
#st.plotly_chart(fig)