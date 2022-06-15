import streamlit as st 
import pandas as pd
import plotly.graph_objects as go
from src.utils import * 
from src.utils_page2 import applicant_compare
import matplotlib.colors

def elgiganten_view(df, compare_candidates):
    #Define show variables in df
    #variables = ['Python_score', 'Education_level', 'Faculty', 'Years_experience', 'factor1', 'factor2', 'ID']
    variables = ['Education', 'Faculty', 'Workfields', 'Years Experience', 'Strength', 'Skills', 'ID', 'unique_color']
    df_plot =df
    df = df[df.columns.intersection(variables)]
    #st.dataframe(df)
    #Define common parameters, if compare_length is sufficient
    if int(len(compare_candidates)) == 2 or len(compare_candidates) == 3:
        #if st.checkbox('Show only differences'):
        #    st.write('write')
        index1 = int(compare_candidates[0][-1])
        index2 = int(compare_candidates[1][-1])

        #Show page for two candidates
        if int(len(compare_candidates)) == 2: 
            #define indexes for df
            indexes = [index1, index2]
            identify_IDs = pd.DataFrame(df_plot.iloc[indexes])

            #Create dataframe
            df = pd.DataFrame(df.iloc[indexes]).transpose()
            #df = df.astype(str)
            
            values = [list(df.index), list(df[df.columns[0]]), list(df[df.columns[1]])]
            
            IDs = list(df.iloc[-2])
            uni_colors = list(df.iloc[-1])
            uni_colors_rgba = [f"rgba{matplotlib.colors.to_rgb(x)}"[:-1]+", 0.3)" for x in uni_colors]#B4FBB8
            
            differences = [list(i) for i in (zip(values[0],values[1], values[2])) if len(set(i[1:]))!=1]
            
            value_header = [['Variable'], IDs[0], IDs[1]]
            compare_these = list(identify_IDs['Name'])
        
            individual1 = applicant_compare(identify_IDs,compare_these[0])
            individual2 = applicant_compare(identify_IDs,compare_these[1])
            match_individual = go.Figure(data=[individual1,individual2],
                layout=go.Layout(polar={'radialaxis': {'visible': False}},width=550, height=400,showlegend=True))
            match_individual.update_polars(radialaxis_range=[0,10]) 


        #Show page for three candidates
        if len(compare_candidates) == 3:
            #Define indexes 
            index3 = int(compare_candidates[2][-1])
            indexes = [index1, index2, index3]
            identify_IDs = pd.DataFrame(df_plot.iloc[indexes])
            
            #Create dataframe
            df = pd.DataFrame(df.iloc[indexes]).transpose()
            values = [list(df.index), list(df[df.columns[0]]), list(df[df.columns[1]]), list(df[df.columns[2]])]

            IDs = list(df.iloc[-2])
            value_header = [['Variable'], IDs[0], IDs[1], IDs[2]]
            uni_colors = list(df.iloc[-1])
            uni_colors_rgba = [f"rgba{matplotlib.colors.to_rgb(x)}"[:-1]+", 0.3)" for x in uni_colors]#B4FBB8
            
            differences = [list(i) for i in (zip(values[0],values[1], values[2], values[3])) if len(set(i[1:]))!=1]
            
            compare_these = list(identify_IDs['Name'])
            individual1 = applicant_compare(identify_IDs,compare_these[0])
            individual2 = applicant_compare(identify_IDs,compare_these[1])
            individual3 = applicant_compare(identify_IDs,compare_these[2])
            match_individual = go.Figure(data=[individual1,individual2,individual3],
                layout=go.Layout(polar={'radialaxis': {'visible': False}},width=550, height=400,showlegend=True))
            match_individual.update_polars(radialaxis_range=[0,10]) 

        fig = go.Figure(data=[go.Table(
            columnwidth = [15,20, 20, 20],
            header = dict(
                values = value_header,
                line_color='darkslategray',
                fill_color='darkgrey',
                align=['left','center'],
                font=dict(color='white', size=12),
                height=40
            ),
            cells=dict(
                #values=values,
                values = [i[:-2] for i in values],
                line_color='white',
                fill=dict(color=['lightgrey']+ uni_colors_rgba),
                align=['left', 'center'],
                font_size=12,
                height=50)
                )
            ])
        
        fig.update_layout(
            autosize=False,
            width=500,
            height=500,
            margin=dict(
                l=50,
                r=50,
                b=100,
                t=100,
                pad=10
            )
        )
        
        c1, c2, c3 = st.columns(3)
        if c3.checkbox('Show only differences', help='Check this box to only show variables where the candidates differ'):
            fig = go.Figure(data=[go.Table(
                columnwidth = [15,20, 20, 20],
                header = dict(
                    values = value_header,
                    line_color='darkslategray',
                    fill_color='darkgrey',
                    align=['left','center'],
                    font=dict(color='white', size=12),
                    height=40
                ),
                cells=dict(
                    #values=values,
                    values = [i[:-2] for i in [i for i in zip(*differences)]],
                    line_color='white',
                    fill=dict(color=['lightgrey']+ uni_colors_rgba),
                    align=['left', 'center'],
                    font_size=12,
                    height=50)
                    )
                ])
            
            fig.update_layout(
                autosize=False,
                width=500,
                height=500,
                margin=dict(
                    l=50,
                    r=50,
                    b=100,
                    t=100,
                    pad=10
                )
            ) 

        col1, col2 = st.columns([15,15])
        with col1:
            st.write(match_individual)
        with col2:        
            #st.checkbox('Show only differences')
            st.plotly_chart(fig)
    else: 
        st.warning('Choose 2 or 3 candidates to compare')

