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


def transition_login_dashboard_guest():
    st.session_state.page = 'dashboard'
    st.session_state['user_details'] = {
        'user_id': '',
        'user_type': 'guest',
        'user_name': 'guest'
    }
    for key in st.session_state.keys():
        if key not in ['page', 'user_details']:
            del st.session_state[key]


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
        st.session_state.user_details['project_id'] = st.session_state.user_choice
        for key in st.session_state.keys():
            if key not in ['page', 'user_details']:
                del st.session_state[key]


def transition_detailed_view_dashboard():
    st.session_state.page = 'dashboard'
    del st.session_state.user_details['project_id']
    del st.session_state.user_details['project_start_date_copy']
    for key in st.session_state.keys():
        if key not in ['page', 'user_details']:
            del st.session_state[key]


def transition_detailed_view_dashboard_submit():
    status, error, data = helper.submit_delProject({
        "projectID": st.session_state.user_details['project_id'],
    })
    if status:
        st.session_state.page = 'dashboard'
        del st.session_state.user_details['project_id']
        del st.session_state.user_details['project_start_date_copy']
        for key in st.session_state.keys():
            if key not in ['page', 'user_details']:
                del st.session_state[key]
    else:
        st.session_state['error'] = error


def transition_dashboard_create_project():
    st.session_state.page = 'create_project'
    for key in st.session_state.keys():
        if key not in ['page', 'user_details']:
            del st.session_state[key]


def transition_create_project_dashboard():
    st.session_state.page = 'dashboard'
    for key in st.session_state.keys():
        if key not in ['page', 'user_details']:
            del st.session_state[key]


def transition_create_project_dashboard_submit():
    req = {
        "projectTitle": st.session_state['project_title'],
        "projectStatus": st.session_state['project_status'],
        "startDate": st.session_state['project_start_date'].strftime("%Y-%m-%d"),
        "facultyID": st.session_state['faculty_ids'],
        "studentID": st.session_state['student_ids']
    }

    if st.session_state['project_end_date']:
        req["endDate"] = st.session_state['project_end_date'].strftime("%Y-%m-%d")

    status, error, data = helper.submit_newProject(req)
    if status:
        st.session_state.page = 'dashboard'
        for key in st.session_state.keys():
            if key not in ['page', 'user_details']:
                del st.session_state[key]
    else:
        st.session_state['error'] = error


def transition_detailed_view_update_project():
    st.session_state.page = 'update_project'
    for key in st.session_state.keys():
        if key not in ['page', 'user_details']:
            del st.session_state[key]


def transition_update_project_detailed_view():
    st.session_state.page = 'detailed_view'
    for key in st.session_state.keys():
        if key not in ['page', 'user_details']:
            del st.session_state[key]


def transition_update_project_detailed_view_submit():
    req = {
        "projectID": st.session_state.user_details['project_id']
    }

    if st.session_state['project_title']:
        req["projectTitle"] = st.session_state['project_title']

    if st.session_state['project_status']:
        req["projectStatus"] = st.session_state['project_status']

    if st.session_state['project_start_date']:
        req["startDate"] = st.session_state['project_start_date'].strftime("%Y-%m-%d")

    if st.session_state['project_end_date']:
        if st.session_state['project_start_date']:
            req["startDate"] = st.session_state['project_start_date'].strftime("%Y-%m-%d")
        else:
            req["startDate"] = st.session_state.user_details['project_start_date_copy']
        req["endDate"] = st.session_state['project_end_date'].strftime("%Y-%m-%d")

    if st.session_state['faculty_ids']:
        req["facultyID"] = st.session_state['faculty_ids']

    if st.session_state['student_ids']:
        req["studentID"] = st.session_state['student_ids']

    status, error, data = helper.submit_updateProject(req)
    if status:
        st.session_state.page = 'detailed_view'
        for key in st.session_state.keys():
            if key not in ['page', 'user_details']:
                del st.session_state[key]
    else:
        st.session_state['error'] = error


def transition_detailed_view_request_meeting():
    st.session_state.page = 'request_meeting'
    for key in st.session_state.keys():
        if key not in ['page', 'user_details']:
            del st.session_state[key]


