import streamlit as st
import requests
import pandas as pd
import newProject
import updateProjects

class GetProjects:
    def __init__(self, id, type):
        self.id=id
        self.type=type
        self.menu_list=['View existing projects','Create new project','Update project','Delete project']

    def menu(self):
        ch= st.selectbox('Welcome to your project view, what would you like to do?',self.menu_list)
        return ch

    def get_projects(self):
        response=requests.post("http://localhost:3002/GetProjects/",
                               json=dict(usrName=self.id, type=st.session_state['type']))
        res_json = response.json()
        return res_json

    def display_projects(self,res_json):
        df = pd.DataFrame(data=res_json['ProjectList'], columns=res_json['ProjectList'][0].keys())
        st.dataframe(df)

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

        if ch==self.menu_list[0]:
            # existing view
            res_json=self.get_projects()
            if self.check_res():
                self.display_projects()
        elif ch==self.menu_list[1]:
            # new project
            newProject_obj=newProject.NewProject(self.id)
            newProject_obj.put_streamlit_newProject()
        elif ch==self.menu_list[2]:
            # update project
            updateProjects_obj=updateProjects.UpdateProjects(self.id)
            updateProjects_obj.put_streamlit_updateProjects()

        elif ch==self.menu_list[3]:
            # delete project
            num=st.number_input('Enter the project id')
