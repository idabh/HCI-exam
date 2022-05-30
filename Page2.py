import streamlit as st
from streamlit_option_menu import option_menu

process_bar = st.progress(50)

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 2



def streamlit_menu(example=1):
    if example == 2:
            # 2. horizontal menu w/o custom style
            selected = option_menu(
                menu_title=None,  # required
                options=["All", "Yes", "Maybe", "No"],  # required
                icons=["circle", "check-circle", "question-circle", "x-circle"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                orientation="horizontal",
                styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                    #"icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {
                    #    "font-size": "25px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {"background-color": 'darkgrey'},
                }
            )
            return selected

    #A function that returns the html code as it should


selected = streamlit_menu(example=EXAMPLE_NO)
if selected == "All":
    st.title(f"You have selected {selected}")

    st.markdown('<img src=url alt="W3Schools.com">', unsafe_allow_html=True)



if selected == "Yes":
    st.title(f"You have selected {selected}")

if selected == "Maybe":
    st.title(f"You have selected {selected}")
if selected == "No":
    st.title(f"You have selected {selected}")