def transition_request_meeting_detailed_view():
    st.session_state.page = 'detailed_view'
    for key in st.session_state.keys():
        if key not in ['page', 'user_details']:
            del st.session_state[key]


def transition_request_meeting_detailed_view_submit():
    status, error, data = helper.submit_newMeeting({
        "projectID": st.session_state.user_details['project_id'],
        "startTime": st.session_state['start_date'].strftime("%Y-%m-%d") + \
                     st.session_state['start_time'].strftime(" %H:%M:%S"),
        "endTime": st.session_state['end_date'].strftime("%Y-%m-%d") + \
                   st.session_state['end_time'].strftime(" %H:%M:%S"),
        "link": st.session_state['link'],
        "remarks": st.session_state['remarks']
    })
    if status:
        st.session_state.page = 'detailed_view'
        for key in st.session_state.keys():
            if key not in ['page', 'user_details']:
                del st.session_state[key]
    else:
        st.session_state['error'] = error


def transition_detailed_view_update_meeting():
    st.session_state.page = 'update_meeting'
    st.session_state.user_details['meeting_id'] = st.session_state.user_choice
    st.session_state.user_details['meeting_start_date_time_copy'] = \
        st.session_state['meeting_timings'][st.session_state.user_choice]

    for key in st.session_state.keys():
        if key not in ['page', 'user_details']:
            del st.session_state[key]


def transition_update_meeting_detailed_view():
    st.session_state.page = 'detailed_view'
    del st.session_state.user_details['meeting_id']
    del st.session_state.user_details['meeting_start_date_time_copy']
    for key in st.session_state.keys():
        if key not in ['page', 'user_details']:
            del st.session_state[key]


def transition_update_meeting_detailed_view_submit():
    req = {
        "meetingID": st.session_state.user_details['meeting_id']
    }

    if (st.session_state['start_date'] and not st.session_state['start_time']) or \
            (not st.session_state['start_date'] and st.session_state['start_time']):
        st.session_state['error'] = 'Invalid start timestamp, both start date and start time should be filled'
        return

    if (st.session_state['end_date'] and not st.session_state['end_time']) or \
            (not st.session_state['end_date'] and st.session_state['end_time']):
        st.session_state['error'] = 'Invalid end timestamp, both end date and end time should be filled'
        return

    if st.session_state['start_date'] and st.session_state['start_time']:
        req["startTime"] = st.session_state['start_date'].strftime("%Y-%m-%d") + \
                           st.session_state['start_time'].strftime(" %H:%M:%S")

    if st.session_state['end_date'] and st.session_state['end_time']:
        if st.session_state['start_date'] and st.session_state['start_time']:
            req["startTime"] = st.session_state['start_date'].strftime("%Y-%m-%d") + \
                               st.session_state['start_time'].strftime(" %H:%M:%S")
        else:
            req["startTime"] = st.session_state.user_details['meeting_start_date_time_copy']
        req["endTime"] = st.session_state['end_date'].strftime("%Y-%m-%d") + \
                         st.session_state['end_time'].strftime(" %H:%M:%S")

    if st.session_state['link']:
        req["link"] = st.session_state['link']

    if st.session_state['remarks']:
        req["remarks"] = st.session_state['remarks']

    status, error, data = helper.submit_updateMeeting(req)
    if status:
        st.session_state.page = 'detailed_view'
        del st.session_state.user_details['meeting_id']
        del st.session_state.user_details['meeting_start_date_time_copy']
        for key in st.session_state.keys():
            if key not in ['page', 'user_details']:
                del st.session_state[key]
    else:
        st.session_state['error'] = error


def transition_logout():
    for key in st.session_state.keys():
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

    st.button('Login as Guest', on_click=transition_login_dashboard_guest)


