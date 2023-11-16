import streamlit as st
import requests
import webbrowser

'''
# Research Paper Management System
'''

# Streamlit input
st.session_state['name']= st.text_input('ID:')
st.session_state['password']=st.text_input('Password:')


def check_constraints():
    # constraint checks
    if len(st.session_state['name']) != 10:
        st.write('Invalid name')
        return False
    return True
def submit():
    if(check_constraints()):
        #API post call
        print('sending login post request')
        response=requests.post("http://localhost:3002/Login/",
                               json={
                                   'id':st.session_state['name'],
                                   'pwd':st.session_state['password']
                               })


        print('response received for login post')

        res_json=response.json()

        return res_json


def check_res(res_json):
    if res_json['status']==True:
        st.session_state['type']=res_json['type']
        st.write('Successful login')

    if st.button('My projects'):
        webbrowser.open_new_tab("http://localhost:3002/GetProjects/")
    else:
        if res_json['invalidRequest']==True:
            print('Login equest is invalid')
        else:
            print('Internal server error on login')
            print(res_json['errMsg'])

# login button
if st.button('Login'):
    res_json=submit()
    check_res(res_json)

# register button
st.write('Do not have an account?')
if st.button('Register'):
    webbrowser.open_new_tab("http://localhost:3002/Register/")

# View as guest
st.write('Not a member?')
if st.button('Login as guest'):
    st.write('Redirect to guest view')

'''
Brought to you by: Suhas K, Srinivaasan N S, Soham Sarkar & Shreya Mandi
'''