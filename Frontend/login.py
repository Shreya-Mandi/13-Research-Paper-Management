import streamlit as st
import requests
import webbrowser

'''
# Research Paper Management System
'''

# Streamlit input
st.session_state['name']= st.text_input('Name')
st.session_state['password']=st.text_input('Password')

#API post call
response=requests.post("http://localhost:6969/Login/",
                       json={
                           'usrName':st.session_state['name'],
                           'usrPwd':st.session_state['password']
                       })

print(response.json())

res_json=response.json()
if res_json['valid']==True:
    st.write('Successful login')
    link2 = 'http://localhost:8503'

    if st.button('My projects'):
        webbrowser.open_new_tab(link2)

link = 'http://localhost:8502'

if st.button('Register'):
    webbrowser.open_new_tab(link)

'''
### Brought to you by: Suhas K, Srinivaasan N S, Soham Sarkar & Shreya Mandi
'''