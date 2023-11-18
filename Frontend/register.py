import streamlit as st
import requests
import webbrowser

class Register:

    def get_register_info(self):

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

    def check_constraints(self):
        # constraint checks
        if st.session_state['type']=='student':
            if len(st.session_state['id']) != 10:
                st.write('Invalid name')
                return False
        else:
            if len(st.session_state['id']) != 8:
                st.write('Invalid name')
                return False
        if st.session_state['password']==st.session_state['password_re']:
            return True
        else:
            st.write('Passwords entered do not match!')
            return False

    def submit(self):
        if(self.check_constraints()):
            print('Sending register request')
            # API post call
            response = requests.post("http://localhost:6969/Register/",
                                     json={
                                         'id': st.session_state['id'],
                                         'pwd': st.session_state['password'],
                                         'type': st.session_state['type'],
                                         'details': st.session_state['details']
                                     })

            res_json = response.json()
            if(res_json):
                print('register res_json received')
            return res_json
        else:
            print('Register passwords did not match')

    def clear_cache(self):
        for key in st.session_state.keys():
            del st.session_state[key]

    def check_res(self,res_json):
        if res_json['status'] == True:
            self.clear_cache()
            st.write('Successful register, please login to continue')
        else:
            if res_json['invalidRequest']==True:
                print('Register module incorrect request made')
            else:
                print('Register module- internal server error')
                print(res_json['errMsg'])

    def put_streamlit_register(self):
        self.get_register_info()

        # register button
        if st.button('Register'):
            res_json=self.submit()
            if res_json:
             self.check_res(res_json)

# # login button
# st.write('Already have an account?')
# if st.button('Login'):
#     st.write('redirect to login')
#     # webbrowser.open_new_tab("http://localhost:3002/Register/")
#
# # View as guest
# st.write('Not a member?')
# if st.button('Login as guest'):
#     st.write('Redirect to guest view')
#     # webbrowser.open_new_tab("http://localhost:3002/Register/")

'''
Brought to you by: Suhas K, Srinivaasan N S, Soham Sarkar & Shreya Mandi
'''
