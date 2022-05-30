from streamlit_option_menu import option_menu
from pathlib import Path
import base64
import streamlit as st

def streamlit_menu(options, icons):
        selected = option_menu(
            menu_title=None,  # required
            options=options,
            icons=icons,
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

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)