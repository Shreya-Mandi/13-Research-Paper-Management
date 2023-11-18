import streamlit as st
import requests
import webbrowser


class Login:
    def __init__(self):
        self.id=st.session_state['id']
        self.pwd=st.session_state['pwd']
        self.type=None
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
            self.id = st.session_state['id']
            self.pwd = st.session_state['pwd']

            res_json = response.json()

            return res_json

    def check_res(self,res_json):
        if res_json['status'] == True:
            st.session_state['type'] = res_json['type']
            self.type=res_json['type']
            st.write('Successful login')

        else:
            if res_json['invalidRequest'] == True:
                print('Login request is invalid')
            else:
                print('Internal server error on login')
                print(res_json['errMsg'])

    def save_login(self):
        if self.id and self.pwd and self.type:
            return(self.id,self.pwd,self.type)
        else:
            return 0


    def put_streamlit_login(self):

        # Streamlit input
        st.session_state['id'] = st.text_input('ID:')
        st.session_state['pwd'] = st.text_input('Password:')


        # login button
        if st.button('Login'):
            res_json=self.submit()
            if res_json:
                self.check_res(res_json)



