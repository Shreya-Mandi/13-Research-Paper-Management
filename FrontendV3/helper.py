import streamlit as st
import requests
def check_constraints_login():
    # constraint checks
    if len(st.session_state['id']) != 13:
        st.write('Invalid name')
        return False
    return True


def submit_login():
    if (check_constraints_login()):
        # API post call
        print('sending login post request')
        response = requests.post("http://localhost:3002/Login/",
                                 json={
                                     'id': st.session_state['id'],
                                     'pwd': st.session_state['pwd']
                                 })

        print('Response received for login')

        res_json = response.json()

        st.session_state['type'] = res_json['type']

        # print('now save login')
        # self.save_login()

        return res_json


def check_res_login(res_json):
    if res_json['status'] == True:

        st.write('Successful login')

    else:
        if res_json['invalidRequest'] == True:
            print('Login request is invalid')
        else:
            print('Internal server error on login')
            print(res_json['errMsg'])