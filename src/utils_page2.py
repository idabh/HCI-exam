import streamlit as st
from src.utils import * 
from PIL import Image

def show_page2(rkey_list, tkey_list, index, df): 
    col1, col2, col3, col4 = st.columns(4)
    
    #define keys
    radio_key = rkey_list[index]
    text_key = tkey_list[index]

    #define image
    image_path = df.iloc[index]['image']
    image = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:270px; height:247px; position:relative; top:0px;'>".format(
        img_to_bytes(f'Images/{image_path}')
        )
        

    #define info
    Text1 = df.iloc[index]['Text1']
    Text2 = df.iloc[index]['Text2']
    years_experience = df.iloc[index]['Years_experience']
    education = df.iloc[index]['education']


    with col1: 
        st.write('')
        st.markdown(image, unsafe_allow_html= True)
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
    
    with col2: 
        st.write('')
        st.write('')
        st.radio(label = 'Select option', options =['Not selected', 'Yes', 'Maybe', 'No'], key=radio_key)
        st.text_input(label = 'Notes', key = text_key)
        st.write('')
        st.write('')
        st.write('')
        st.write('')

    with col3: 
        st.markdown(f"<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-briefcase' viewBox='0 0 16 16'><path d='M6.5 1A1.5 1.5 0 0 0 5 2.5V3H1.5A1.5 1.5 0 0 0 0 4.5v8A1.5 1.5 0 0 0 1.5 14h13a1.5 1.5 0 0 0 1.5-1.5v-8A1.5 1.5 0 0 0 14.5 3H11v-.5A1.5 1.5 0 0 0 9.5 1h-3zm0 1h3a.5.5 0 0 1 .5.5V3H6v-.5a.5.5 0 0 1 .5-.5zm1.886 6.914L15 7.151V12.5a.5.5 0 0 1-.5.5h-13a.5.5 0 0 1-.5-.5V7.15l6.614 1.764a1.5 1.5 0 0 0 .772 0zM1.5 4h13a.5.5 0 0 1 .5.5v1.616L8.129 7.948a.5.5 0 0 1-.258 0L1 6.116V4.5a.5.5 0 0 1 .5-.5z'/></svg>     {years_experience} years of experience in ", unsafe_allow_html=True)
    
    with col4: 
        st.markdown(f"<p style = 'position:absolute; top:{index + 25}px; height: 100px; width: 200px; border: 3px solid #73AD21;'>{Text1}</p> ", unsafe_allow_html=True)
        st.markdown(f"<p style = 'position:absolute; top:{index + 150}px; height: 100px; width: 200px; border: 3px solid #73AD21;'>{Text2}</p> ", unsafe_allow_html=True)