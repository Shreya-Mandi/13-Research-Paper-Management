import streamlit as st
import requests
import json


class Login:
    def __init__(self):
        # self.id = None
        # self.pwd = None
        # self.type = None

        if 'id' not in st.session_state:
            self.id = st.session_state['id'] = None
        if 'pwd' not in st.session_state:
            self.pwd = st.session_state['pwd'] = None
        if 'type' not in st.session_state:
            self.type = st.session_state['type'] = None

    def check_constraints(self):
        # constraint checks
        if len(st.session_state['id']) != 13:
            st.write('Invalid name')
            return False
        return True

    def submit(self):
        if (self.check_constraints()):
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

            print('now save login')
            self.save_login()

            return res_json

    def check_res(self,res_json):
        if res_json['status'] == True:

            st.write('Successful login')

        else:
            if res_json['invalidRequest'] == True:
                print('Login request is invalid')
            else:
                print('Internal server error on login')
                print(res_json['errMsg'])


    def save_login(self):
        # if self.id and self.pwd and self.type:
        with open('my_info.json','w') as file:
            print('in the loop')
            my_login={
                'id':st.session_state['id'],
                'pwd':st.session_state['pwd'],
                'type':st.session_state['type']
            }
            json.dump(my_login,file)
        return(st.session_state['id'],
                st.session_state['pwd'],
                st.session_state['type'])
        # else:
        #     return 0

    def put_streamlit_login(self):
        with st.form('login_form'):
            # Streamlit input
            st.session_state['id'] = st.text_input('ID:')
            st.session_state['pwd'] = st.text_input('Password:')


            # login button
            if st.form_submit_button('Login'):
                res_json=self.submit()
                if res_json:
                    self.check_res(res_json)



