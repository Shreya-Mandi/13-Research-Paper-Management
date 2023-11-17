import streamlit as st
import requests
import pandas as pd
'''
# Research Paper Management System
'''

def get_projects():
    response=requests.post("http://localhost:3002/GetProjects/",
                           json=dict(usrName=st.session_state['id'], type=st.session_state['type']))


    res_json = response.json()
    return res_json

def display_projects(res_json):
    df = pd.DataFrame(data=res_json['ProjectList'], columns=res_json['ProjectList'][0].keys())
    st.dataframe(df)

def check_res(res_json):
    if res_json['status'] == True:
        print('Get projects successful')
        return True
    else:
        if res_json['invalidRequest']==True:
            print('Get projects module incorrect request made')
        else:
            print('Get projects module- internal server error')
            print(res_json['errMsg'])
        False

res_json=get_projects()
if check_res():
    display_projects()

'''
### Brought to you by: Suhas K, Srinivaasan N S, Soham Sarkar & Shreya Mandi
'''

# def reload_stuff():
#     check=0
#     b=st.button('Reload')
#     if (b) or check==0:
#         check=1
#         st.cache_resource.clear()
#         res_json = response.json()
#         print(res_json)