import streamlit as st
import requests
import pandas as pd
'''
# Research Paper Management System
'''
st.session_state['name']='shreya'
st.session_state['type']='student'

response=requests.post("http://localhost:6969/ProjectList/",
                       json={
                           'usrName':st.session_state['name'],
                           'type':st.session_state['type']
                       })


check=0
b=st.button('Reload')
if (b) or check==0:
    check=1
    st.cache_resource.clear()
    res_json = response.json()
    print(res_json)

    df = pd.DataFrame(data=res_json['ProjectList'], columns=res_json['ProjectList'][0].keys())
    st.dataframe(df)

'''
### Brought to you by: Suhas K, Srinivaasan N S, Soham Sarkar & Shreya Mandi
'''