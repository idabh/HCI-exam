import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px

#load data
df = pd.read_csv("./Data/applicants250.csv")

#look at data:
st.dataframe(df)


# pie chart
fig = px.pie(df, values=[1, 2, 3], 'Sex', title='Gender distribution (all applicants)')


st.plotly_chart(fig)