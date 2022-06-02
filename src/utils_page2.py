import streamlit as st
from src.utils import * 

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
        st.markdown(f"<p style = 'position:absolute; top:{index + 25}px; height: 100px; width: 200px; border: 3px solid #73AD21;'>{Text1}</p> ", unsafe_allow_html=True)
        st.markdown(f"<p style = 'position:absolute; top:{index + 150}px; height: 100px; width: 200px; border: 3px solid #73AD21;'>{Text2}</p> ", unsafe_allow_html=True)