import streamlit as st 
import pandas as pd
import plotly.graph_objects as go
from src.utils import * 
from src.utils_page2 import applicant_compare

def elgiganten_view(df, compare_candidates):
    #Define show variables in df
    variables = ['Python_score', 'Education_level', 'Faculty', 'Years_experience', 'factor1', 'factor2', 'ID']
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
            df = df.astype(str)
            
            values = [list(df.index), df[df.columns[0]], df[df.columns[1]]]
            value_header = [['Variable'],['Candidate X'], ['Candidate Y']]

            compare_these = list(identify_IDs['Name'])
        
            individual1 = applicant_compare(identify_IDs,compare_these[0])
            individual2 = applicant_compare(identify_IDs,compare_these[1])
            match_individual = go.Figure(data=[individual1,individual2],
                layout=go.Layout(polar={'radialaxis': {'visible': False}},width=600, height=600,showlegend=True))
            match_individual.update_polars(radialaxis_range=[0,10]) 


        #Show page for three candidates
        if len(compare_candidates) == 3:
            #Define indexes 
            index3 = int(compare_candidates[2][-1])
            indexes = [index1, index2, index3]
            identify_IDs = pd.DataFrame(df_plot.iloc[indexes])
            #Create dataframe
            df = pd.DataFrame(df.iloc[indexes]).transpose()
            values = [list(df.index), df[df.columns[0]], df[df.columns[1]], df[df.columns[2]]]
            value_header = [['Variable'],['Candidate X'], ['Candidate Y'], ['Candidate Z']]

            compare_these = list(identify_IDs['Name'])
            individual1 = applicant_compare(identify_IDs,compare_these[0])
            individual2 = applicant_compare(identify_IDs,compare_these[1])
            individual3 = applicant_compare(identify_IDs,compare_these[2])
            match_individual = go.Figure(data=[individual1,individual2,individual3],
                layout=go.Layout(polar={'radialaxis': {'visible': False}},width=600, height=600,showlegend=True))
            match_individual.update_polars(radialaxis_range=[0,10]) 

        fig = go.Figure(data=[go.Table(
            columnwidth = [250,600, 600, 600],
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
                line_color='white',
                fill=dict(color=['paleturquoise', 'red']),
                
                align=['left', 'center'],
                font_size=12,
                height=50)
                )
            ])
        fig.update_layout(
            autosize=False,
            width=1000,
            height=500,
            margin=dict(
                l=50,
                r=50,
                b=100,
                t=100,
                pad=10
            )
        )
        
        #compare

        
        #df = df.iloc[:3,]

        #compare_these = list(df_plot['Name'])
        
        #individual1 = applicant_compare(df_plot,compare_these[0])
        #individual2 = applicant_compare(df_plot,compare_these[1])
        #match_individual = go.Figure(data=[individual1,individual2],
        #    layout=go.Layout(polar={'radialaxis': {'visible': False}},width=600, height=600,showlegend=True))
        #individual3 = applicant_compare(df_plot,compare_these[2])
        #match_individual = go.Figure(data=[individual1,individual2,individual3],
        #    layout=go.Layout(polar={'radialaxis': {'visible': False}},width=600, height=600,showlegend=True))
        #match_individual.update_polars(radialaxis_range=[0,10]) 

        st.write(match_individual)
                
        st.plotly_chart(fig)

    else: 
        st.warning('Choose 2 or 3 candidates to compare')

