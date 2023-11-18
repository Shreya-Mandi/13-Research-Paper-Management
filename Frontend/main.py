import streamlit as st
from streamlit_option_menu import option_menu


#main frame
'''
# Research Paper Management System
'''

# sidebar
with st.sidebar:
    choose = option_menu("Navigation Pane", ["Login", "Register", "Your Projects"],
                            default_index=0,
                             styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "", "font-size": "15px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#82caff"},
            "nav-link-selected": {"background-color": "#82caff"},
        }
        )