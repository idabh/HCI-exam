from streamlit_option_menu import option_menu
from pathlib import Path
import base64
import streamlit as st

def streamlit_menu(options, icons, key, default_index):
        selected = option_menu(
            menu_title=None,  # required
            options=options,
            icons=icons,
            key = key,
            menu_icon="cast",  # optional
            default_index=default_index,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#b8d5cd"},
                "icon": {"color": "white", "font-size": "20px"},
                "nav-link": {
                    "font-size": "17px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#8abaae",
                     "color": "white",
                },
                "nav-link-selected": {"background-color": '#5ca08e', "color": "white"},
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