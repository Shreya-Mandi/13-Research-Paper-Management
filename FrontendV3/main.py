import streamlit as st
import requests
import helper

placeholder_login=st.empty()
with placeholder_login.container():
    with st.form('login_form'):
        # Streamlit input
        st.session_state['id'] = st.text_input('ID:')
        st.session_state['pwd'] = st.text_input('Password:')

        # login button
        if st.form_submit_button('Login'):
            res_json = helper.submit_login()
            if res_json:
               helper.check_res_login(res_json)
            placeholder_login.empty()
    for i,v in st.session_state.items():
        print(i,v)
#
#     bt=st.button('Clear')
#
# if bt:
#     for i, v in st.session_state.items():
#         print(i, v)
#     placeholder_login.empty()
