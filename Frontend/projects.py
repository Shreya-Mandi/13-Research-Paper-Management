import streamlit as st
import requests
import pandas as pd
import newProject
import updateProjects
import json

class GetProjects:
    def __init__(self, id, type):
        self.id=id
        self.type=type
        self.menu_list=['View existing projects','Create new project','Update project','Delete project']

    def get_project_id(self):
        with open("my_info.json", "r") as file:
            data = json.load(file)
            self.id=data['id']
            self.type=data['type']

    def menu(self):
        ch= st.selectbox('Welcome to your project view, what would you like to do?',self.menu_list)
        return ch

    def get_projects(self):
        self.get_project_id()
        response=requests.post("http://localhost:3002/GetProjects/",
                               json={'id':self.id, 'type':self.type})
        res_json = response.json()
        return res_json

    def display_projects(self,res_json):
        if(res_json['projects']==[]):
            st.write('no existing projects')
        else:
            df = pd.DataFrame(data=res_json['projects'], columns=res_json['projects'][0].keys())
            st.dataframe(df)

    def check_res(self,res_json):
        if res_json['status'] == True:
            print('Get projects successful')
            return True
        else:
            if res_json['invalidRequest']==True:
                print('Get projects module incorrect request made')
                print(res_json['errMsg'])
            else:
                print('Get projects module- internal server error')
                print(res_json['errMsg'])
            return False

    def put_streamlit_projects(self):
        # ch=self.menu()
        self.get_project_id()
        if st.button(self.menu_list[0]):
            # existing view
            res_json=self.get_projects()
            if self.check_res(res_json):
                self.display_projects(res_json)
        elif st.button(self.menu_list[1]):
            print('pressed1')
            # new project
            newProject_obj=newProject.NewProject(self.id)
            newProject_obj.put_streamlit_newProject()
        elif st.button(self.menu_list[2]):
            # update project
            updateProjects_obj=updateProjects.UpdateProjects(self.id)
            updateProjects_obj.put_streamlit_updateProjects()

        elif st.button(self.menu_list[3]):
            # delete project
            num=st.number_input('Enter the project id')
