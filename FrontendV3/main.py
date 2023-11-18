import streamlit as st
import helper

ph = st.empty()


def login():
    with ph.container():
        st.title('Login')

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

        if st.button('Register'):
            ph.empty()
            register()


def register():
    pass


def dashboard(user_id, user_type, user_name):
    with ph.container():
        st.title('Dashboard')
        st.write('Welcome,', user_name)


login()
