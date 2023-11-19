def dashboard():
    user_id = 'PES2UG21CS001'
    user_type = 'student'
    user_name = 'Sudeev Divakar'
    st.write("Welcome, ",user_name)

    req = dict()
    req['id'] = user_id
    req['type'] = user_type
    status, error, data = helper.submit_getProjects(req)
    if status:
        st.write('Projects')
        if (data['projects'] == []):
            st.write('No existing projects')
        else:

            df = pd.DataFrame(data=data['projects'], columns=data['projects'][0].keys())
            df2 = df[['projectID',
                        'projectTitle',
                        'projectStatus'
                        ]]
            df3=pd.DataFrame()
            df3_f=[]
            df3_s=[]
            for i in df['faculty']:
                temp=[]
                for j in i:
                    temp.append(j['name'])
                df3_f.append(' '.join(temp))
            for i in df['student']:
                temp = []
                for j in i:
                    temp.append(j['name'])
                df3_s.append(' '.join(temp))
            df2['faculty']=df3_f
            df2['student']=df3_s
            st.dataframe(df2)

    else:
        st.write(error)







def getProjectDetailed():
    req=dict()
    req['projectID']='1'
    status, error, data = helper.submit_getProjectDetailed(req)
    if status:
        title=data['projectTitle']
        proj_status=data['projectStatus']
        start_data=data['startDate']
        end_date=data['endDate']
        st.write(f'{title}')

        l=data['details']['faculty']
        temp=[]
        for i in l:
            temp.append(
                i['name']
            )
        fac_st=', '.join(temp)
        st.write(f'Faculty:{fac_st}')

        l = data['details']['student']
        temp = []
        for i in l:
            temp.append(
                i['name']
            )
        stu_st = ', '.join(temp)
        st.write(f'Students:{stu_st}')
        st.write(f'Status:{proj_status}')
        st.write(f'Start Date:{start_data}')
        st.write(f'End Date:{end_date}')

        st.write('Faculty suggestions')

        st.write('Meetings')

    else:
        st.write(error)

def submit_getProjectDetailed(req):
    passed, validation_error = validator.validate_getProjectDetailed(req)
    if passed:
        print('sending get projects detailed post request')
        response = requests.post("http://localhost:3002/GetProjects/",
                                 # json={'projectTitle' :req['projectTitle'],
                                 # 'projectStatus' : req['projectStatus'],
                                 # 'startDate' :req['startDate'],
                                 # 'endDate' : req['endDate'],
                                 # 'facultyID' : req['facultyID'],
                                 # 'studentID' : req['studentID']}
                                 json=req
                                 )

        print('response for get projects detailed')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}