def register():
    st.title('Register')

    user_type = st.selectbox('Select type of User:', ['student', 'faculty'], index=0, key="user_type")

    with st.form('register_form'):

        st.text_input('ID:', key="user_id")
        st.text_input('First Name:', key="first_name")
        st.text_input('Last Name:', key="last_name")
        st.text_input('Password:', type="password", key="user_pwd")
        st.selectbox('Department:', ['CSE', 'ECE', 'EEE', 'AIML', 'ME'], key="user_dept")

        if user_type == 'student':
            st.number_input('Semester:', value=0, key="user_sem")
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

    st.session_state['project_ids'] = []

    st.title('Dashboard')
    st.write("Welcome, ", user_name)

    if user_type != 'guest':
        status, error, data = helper.submit_getProjects({
            'id': user_id,
            'type': user_type
        })
    else:
        status, error, data = helper.submit_getProjects({
            'type': 'guest'
        })

    if status:
        st.write('Projects')
        if not data['projects']:
            st.write('No Existing Projects')
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

            st.session_state['project_ids'] = list(df['projectID'])
    else:
        st.write(error)

    with st.form('get-detailed-view'):
        st.selectbox('Select Which Project You Need',
                     st.session_state['project_ids'],
                     key="user_choice")

        st.form_submit_button('Get Detailed Info', on_click=transition_dashboard_detailed_view)

    if user_type != 'guest':
        st.button("Create Project", on_click=transition_dashboard_create_project)
    else:
        st.info("PES CONTACT DETAILS", icon="ℹ️")

    st.button("Logout", on_click=transition_logout)


def detailed_view():
    st.title("Detailed View")
    st.write(st.session_state.user_details['project_id'])

    req = dict()
    req['projectID'] = st.session_state.user_details['project_id']
    status, error, data = helper.submit_getProjectDetailed(req)
    if status:
        title = data['details']['projectTitle']
        proj_status = data['details']['projectStatus']
        st.session_state.user_details['project_start_date_copy'] = start_data = data['details']['startDate']
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

        if st.session_state.user_details['user_type'] != 'guest':
            st.write('Faculty suggestions:')
            status_sug, error_sug, data_sug = helper.submit_getSuggestions(req)
            if status_sug:
                if not data_sug['suggestions']:
                    st.write('No Existing Suggestions')
                else:
                    l = data_sug['suggestions']
                    df = pd.DataFrame(data=l, columns=l[0].keys())
                    st.dataframe(df)

                    if st.session_state.user_details['user_type'] == "faculty":
                        with st.form('add suggestion'):
                            suggestion = st.text_input('Enter Suggestion:')
                            if st.form_submit_button('Add'):
                                status, error, data = helper.submit_newSuggestion({
                                    "projectID": st.session_state.user_details['project_id'],
                                    "facultyID": st.session_state.user_details['user_id'],
                                    "suggestion": suggestion
                                })
                                if status:
                                    st.rerun()
                                else:
                                    st.write(error)
            else:
                st.write(error_sug)

            st.write('Meetings:')
            status_meeting, error_meeting, data_meeting = helper.submit_getMeetings(req)

            if status_meeting:
                if not data_meeting['meetings']:
                    st.write('No Existing Meetings')
                else:
                    l = data_meeting['meetings']
                    df = pd.DataFrame(data=l, columns=l[0].keys())
                    st.dataframe(df)

                    st.session_state['meeting_timings'] = {}
                    requested_meeting_ids = []
                    for item in l:
                        st.session_state['meeting_timings'][item['id']] = item['startTime']
                        if item['status'] == "Requested":
                            requested_meeting_ids.append(item['id'])

                    with st.form('Update Meeting'):
                        st.selectbox('Select Which Meeting to update', df['id'], key="user_choice")
                        st.form_submit_button('Update Meeting', on_click=transition_detailed_view_update_meeting)

                    if st.session_state.user_details['user_type'] == "faculty":
                        with st.form('ack meeting'):
                            meeting_id = st.selectbox('Select Which Meeting to Acknowledge', requested_meeting_ids)
                            meeting_status = st.selectbox('', ['Accepted', 'Rejected'])
                            if st.form_submit_button('Update'):
                                status, error, data = helper.submit_updateMeeting({
                                    "meetingID": meeting_id,
                                    "status": meeting_status
                                })
                                if status:
                                    st.rerun()
                                else:
                                    st.write(error)

    else:
        st.write(error)

    if st.session_state.user_details['user_type'] != 'guest':
        st.button("Update Project", on_click=transition_detailed_view_update_project)

        st.button("Delete Project", on_click=transition_detailed_view_dashboard_submit)

        if 'error' in st.session_state:
            st.write(st.session_state.error)
            del st.session_state.error

    if st.session_state.user_details['user_type'] == "student":
        st.button("Request Meeting", on_click=transition_detailed_view_request_meeting)

    st.button("Go Back", on_click=transition_detailed_view_dashboard)


