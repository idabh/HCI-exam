from page1 import * 
from page2 import *
from page5 import * 
import os

#set wide style 

#define style
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

candidates = pd.read_csv('Data/applicants-from-page-1.csv',na_values=['a','b'])
st.session_state['page_no'] = 1

def main(candidates): 
    if st.session_state['page_no'] == 1: 
        temp_df, radar_data, education_rank = page1(st.session_state['page_no'])
        #Next button
        next1 = st.button('Next', key = 'page1')

        #Change to next page
        if next1 == True: 
            image_files=[]
            for applicant in list(temp_df['Name']):
                applicant_match(temp_df, applicant, radar_data, education_rank)
                image_files.append(f'{(applicant).replace(" ", "")}.png')
            temp_df['ano_image'] = image_files    
            temp_df.to_csv("Data/applicants-from-page-1.csv")
            st.session_state['page_no'] = 2

    elif st.session_state['page_no'] == 2: 
        yes_candidates = page2(st.session_state['page_no'], candidates)
        #Next button
        next2 = st.button('Next', key = 'page2')
        #Change to next page
        if next2 == True: 
            df = candidates.iloc[yes_candidates]
            df.to_csv('Data/yes_candidates.csv') 
            st.session_state['page_no'] = 3
    elif st.session_state['page_no'] == 3:
        #page1()
        st.write('succes')

main(candidates)