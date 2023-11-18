import streamlit as st
import requests
import webbrowser
import datetime

'''
# Research Paper Management System

## Request meeting
## Meeting Details
'''
# session states
st.session_state['facultyID']='abc123'


# Streamlit input
st.session_state['projectID']=st.number_input('ProjectID',min_value=1)
st.session_state['suggestion']=st.text_area('Suggestion')

def check_constraints():
# constraint checks
    if(
 st.session_state['projectID'] &
 st.session_state['facultyID']
):
        st.write('ProjectID and facultyID are required fields.')
        return True
    return False
def submit():
    if(check_constraints()):
        print('Sending new meeting request')
        # API post call
        response = requests.post("http://localhost:3002/NewSuggestion/",
                                 json={
                                     'projectID': st.session_state['projectID'],
                                     'facultyID': st.session_state['facultyID'],
                                     'suggestion': st.session_state['suggestion'],
                                 })

        res_json = response.json()
        if(res_json):
            print('new suggestion request res_json received')
        return res_json
    else:
        print('New suggestion request data did not pass constraint check')

def check_res(res_json):
    if res_json['status'] == True:
        st.write('Successful new meeting posted')
    else:
        if res_json['invalidRequest']==True:
            print('New suggestion request module incorrect request made')
        else:
            print('New suggestion request module- internal server error')
            print(res_json['errMsg'])


# submit button
if st.button('Submit'):
    res_json=submit()
    if res_json:
     check_res(res_json)

# login button
st.write('Go back to projects view')
if st.button('Projects'):
    st.write('redirect to getProjects')
    # webbrowser.open_new_tab("http://localhost:3002/Register/")

# go to homepage
st.write('Back to homepage?')
if st.button('Homepage'):
    st.write('Redirect to landing page')
    # webbrowser.open_new_tab("http://localhost:3002/Register/")

'''
Brought to you by: Suhas K, Srinivaasan N S, Soham Sarkar & Shreya Mandi
'''
