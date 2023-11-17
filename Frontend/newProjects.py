import streamlit as st
import requests
import webbrowser

'''
# Research Paper Management System

## Create Project
## Project Details
'''
# session states
st.session_state['type']='student'
# 'faculty'


# Streamlit input
st.session_state['projectTitle']=st.text_input('Project Title:')
st.session_state['projectStatus']=st.text_input('Project Status:')
st.session_state['startDate']=st.date_input('Project Start Date:')
st.session_state['endDate']=st.date_input('Project End Date:')
st.session_state['facultyID']=st.selectbox('Faculty ID:',['Dr.Bharathi','Dr. Sudeepa','Dr. Charu','Dr. Prajwala'])
st.session_state['students_num']=st.number_input('Student members number:',min_value=1, max_value=4)
st.session_state['studentID']=list()

for i in range(st.session_state['students_num']):
    st.session_state['studentID'].append(st.text_input(f'Enter the student id{i+1}'))
def check_constraints():
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
def submit():
    if(check_constraints()):
        print('Sending new projects request')
        # API post call
        response = requests.post("http://localhost:3002/NewProject/",
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
            print('register res_json received')
        return res_json
    else:
        print('New project create data did not pass constraint check')

def check_res(res_json):
    if res_json['status'] == True:
        st.write('Successful register')
    else:
        if res_json['invalidRequest']==True:
            print('Register module incorrect request made')
        else:
            print('Register module- internal server error')
            print(res_json['errMsg'])


# register button
if st.button('Submit'):
    res_json=submit()
    if res_json:
     check_res(res_json)

# login button
st.write('Go back to prjects')
if st.button('Projects'):
    st.write('redirect to getProjects')
    # webbrowser.open_new_tab("http://localhost:3002/Register/")

# View as guest
st.write('Back to homepage?')
if st.button('Homepage'):
    st.write('Redirect to landing page')
    # webbrowser.open_new_tab("http://localhost:3002/Register/")

'''
Brought to you by: Suhas K, Srinivaasan N S, Soham Sarkar & Shreya Mandi
'''