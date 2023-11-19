import streamlit as st
import helper
import pandas as pd
import datetime

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
            details['firstName'] = st.text_input('First Name')
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
                req=dict()
                req['id']=id
                req['password']=password
                req['type']=type
                req['details']=details
                status, error, data = helper.submit_register(req)
                if status:
                    ph.empty()
                    # dashboard2(id,type)
                    st.write('Redirect to Login Page')
                else:
                    print(data)
                    st.write(error)

# def dashboard2(id,type):
#     with ph.container():
#         st.write("Welcome, successfully registered user")

def getProjects(id,type):
    with ph.container():
        with st.form('getProjects'):

            if st.form_submit_button('View Existing Projects'):
                req=dict()
                req['id']=id
                req['type']=type
                status, error, data = helper.submit_getProjects(req)
                if status:
                    ph.empty()
                    st.print('Redirect to print the project dashboard')
                    dashboard3(data)
                else:
                    st.write(error)
def dashboard3(data):
    with ph.container():
        if (data['projects'] == []):
            st.write('no existing projects')
        else:

            df = pd.DataFrame(data=data['projects'], columns=data['projects'][0].keys())
            # df2 = df[['projectID',
            #             'projectTitle',
            #             'projectStatus'
            #             ]]
            # df3=pd.DataFrame()
            # df31=[]
            # df32=[]
            # for i in df['faculty']:
            #     temp=[]
            #     for j in i:
            #         temp.append(j['name'])
            #     df31.append(' '.join(j))
            # for i in df['student']:
            #     temp=[]
            #     for j in i:
            #         temp.append(j['name'])
            #     df32.append(' '.join(j))
            # df2['faculty']=df31
            # df2['student']=df32
            st.dataframe(df)

def newProject(id,type):
    with ph.container():
        with st.form('newProject'):
            req=dict()
            req['projectTitle']= st.text_input('Project Title:')
            req['projectStatus'] = st.text_input('Project Status:')
            req['startDate'] = st.date_input('Project Start Date:')
            req['endDate'] = st.date_input('Project End Date:')
            req['facultyID'] = st.radio('Faculty ID:',
                                                     ['Dr.Bharathi', 'Dr. Sudeepa', 'Dr. Charu', 'Dr. Prajwala'])
            req['students_num'] = st.number_input('Student members number:', min_value=1, max_value=4)
            req['studentID'] = list()

            for i in range(req['students_num']):
                req['studentID'].append(st.text_input(f'Enter the student id{i + 1}'))

            if st.form_submit_button('Create New Project'):
                status, error, data = helper.submit_newProject(req)
                if status:
                    ph.empty()
                    dashboard4(data)
                else:
                    st.write(error)
def dashboard4(data):
    with ph.container():
        st.write("Successfully created new project")

def requestMeeting():
    with ph.container():
        with st.form('requestMeeting'):
            req=dict()
            start_date = st.date_input('Project Start Date:')
            start_time = st.time_input('Project Start Date:')
            end_date = st.date_input('Project End Date:')
            end_time = st.time_input('Project End Date:')

            req['projectID'] = st.number_input('ProjectID', min_value=1)

            req['link'] = st.text_input('Link:', placeholder='http or https://')
            req['remarks'] = st.text_input('Remarks:')

            req['startTime'] = datetime.datetime.combine(start_date, start_time)
            req['endTime'] = datetime.datetime.combine(end_date, end_time)

            if st.form_submit_button('Request New Meeting'):
                status, error, data = helper.submit_newMeeting(req)
                if status:
                    ph.empty()
                    # dashboard5(data)
                    st.write('New meeting added\n Redirect to GetMeetings')
                else:
                    st.write(error)
# def dashboard5(data):
#     st.write('New meeting added')

def updateMeeting():
    with ph.container():
        with st.form('updateMeeting'):
            req=dict()
            start_date = st.date_input('Project Start Date:')
            start_time = st.time_input('Project Start Date:')
            end_date = st.date_input('Project End Date:')
            end_time = st.time_input('Project End Date:')

            req['projectID'] = st.number_input('ProjectID', min_value=1)

            req['link'] = st.text_input('Link:', placeholder='http or https://')
            req['remarks'] = st.text_input('Remarks:')

            req['startTime'] = datetime.datetime.combine(start_date, start_time)
            req['endTime'] = datetime.datetime.combine(end_date, end_time)


            req['Status'] = st.radio('Status', ['Accepted', 'Rejected'
                , 'Requested'])
            if st.form_submit_button('Update Meeting'):
                status, error, data = helper.submit_updateMeeting(req)
                if status:
                    ph.empty()
                    # dashboard6(data)
                    st.write('Meeting updated\nRedirect to getMeetings')
                else:
                    st.write(error)
# def dashboard6(data):
#     st.write('Meeting updated')

def newSuggestion(proj_id, faculty_id):
    with ph.container():
        with st.form('newSuggestion'):
            req=dict()
            req['projectID'] = proj_id
            req['facultyID'] = faculty_id
            req['suggestion'] = st.text_area('Suggestion')

            if st.form_submit_button('newSuggestion'):
                status, error, data = helper.submit_newSuggestion(req)
                if status:
                    ph.empty()
                    # dashboard7(data)
                    st.write('New suggestion updated\nRedirect to Project view')

                else:
                    st.write(error)
# def dashboard7(data):
#     st.write('New suggestion updated')

def getSuggestions(proj_id):
    with ph.container():
        with st.form('getSuggestions'):
            req=dict()
            req['projectID'] = proj_id

            if st.form_submit_button('getSuggestions'):
                status, error, data = helper.submit_getSuggestions(req)
                if status:
                    ph.empty()
                    dashboard8(data)
                else:
                    st.write(error)
def dashboard8(data):
    st.write('Get suggestions successful needs to display the sugggestions from df')


