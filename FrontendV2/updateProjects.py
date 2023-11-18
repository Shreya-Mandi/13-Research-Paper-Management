import streamlit as st
import requests
import webbrowser


class UpdateProjects():

    def __init__(self,id):
        self.id=id

    def get_info(self):
        # Streamlit input
        st.session_state['projectTitle']=st.text_input('Project Title:', placeholder='required')
        st.session_state['projectStatus']=st.text_input('Project Status:')
        st.session_state['startDate']=st.date_input('Project Start Date:')
        st.session_state['endDate']=st.date_input('Project End Date:')
        st.session_state['facultyID']=st.selectbox('Faculty ID:',['Dr.Bharathi','Dr. Sudeepa','Dr. Charu','Dr. Prajwala'])
        st.session_state['students_num']=st.number_input('Student members number:',min_value=1, max_value=4)
        st.session_state['studentID']=list()

        for i in range(st.session_state['students_num']):
            st.session_state['studentID'].append(st.text_input(f'Enter the student id{i+1}'))

    def check_constraints(self):
    # constraint checks
        if(
     st.session_state['projectTitle']
    ):
            st.write('Project id is required.')
            return True
        return False
    def submit(self):
        if(self.check_constraints()):
            print('Sending new update projects request')
            # API post call
            response = requests.post("http://localhost:3002/UpdProject/",
                                     json={
                                         'projectTitle': st.session_state['projectTitle'],
                                         'projectStatus': st.session_state['projectStatus'],
                                         'startDate': st.session_state['startDate'],
                                         'endDate': st.session_state['endDate'],
                                         'facultyID': st.session_state['facultyID'],
                                         'students_num': st.session_state['students_num'],
                                         'studentID': st.session_state['students_num'],
                                     })

            res_json = response.json()
            if(res_json):
                print('update project res_json received')
            return res_json
        else:
            print('Update project create data did not pass constraint check')

    def check_res(self,res_json):
        if res_json['status'] == True:
            st.write('Successful register')
        else:
            if res_json['invalidRequest']==True:
                print('Register module incorrect request made')
            else:
                print('Register module- internal server error')
                print(res_json['errMsg'])

    def put_streamlit_updateProjects(self):
        '''

        ## Update Project
        ## Project Details
        '''

        # submit button
        if st.button('Submit'):
            res_json=self.submit()
            if res_json:
             self.check_res(res_json)

# # login button
# st.write('Go back to projects')
# if st.button('Projects'):
#     st.write('redirect to getProjects')
#     # webbrowser.open_new_tab("http://localhost:3002/Register/")
#
# # View as guest
# st.write('Back to homepage?')
# if st.button('Homepage'):
#     st.write('Redirect to landing page')
#     # webbrowser.open_new_tab("http://localhost:3002/Register/")

'''
Brought to you by: Suhas K, Srinivaasan N S, Soham Sarkar & Shreya Mandi
'''
