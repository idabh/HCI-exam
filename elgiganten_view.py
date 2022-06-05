import streamlit as st 
import pandas as pd
from src.utils import * 

def elgiganten_view(df, compare_candidates):
    st.write('elgiganten_view')
    if int(len(compare_candidates)) == 2 or len(compare_candidates) == 3:
        index1 = int(compare_candidates[0][-1])
        index2 = int(compare_candidates[1][-1])
        #col1, col2 = st.columns(2)

        ## Candidate 1
        Text1_1 = df.iloc[index1]['Text1']
        Text2_1 = df.iloc[index1]['Text2']
        motivation_1 = df.iloc[index1]['motivation_letter']
        years_experience_1 = df.iloc[index1]['Years_experience']
        education_1 = df.iloc[index1]['education']
        workfield_1 = df.iloc[index1]['workfields']
        strength_1 = df.iloc[index1]['strength']
        skills_str_1 = df.iloc[index1]['skills']
        skill_1 = list(skills_str_1.split("'"))
        skills_1 = f'Skills: {skill_1[1]}, {skill_1[3]}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; and {skill_1[5]}'
        image_path_1 = df.iloc[index1]['image']
        image_1 = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:270px; height:247px;'>".format(
            img_to_bytes(f'Data/Images/{image_path_1}')
            )
        
        ## Candidate 2
        Text1_2 = df.iloc[index2]['Text1']
        Text2_2 = df.iloc[index2]['Text2']
        motivation_2 = df.iloc[index2]['motivation_letter']
        years_experience_2 = df.iloc[index2]['Years_experience']
        education_2 = df.iloc[index2]['education']
        workfield_2 = df.iloc[index2]['workfields']
        strength_2 = df.iloc[index2]['strength']

        skills_str_2 = df.iloc[index2]['skills']
        skill_2 = list(skills_str_2.split("'"))
        skills_2 = f'Skills: {skill_2[1]}, {skill_2[3]}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; and {skill_2[5]}'
        image_path_2 = df.iloc[index2]['image']
        image_2 = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:270px; height:247px;'>".format(
            img_to_bytes(f'Data/Images/{image_path_2}')
            )

        #show images
        st.markdown(image_1, unsafe_allow_html= True)
        st.markdown(image_2, unsafe_allow_html= True)



        #define indexes for df
        indexes = [index1, index2]
            
        if len(compare_candidates) == 3:
            #col1, col2, col3 = st.columns (3)
            index3 = int(compare_candidates[2][-1])

            ## Candidate 3
            Text1_3 = df.iloc[index3]['Text1']
            Text2_3 = df.iloc[index3]['Text2']
            motivation_3 = df.iloc[index3]['motivation_letter']
            years_experience_3 = df.iloc[index3]['Years_experience']
            education_3 = df.iloc[index3]['education']
            workfield_3 = df.iloc[index3]['workfields']
            strength_3 = df.iloc[index3]['strength']

            skills_str_3 = df.iloc[index3]['skills']
            skill_3 = list(skills_str_3.split("'"))
            skills_3 = f'Skills: {skill_3[1]}, {skill_3[3]}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; and {skill_3[5]}'
            image_path_3 = df.iloc[index3]['image']
            image_3 = "<img src='data:image/png;base64,{}' class='img-fluid' style='width:270px; height:247px; position: fixed, left: -200px'>".format(
                img_to_bytes(f'Data/Images/{image_path_3}')
                )
            #show candidate 3
            #with col3: 
            st.markdown(image_3, unsafe_allow_html= True)
            #    st.image(f'Data/Images/{image_path_3}')


            indexes = [index1, index2, index3]

        data = pd.DataFrame(df.iloc[indexes]).transpose()
        test = data.astype(str)
        st.dataframe(data=test)

    else: 
        st.warning('Choose 2 or 3 candidates to compare')

   

   


    

