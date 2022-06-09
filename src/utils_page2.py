import streamlit as st
from src.utils import * 
from PIL import Image
import plotly.graph_objects as go
    
def show_page2(ckey_list, rkey_list, tkey_list, index, df): 
    col1, col2, col3, col4 = st.columns(4)
    
    #define keys
    radio_key = rkey_list[index]
    text_key = tkey_list[index]
    compare_key = ckey_list[index]

    #define image
    image_path = df.iloc[index]['ano_image']
    image = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:270px; height:247px; position:relative; top:0px;'>".format(
        img_to_bytes(f'Images/{image_path}')
        )
    
    #define personality profile
    personality_path = df.iloc[index]['Personality Profiles']
    personality_profile = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:270px; height:200px; position:relative; top:-7px;'>".format(
        img_to_bytes(f'Data/personality_plots/{personality_path}')
        )
        

    #define info
    motivation = df.iloc[index]['Motivation Letter']
    years_experience = df.iloc[index]['Years Experience']
    education = df.iloc[index]['Education']
    workfield = df.iloc[index]['Workfields']
    strength = df.iloc[index]['Strength']
    alias = df.iloc[index]['ID']
    skills = df.iloc[index]['Skills']

    with col1: 
        st.markdown(f"<div style = ' position:relative; left:90px; '> <b> {alias} </b></div>", unsafe_allow_html=True)

        st.markdown(image, unsafe_allow_html= True)
    
    with col2: 
        st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key=radio_key)
        st.write('')
        st.text_input(label = 'Notes', key = text_key)

    with col3: 
        #write education
        st.markdown(f"<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-book' viewBox='0 0 16 16'><path d='M1 2.828c.885-.37 2.154-.769 3.388-.893 1.33-.134 2.458.063 3.112.752v9.746c-.935-.53-2.12-.603-3.213-.493-1.18.12-2.37.461-3.287.811V2.828zm7.5-.141c.654-.689 1.782-.886 3.112-.752 1.234.124 2.503.523 3.388.893v9.923c-.918-.35-2.107-.692-3.287-.81-1.094-.111-2.278-.039-3.213.492V2.687zM8 1.783C7.015.936 5.587.81 4.287.94c-1.514.153-3.042.672-3.994 1.105A.5.5 0 0 0 0 2.5v11a.5.5 0 0 0 .707.455c.882-.4 2.303-.881 3.68-1.02 1.409-.142 2.59.087 3.223.877a.5.5 0 0 0 .78 0c.633-.79 1.814-1.019 3.222-.877 1.378.139 2.8.62 3.681 1.02A.5.5 0 0 0 16 13.5v-11a.5.5 0 0 0-.293-.455c-.952-.433-2.48-.952-3.994-1.105C10.413.809 8.985.936 8 1.783z'/></svg>     {education}", unsafe_allow_html=True)
        #write experience
        st.markdown(f"<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-briefcase' viewBox='0 0 16 16'><path d='M6.5 1A1.5 1.5 0 0 0 5 2.5V3H1.5A1.5 1.5 0 0 0 0 4.5v8A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-8A1.5 1.5 0 0 0 14.5 3H11v-.5A1.5 1.5 0 0 0 9.5 1h-3zm0 1h3a.5.5 0 0 1 .5.5V3H6v-.5a.5.5 0 0 1 .5-.5zm1.886 6.914L15 7.151V12.5a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5V7.15l6.614 1.764a1.5 1.5 0 0 0 .772 0zM1.5 4h13a.5.5 0 0 1 .5.5v1.616L8.129 7.948a.5.5 0 0 1-.258 0L1 6.116V4.5a.5.5 0 0 1 .5-.5z'/></svg>    {years_experience} years of experience with <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{workfield} ", unsafe_allow_html=True)
        #write strength
        st.markdown(f"<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-lightning' viewBox='0 0 16 16'><path d='M5.52.359A.5.5 0 0 1 6 0h4a.5.5 0 0 1 .474.658L8.694 6H12.5a.5.5 0 0 1 .395.807l-7 9a.5.5 0 0 1-.873-.454L6.823 9.5H3.5a.5.5 0 0 1-.48-.641l2.5-8.5zM6.374 1 4.168 8.5H7.5a.5.5 0 0 1 .478.647L6.78 13.04 11.478 7H8a.5.5 0 0 1-.474-.658L9.306 1H6.374z'/></svg> {strength}", unsafe_allow_html=True)
        #write skills 
        st.markdown(f"<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-tools' viewBox='0 0 16 16'><path d='M1 0 0 1l2.2 3.081a1 1 0 0 0 .815.419h.07a1 1 0 0 1 .708.293l2.675 2.675-2.617 2.654A3.003 3.003 0 0 0 0 13a3 3 0 1 0 5.878-.851l2.654-2.617.968.968-.305.914a1 1 0 0 0 .242 1.023l3.27 3.27a.997.997 0 0 0 1.414 0l1.586-1.586a.997.997 0 0 0 0-1.414l-3.27-3.27a1 1 0 0 0-1.023-.242L10.5 9.5l-.96-.96 2.68-2.643A3.005 3.005 0 0 0 16 3c0-.269-.035-.53-.102-.777l-2.14 2.141L12 4l-.364-1.757L13.777.102a3 3 0 0 0-3.675 3.68L7.462 6.46 4.793 3.793a1 1 0 0 1-.293-.707v-.071a1 1 0 0 0-.419-.814L1 0Zm9.646 10.646a.5.5 0 0 1 .708 0l2.914 2.915a.5.5 0 0 1-.707.707l-2.915-2.914a.5.5 0 0 1 0-.708ZM3 11l.471.242.529.026.287.445.445.287.026.529L5 13l-.242.471-.026.529-.445.287-.287.445-.529.026L3 15l-.471-.242L2 14.732l-.287-.445L1.268 14l-.026-.529L1 13l.242-.471.026-.529.445-.287.287-.445.529-.026L3 11Z'/></svg>  {skills}", unsafe_allow_html=True)


    with col4: 
        st.markdown("<div style = 'position:relative; left:95px; top:opx; '>DISC-Profile</div>", unsafe_allow_html= True)
        st.markdown(personality_profile, unsafe_allow_html= True)
        st.checkbox('Compare', key =  compare_key)
  
    with st.expander(f"More information about {alias}"):
        st.markdown(f'<b>Motivation </b> <br> {motivation}', unsafe_allow_html=True)
    st.write('')
    st.write('')
    
    

def applicant_compare(data, individual):
    education_rank = {"High School":1, "Bachelor":2, "Masters":3, "Ph.d.":4, "Postdoc":5}
    proficiency_rank = {"No Proficiency":1, "Limited":2, "Professional":3, "Advanced":4, "Native":5}
    d = data.loc[data['Name'] == individual]
    ID = str(d.iloc[0,19])
    r=[ d.iloc[0,3]/10,
        education_rank[d.iloc[0,4]]*2,
        proficiency_rank[d.iloc[0,14]]*2,
        d.iloc[0,15],
        d.iloc[0,18]/10]
    theta=['Python Score','Education Level','English Proficiency','GPA', 'SQL Score']
    color = d.iloc[0,20]
    r = [*r, r[0]]
    individual = go.Scatterpolar(r=r, theta=theta, fill='toself',name=ID, line_color = color,opacity = 0.2,fillcolor= color) 
    return individual


