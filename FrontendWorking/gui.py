import streamlit as st
import pandas as pd
import helper

if 'page' not in st.session_state:
    st.session_state.page = 'login'

print("SESSION_STATE", st.session_state)


def transition_login_dashboard_submit():
    status, error, data = helper.submit_login({
        "id": st.session_state.user_id,
        "pwd": st.session_state.user_pwd
    })
    if status:
        st.session_state.page = 'dashboard'
        st.session_state['user_details'] = {
            'user_id': st.session_state['user_id'],
            'user_type': data['type'],
            'user_name': data['name']
        }
        for key in st.session_state.keys():
            if key not in ['page', 'user_details']:
                del st.session_state[key]
    else:
        st.session_state['error'] = error


def transition_login_register():
    st.session_state.page = 'register'
    for key in st.session_state.keys():
        if key != 'page':
            del st.session_state[key]


def transition_register_login():
    st.session_state.page = 'login'
    for key in st.session_state.keys():
        if key != 'page':
            del st.session_state[key]


def transition_register_login_submit():
    status, error, data = helper.submit_register({
        'id': st.session_state.user_id,
        'pwd': st.session_state.user_pwd,
        'type': st.session_state.user_type,
        'details': {
            'firstName': st.session_state.first_name,
            'lastName': st.session_state.last_name,
            'dept': st.session_state.user_dept,
            'sem': st.session_state.user_sem,
            'sec': st.session_state.user_sec
        } if st.session_state.user_type == 'student' else
        {
            'firstName': st.session_state.first_name,
            'lastName': st.session_state.last_name,
            'dept': st.session_state.user_dept,
            'domain': st.session_state.user_domain
        }
    })
    if status:
        st.session_state.page = 'login'
        for key in st.session_state.keys():
            if key != 'page':
                del st.session_state[key]
    else:
        st.session_state['error'] = error


def transition_dashboard_detailed_view():
    if st.session_state.user_choice:
        st.session_state.page = 'detailed_view'
        del st.session_state.user_details['project_ids']
        st.session_state.user_details['project_id'] = st.session_state.user_choice
        for key in st.session_state.keys():
            if key not in ['page', 'user_details']:
                del st.session_state[key]


def transition_detailed_view_dashboard():
    st.session_state.page = 'dashboard'
    del st.session_state.user_details['project_id']
    for key in st.session_state.keys():
        if key not in ['page', 'user_details']:
            del st.session_state[key]


def login():
    st.title('Login')

    with st.form('login_form'):
        st.text_input('ID:', key="user_id")
        st.text_input('Password:', type="password", key="user_pwd")

        st.form_submit_button('Login', on_click=transition_login_dashboard_submit)

        if 'error' in st.session_state:
            st.write(st.session_state.error)
            del st.session_state.error

    st.button('Register', on_click=transition_login_register)


def register():
    st.title('Register')

    with st.form('register_form'):

        st.text_input('ID:', key="user_id")
        st.text_input('First Name:', key="first_name")
        st.text_input('Last Name:', key="last_name")
        st.text_input('Password:', type="password", key="user_pwd")
        st.text_input('Re-enter Password:', type="password", key="re_user_pwd")
        user_type = st.selectbox('Select type of User:', ['student', 'faculty'], key="user_type")
        st.selectbox('Department:', ['CSE', 'ECE', 'EEE', 'AIML', 'ME'], key="user_dept")

        if user_type == 'student':
            st.number_input('Semester:', min_value=1, max_value=8, key="user_sem")
            st.text_input('Section:', key="user_sec")

        if user_type == 'faculty':
            st.text_input('Domain:', key="user_domain")

        st.form_submit_button('Register', on_click=transition_register_login_submit)

        if 'error' in st.session_state:
            st.write(st.session_state.error)
            del st.session_state.error

    st.button('Login', on_click=transition_register_login)


def dashboard():
    user_id = st.session_state.user_details['user_id']
    user_type = st.session_state.user_details['user_type']
    user_name = st.session_state.user_details['user_name']

    st.session_state.user_details['project_ids'] = []

    st.title('Dashboard')
    st.write("Welcome, ", user_name)

    req = dict()
    req['id'] = user_id
    req['type'] = user_type
    status, error, data = helper.submit_getProjects(req)
    if status:
        st.write('Projects')
        if not data['projects']:
            st.write('No existing projects')
        else:
            df = pd.DataFrame(data=data['projects'], columns=data['projects'][0].keys())
            df2 = df[['projectID',
                      'projectTitle',
                      'projectStatus']]

            df3_f = []
            df3_s = []
            for i in df['faculty']:
                temp = []
                for j in i:
                    temp.append(j['name'])
                df3_f.append(', '.join(temp))

            for i in df['student']:
                temp = []
                for j in i:
                    temp.append(j['name'])
                df3_s.append(', '.join(temp))

            df2['faculty'] = df3_f
            df2['student'] = df3_s

            st.dataframe(df2)

            st.session_state.user_details['project_ids'] = list(df['projectID'])
    else:
        st.write(error)

    with st.form('get-detailed-view'):
        st.selectbox('Select Which Project you need',
                     st.session_state.user_details['project_ids'],
                     key="user_choice")

        st.form_submit_button('Get Detailed Info', on_click=transition_dashboard_detailed_view)


def detailed_view():
    st.title("Detailed View")
    st.write(st.session_state.user_details['project_id'])

    req = dict()
    req['projectID'] = st.session_state.user_details['project_id']
    status, error, data = helper.submit_getProjectDetailed(req)
    if status:
        title = data['details']['projectTitle']
        proj_status = data['details']['projectStatus']
        start_data = data['details']['startDate']
        end_date = data['details']['endDate']

        l = data['details']['faculty']
        temp = []
        for i in l:
            temp.append(i['name'])
        fac_st = ', '.join(temp)

        l = data['details']['student']
        temp = []
        for i in l:
            temp.append(i['name'])
        stu_st = ', '.join(temp)

        st.write("Title:", title)
        st.write("Faculty:", fac_st)
        st.write("Students:", stu_st)
        st.write("Status:", proj_status)
        st.write("Start Date:", start_data)
        st.write("End Date:", end_date)

        st.write('Faculty suggestions:')
        status_sug, error_sug, data_sug = helper.submit_getSuggestions(req)
        if status_sug:
            if not data_sug['suggestions']:
                st.write('No existing suggestions!!!!!!!!!!!!')
            else:
                l = data_sug['suggestions']
                df = pd.DataFrame(data=l, columns=l[0].keys())
                st.dataframe(df)
        else:
            st.write(error_sug)

        st.write('Meetings:')
        status_meeting, error_meeting, data_meeting = helper.submit_getMeetings(req)

        if status_meeting:
            if not data_meeting['meetings']:
                st.write('No existing meetings!!!!!!!!!!!')
            else:
                l = data_meeting['meetings']
                df = pd.DataFrame(data=l, columns=l[0].keys())
                st.dataframe(df)
    else:
        st.write(error)

    st.button("Go Back", on_click=transition_detailed_view_dashboard)


if st.session_state['page'] == 'login':
    login()
elif st.session_state['page'] == 'register':
    register()
elif st.session_state['page'] == 'dashboard':
    dashboard()
elif st.session_state['page'] == 'detailed_view':
    detailed_view()