def create_project():
    st.title("Create Project")

    with st.form('newProject'):
        status_users, error_users, data_users = helper.submit_getUsers()
        if status_users:
            st.text_input('Project Title:', key="project_title")
            st.selectbox('Project Status:', ["Published", "Ongoing"], key="project_status")
            st.date_input('Project Start Date:', key="project_start_date")
            st.date_input('Project End Date:', value=None, key="project_end_date")

            st.multiselect('Faculty ID:', [x['id'] for x in data_users['facultyID']], key="faculty_ids")
            st.multiselect('Student ID:', [x['srn'] for x in data_users['studentID']], key="student_ids")

            st.form_submit_button('Create New Project', on_click=transition_create_project_dashboard_submit)

            if 'error' in st.session_state:
                st.write(st.session_state.error)
                del st.session_state.error

        else:
            st.write(error_users)

    st.button("Go Back", on_click=transition_create_project_dashboard)


def update_project():
    st.title("Update Project")

    with st.form('updateProject'):
        status_users, error_users, data_users = helper.submit_getUsers()
        if status_users:
            st.text_input('Project Title:', key="project_title")
            st.selectbox('Project Status:', ["Published", "Ongoing"], key="project_status")
            st.date_input('Project Start Date:', value=None, key="project_start_date")
            st.date_input('Project End Date:', value=None, key="project_end_date")

            st.multiselect('Faculty ID:', [x['id'] for x in data_users['facultyID']], key="faculty_ids")
            st.multiselect('Student ID:', [x['srn'] for x in data_users['studentID']], key="student_ids")

            st.form_submit_button('Update Project', on_click=transition_update_project_detailed_view_submit)

            if 'error' in st.session_state:
                st.write(st.session_state.error)
                del st.session_state.error
        else:
            st.write(error_users)

    st.button("Go Back", on_click=transition_update_project_detailed_view)


def request_meeting():
    st.title("Request Meeting")

    with st.form('requestMeeting'):
        st.date_input('Meeting Start Date:', key="start_date")
        st.time_input('Meeting Start Time:', key="start_time")
        st.date_input('Meeting End Date:', key="end_date")
        st.time_input('Meeting End Time:', key="end_time")

        st.text_input('Link:', placeholder='http:// or https://', key="link")
        st.text_input('Remarks:', key="remarks")

        st.form_submit_button('Request New Meeting', on_click=transition_request_meeting_detailed_view_submit)

        if 'error' in st.session_state:
            st.write(st.session_state.error)
            del st.session_state.error

    st.button("Go Back", on_click=transition_request_meeting_detailed_view)


def update_meeting():
    st.title("Update Meeting")

    with st.form('updateMeeting'):
        st.date_input('Meeting Start Date:', value=None, key="start_date")
        st.time_input('Meeting Start Time:', value=None, key="start_time")
        st.date_input('Meeting End Date:', value=None, key="end_date")
        st.time_input('Meeting End Time:', value=None, key="end_time")

        st.text_input('Link:', placeholder='http:// or https://', key="link")
        st.text_input('Remarks:', key="remarks")

        st.form_submit_button('Update Meeting', on_click=transition_update_meeting_detailed_view_submit)

        if 'error' in st.session_state:
            st.write(st.session_state.error)
            del st.session_state.error

    st.button("Go Back", on_click=transition_update_meeting_detailed_view)


if st.session_state['page'] == 'login':
    login()
elif st.session_state['page'] == 'register':
    register()
elif st.session_state['page'] == 'dashboard':
    dashboard()
elif st.session_state['page'] == 'detailed_view':
    detailed_view()
elif st.session_state['page'] == 'create_project':
    create_project()
elif st.session_state['page'] == 'update_project':
    update_project()
elif st.session_state['page'] == 'request_meeting':
    request_meeting()
elif st.session_state['page'] == 'update_meeting':
    update_meeting()
