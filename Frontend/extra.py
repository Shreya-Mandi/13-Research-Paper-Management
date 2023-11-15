import streamlit as st
import pandas as pd
import numpy as np

# # Displaying a dataframe
# st.write(pd.DataFrame({
#     'col1': [1,2,3,4,5],
#     'col2': ['a','b','c','d','e']
# }))

## Line chart
# dataframe=np.random.rand(10,10)
# columns=['a','b','c','d','e','f','g','h','i','j']
#
# chart_data=pd.DataFrame(dataframe,
#                         columns)
#
# st.line_chart(chart_data)

## Adding map data
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
#
# st.map(map_data)

# Widgets
# x =st.slider('x')
# st.write(x,'squared is',x*x)
#
# st.text_input('Your name', key='name')
# st.write('Name:',st.session_state.name)

import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
#
# '''
# # Research Paper Management System
# ### Brought to you by: Suhas K, Srinivaasan N S, Soham Sarkar & Shreya Mandi
# '''
#
# with open('config/auth.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)
#
# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorised']
# )
#
# authenticator.login('Login', 'main')
#
# if st.session_state["authentication_status"]:
#     authenticator.logout('Logout', 'main', key='unique_key')
#     st.write(f'Welcome *{st.session_state["name"]}*')
#     st.title('Some content')
# elif st.session_state["authentication_status"] is False:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] is None:
#     st.warning('Please enter your username and password')