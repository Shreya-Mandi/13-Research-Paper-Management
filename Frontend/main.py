import login
import register
import projects
import streamlit as st


class Landing:
    def __init__(self):
        self.id = None
        self.pwd = None
        self.type = None
        st.session_state['id'] = None
        st.session_state['pwd'] = None

    def is_logged_in(self):
        if self.id != None and self.pwd != None:
            return 1
        else:
            return 0

    def login_or_register(self):
        choice = st.selectbox('Welocome, login, register or use as guest:', ['login', 'register', 'guest'])
        print(choice)
        return choice

    def display_auth_module(self, choice):
        if choice == 'login':
            login_obj = login.Login()
            login_obj.put_streamlit_login()
            if login_obj.save_login():
                self.id, self.pwd, self.type = login_obj.save_login()
            print(self.id, self.pwd, self.type)

        if choice == 'register':
            register_obj = register.Register()
            register_obj.put_streamlit_register()
        # else:
        #     # login as guest

def run_choice():
    if choose_menu == None or choose_menu == 'Home':
        if (not landing_obj.is_logged_in()):
            ch = landing_obj.login_or_register()
            landing_obj.display_auth_module(ch)

    elif choose_menu == 'Your Projects':
        print('your projects')
        projects_obj = projects.GetProjects(landing_obj.id, landing_obj.type)
        projects_obj.put_streamlit_projects()


choose_menu = None

# main frame
'''
# Research Paper Management System
'''
landing_obj = Landing()

'''
Brought to you by: Suhas K, Srinivaasan N S, Soham Sarkar & Shreya Mandi
'''

# sidebar
if st.sidebar.button('Home'):
    choose_menu='Home'
    run_choice()

if st.sidebar.button('Your Projects'):
    choose_menu='Your Projects'
    run_choice()