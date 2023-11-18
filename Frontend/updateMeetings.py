import streamlit as st
import requests
import webbrowser
import datetime

'''
# Research Paper Management System

## Update meeting
## Meeting Details
'''
# session states
st.session_state['type']='student'
# 'faculty'


# Streamlit input
st.session_state['projectID']=st.number_input('ProjectID',min_value=1)

start_date=st.date_input('Project Start Date:')
start_time=st.time_input('Project Start Date:')
end_date=st.date_input('Project End Date:')
end_time=st.time_input('Project End Date:')


st.session_state['link']=st.text_input('Link:', placeholder='http or https://')
st.session_state['remarks']=st.text_input('Remarks:')

st.session_state['startTime'] = datetime.datetime.combine(start_date, start_time)
st.session_state['endTime'] = datetime.datetime.combine(end_date, end_time)

st.session_state['Status']=st.radio('Status',['Accepted','Rejected'
,'Requested'])

def check_constraints():
# constraint checks
    if(
 st.session_state['projectID']
):
        st.write('ProjectID is a required field.')
        return True
    return False
def submit():
    if(check_constraints()):
        print('Sending update meeting request')
        # API post call
        response = requests.post("http://localhost:3002/UpdMeeting/",
                                 json={
                                     'projectID': st.session_state['projectID'],
                                     'status': st.session_state['status'],
                                     'startTime': st.session_state['startTime'],
                                     'endTime': st.session_state['endTime'],
                                     'link': st.session_state['link'],
                                     'remarks': st.session_state['remarks'],
                                 })

        res_json = response.json()
        if(res_json):
            print('update meeting request res_json received')
        return res_json
    else:
        print('update meeting request data did not pass constraint check')

def check_res(res_json):
    if res_json['status'] == True:
        st.write('Successful new meeting posted')
    else:
        if res_json['invalidRequest']==True:
            print('New meeting request module incorrect request made')
        else:
            print('New meeting request module- internal server error')
            print(res_json['errMsg'])


# submit button
if st.button('Submit'):
    res_json=submit()
    if res_json:
     check_res(res_json)

# projects button
st.write('Go back to projects')
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
