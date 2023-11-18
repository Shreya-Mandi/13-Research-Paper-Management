import login
import register
import projects
import streamlit as st
import newProject
import updateProjects
import json

st.session_state['id'] = None
st.session_state['pwd'] = None
st.session_state['type'] = None
st.session_state['where'] = None
st.session_state['menu'] = None
class Landing:
    def __init__(self):
        # self.id = None
        # self.pwd = None
        # self.type = None
        if 'id' not in st.session_state:
            st.session_state['id']=None
        if 'pwd' not in st.session_state:
            st.session_state['pwd']=None
        if 'type' not in st.session_state:
            st.session_state['type']=None
        if 'where' not in st.session_state:
            st.session_state['where']=None
        if 'menu' not in st.session_state:
            st.session_state['menu'] = None

    def is_logged_in(self):
        if st.session_state['id'] != None and st.session_state['pwd'] != None:
            return 1
        else:
            return 0

    def login_or_register(self):
        st.session_state['menu'] = st.selectbox('Welcome- login, register or use as guest:', ['login', 'register', 'guest'])
        return st.session_state['menu']


    def display_auth_module(self, choice):
        if choice == 'login':
            login_obj = login.Login()
            login_obj.put_streamlit_login()

        if choice == 'register':
            register_obj = register.Register()
            register_obj.put_streamlit_register()
        # else:
        #     # login as guest

# def run_choice():
#     if st.session_state['where']== 'Home':
#         if (not landing_obj.is_logged_in()):
#             ch = landing_obj.login_or_register()
#             landing_obj.display_auth_module(ch)
#
#     elif st.session_state['where']== 'Your Projects':
#
#         projects_obj = projects.GetProjects()
#         projects_obj.put_streamlit_projects()
#
#     # elif st.session_state['where']=='Your Meetings':
#     #     print('your meetings')


# main frame
'''
# Research Paper Management System
'''
landing_obj = Landing()
# if st.session_state['where']== None:

if (not landing_obj.is_logged_in()):
    ch = landing_obj.login_or_register()
    landing_obj.display_auth_module(ch)

'''
Brought to you by: Suhas K, Srinivaasan N S, Soham Sarkar & Shreya Mandi
'''

# sidebar
if st.sidebar.button('Home'):
    st.session_state['where'] = 'Home'
    if (not landing_obj.is_logged_in()):
        ch = landing_obj.login_or_register()
        landing_obj.display_auth_module(ch)

if st.sidebar.button('Your Projects'):
    st.session_state['where'] = 'Your Projects'
    projects_obj = projects.GetProjects()
    choice=projects_obj.put_streamlit_projects()


    if choice == projects_obj.menu_list[0]:
        # existing view
        res_json = projects_obj.get_projects()
        if projects_obj.check_res(res_json):
            projects_obj.display_projects(res_json)
    elif choice == projects_obj.menu_list[1]:
        print('pressed1')
        # new project
        newProject_obj = newProject.NewProject(st.session_state['id'])
        newProject_obj.put_streamlit_newProject()
    elif choice == projects_obj.menu_list[2]:
        # update project
        updateProjects_obj = updateProjects.UpdateProjects(st.session_state['id'])
        updateProjects_obj.put_streamlit_updateProjects()

    elif choice == projects_obj.menu_list[3]:
        # delete project
        num = st.number_input('Enter the project id')

if st.sidebar.button('Your Meetings'):
    st.session_state['where'] = 'Your Meetings'
    # run_choice()

