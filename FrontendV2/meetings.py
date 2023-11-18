import streamlit as st
import requests
import pandas as pd
import newProject
import updateProjects

class Meetings:
    def __init__(self, id, type, pro_id):
        self.id=id
        self.project_id=pro_id
        self.type=type
        self.menu_list=['View approved meetings','Request new meeting','Update meeting','Delete meeting']

    def menu(self):
        ch= st.selectbox('Welcome to your project view, what would you like to do?',self.menu_list)
        return ch

    def get_projects(self):
        response=requests.post("http://localhost:3002/GetMeetings/",
                               json=dict(usrName=self.id, type=self.type))
        res_json = response.json()
        return res_json

    def get_project_id(self,res_json):
        df = pd.DataFrame(data=res_json['ProjectList'], columns=res_json['ProjectList'][0].keys())
        st.dataframe(df)

        self.project_id=st.number_input('Enter project id:', min_value=0, max_value=len(df)-1)

    def check_res(self,res_json):
        if res_json['status'] == True:
            print('Get projects successful')
            return True
        else:
            if res_json['invalidRequest']==True:
                print('Get projects module incorrect request made')
            else:
                print('Get projects module- internal server error')
                print(res_json['errMsg'])
            return False



    def put_streamlit_projects(self):
        ch=self.menu()

        if ch==self.menu_list[1]:
            # new meeting
            res_json=self.get_projects()
            if self.check_res():
                self.get_project_id()

        elif ch==self.menu_list[0]:
            # existing meeting
            newProject_obj=newProject.NewProject(self.id)
            newProject_obj.put_streamlit_newProject()
        elif ch==self.menu_list[2]:
            # update project
            updateProjects_obj=updateProjects.UpdateProjects(self.id)
            updateProjects_obj.put_streamlit_updateProjects()

        elif ch==self.menu_list[3]:
            # delete project
            num=st.number_input('Enter the project id')
