import streamlit as st
import requests
import webbrowser

'''
# Research Paper Management System
'''

# Streamlit input
st.session_state['name'] = st.text_input('First name')
st.session_state['type'] = st.radio('Pick one:', ['student', 'faculty'])
st.session_state['password'] = st.text_input('Password')
st.session_state['password_re'] = st.text_input('Re-enter Password')

# API post call
response = requests.post("http://localhost:6969/Register/",
                         json={
                             'usrName': st.session_state['name'],
                             'usrPwd': st.session_state['password'],
                             'type': st.session_state['type']
                         })

res_json = response.json()
if res_json['status'] == True:
    if st.session_state['password'] == st.session_state['password_re']:
        st.write('Successful register')

print(res_json)
link = 'http://localhost:8501'

if st.button('Login'):
    webbrowser.open_new_tab(link)

'''
### Brought to you by: Suhas K, Srinivaasan N S, Soham Sarkar & Shreya Mandi
'''
