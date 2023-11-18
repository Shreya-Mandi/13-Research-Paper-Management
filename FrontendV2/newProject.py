import streamlit as st
import requests
import json


class NewProject():

    def __init__(self, id):
        self.id=id

    def get_info(self):
        with st.form('new _project'):
            # Streamlit input
            st.session_state['projectTitle']=st.text_input('Project Title:')
            st.session_state['projectStatus']=st.text_input('Project Status:')
            st.session_state['startDate']=st.date_input('Project Start Date:')
            st.session_state['endDate']=st.date_input('Project End Date:')
            st.session_state['facultyID']=st.radio('Faculty ID:',['Dr.Bharathi','Dr. Sudeepa','Dr. Charu','Dr. Prajwala'])
            st.session_state['students_num']=st.number_input('Student members number:',min_value=1, max_value=4)
            st.session_state['studentID']=list()

            for i in range(st.session_state['students_num']):
                    st.session_state['studentID'].append(st.text_input(f'Enter the student id{i+1}'))

            # submit button
            if st.form_submit_button('Submit'):
                res_json = self.submit()
                if res_json:
                    self.check_res(res_json)

    def check_constraints(self):
        # constraint checks
        if(
                st.session_state['projectTitle']
                | st.session_state['projectStatus']
                | st.session_state['startDate']
                | st.session_state['endDate']
                | st.session_state['facultyID']
                | st.session_state['students_num']
                | st.session_state['students_num']):
            return True
        return False

    def submit(self):
        if(self.check_constraints()):
            print('Sending new projects request')
            # API post call
            response = requests.post("http://localhost:3002/NewProject/",
                                     json={
                                         'projectTitle': st.session_state['projectTitle'],
                                         'projectStatus': st.session_state['projectStatus'],
                                         'startDate': st.session_state['startDate'],
                                         'endDate': st.session_state['endDate'],
                                         'facultyID': st.session_state['facultyID'],
                                         'studentID': st.session_state['students_num'],
                                     })

            res_json = response.json()
            if(res_json):
                print('register res_json received')
            return res_json
        else:
            print('New project create data did not pass constraint check')

    def check_res(self,res_json):
        if res_json['status'] == True:
            st.write('Successful register')
        else:
            if res_json['invalidRequest']==True:
                print('Register module incorrect request made')
            else:
                print('Register module- internal server error')
                print(res_json['errMsg'])

    def put_streamlit_newProject(self):
        '''
                ## Create Project
                ## Project Details
                '''

        self.get_info()





















