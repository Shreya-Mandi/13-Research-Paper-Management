import streamlit as st
import helper

ph = st.empty()


def login():
    with ph.container():
        with st.form('login_form'):
            user_id = st.text_input('ID:')
            user_pwd = st.text_input('Password:')

            if st.form_submit_button('Login'):
                status, error, data = helper.submit_login(user_id, user_pwd)
                if status:
                    ph.empty()
                    dashboard(user_id, data['type'], data['name'])
                else:
                    st.write(error)


def dashboard(user_id, user_type, user_name):
    with ph.container():
        st.write("Welcome, ", user_id, user_type, user_name)

def register():
    with ph.container():
        with st.form('register_form'):
            details = dict()
            id = st.text_input('ID:')
            details['firsName'] = st.text_input('First Name')
            details['lastName'] = st.text_input('Last Name')
            password = st.text_input('Password')
            password_re = st.text_input('Re-enter Password')
            type= st.selectbox('Pick one:', ['student', 'faculty'])
            details['dept'] = st.radio('Department:', ['CSE', 'ECE', 'EEE', 'AI/ML', 'ME'])
            if type == 'student':
                details['sem'] = st.number_input(label='Semester:', min_value=1, max_value=8)
                details['sec'] = st.select_slider(label='Section:', options=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

            if type == 'faculty':
                details['domain'] = st.selectbox('Domain:',['DA', 'NLP', 'LLM', 'SYS', 'EEE', 'GT', 'others'])

        if st.form_submit_button('Register'):
                status, error, data = helper.submit_login(id, password, type, details)
                if status:
                    ph.empty()
                    dashboard(user_id, data['type'], data['name'])
                else:
                    st.write(error)

login()
