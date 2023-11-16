import streamlit as st
import requests
import webbrowser

'''
# Research Paper Management System
'''

# Streamlit input
st.session_state['details']=dict()
st.session_state['id']=st.text_input('ID:')
st.session_state['details']['firstName'] = st.text_input('First Name')
st.session_state['details']['lastName']=st.text_input('Last Name')
st.session_state['password'] = st.text_input('Password')
st.session_state['password_re'] = st.text_input('Re-enter Password')
st.session_state['type'] = st.selectbox('Pick one:', ['student', 'faculty'])
st.session_state['details']['dept']= st.radio('Department:',['CSE','ECE','EEE','AI/ML','ME'])
if st.session_state['type']=='student':
    st.session_state['details']['sem']=st.number_input(label='Semester:',min_value=1,max_value=8)
    st.session_state['details']['sec']=st.select_slider(label='Section:', options=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
if st.session_state['type']=='faculty':
    st.session_state['details']['domain']= st.selectbox('Domain:',['DA','NLP','LLM','SYS','EEE','GT','others'])

def check_constraints():
    if st.session

def submit():
    # API post call
    response = requests.post("http://localhost:6969/Register/",
                             json={
                                 'id': st.session_state['id'],
                                 'pwd': st.session_state['password'],
                                 'type': st.session_state['type'],
                                 'details': st.session_state['details']
                             })

    res_json = response.json()

def check_res(res_json):
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
