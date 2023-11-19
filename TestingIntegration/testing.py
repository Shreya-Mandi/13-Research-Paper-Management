def dashboard():
    user_id = 'PES2UG21CS001'
    user_type = 'student'
    user_name = 'Sudeev Divakar'
    st.write("Welcome, ",user_name)
    with st.form('getProjects'):

        if st.form_submit_button('View Existing Projects'):
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
                    # df2 = df[['projectID',
                    #             'projectTitle',
                    #             'projectStatus'
                    #             ]]
                    # df3=pd.DataFrame()
                    # df3_1=[]
                    # df3_2=[]
                    # for i in df['faculty']:
                    #     temp=[]
                    #     for j in i:
                    #         temp.append(j['name'])
                    #     df31.append(' '.join(j))
                    # for i in df['student']:
                    #     temp=[]
                    #     for j in i:
                    #         temp.append(j['name'])
                    #     df32.append(' '.join(j))
                    # df2['faculty']=df31
                    # df2['student']=df32
                    st.dataframe(df)

            else:
                st.write(error)