import streamlit as st 
import pandas as pd
import plotly.graph_objects as go
from src.utils import * 

def elgiganten_view(df, compare_candidates):
    st.write('view')
    #Define common parameters, if compare_length is sufficient
    if int(len(compare_candidates)) == 2 or len(compare_candidates) == 3:
        index1 = int(compare_candidates[0][-1])
        index2 = int(compare_candidates[1][-1])


        #Show page for two candidates
        if int(len(compare_candidates)) == 2: 
            #define indexes for df
            indexes = [index1, index2]


            #Create dataframe
            df = pd.DataFrame(df.iloc[indexes]).transpose()
            df = df.astype(str)

            values = [list(df.index), df[df.columns[0]], df[df.columns[1]]]
            value_header = [['Variable'],['Candidate X'], ['Candidate Y']]

        #Show page for three candidates
        if len(compare_candidates) == 3:
            #Define indexes 
            index3 = int(compare_candidates[2][-1])
            indexes = [index1, index2, index3]

            #Create dataframe
            df = pd.DataFrame(df.iloc[indexes]).transpose()
            values = [list(df.index), df[df.columns[0]], df[df.columns[1]], df[df.columns[2]]]
            value_header = [['Variable'],['Candidate X'], ['Candidate Y'], ['Candidate Z']]

        fig = go.Figure(data=[go.Table(
            columnwidth = [200,800, 800],
            header = dict(
                values = value_header,
                line_color='darkslategray',
                fill_color='royalblue',
                align=['left','center'],
                font=dict(color='white', size=12),
                height=40
            ),
            cells=dict(
                values=values,
                line_color='darkslategray',
                fill=dict(color=['paleturquoise', 'white']),
                align=['left', 'center'],
                font_size=12,
                height=30)
                )
            ])

        st.plotly_chart(fig)

    else: 
        st.warning('Choose 2 or 3 candidates to compare')

