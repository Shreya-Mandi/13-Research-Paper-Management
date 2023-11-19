import requests
import validator


def submit_login(req):
    passed, validation_error = validator.validate_login(req['id'], req['pwd'])
    if passed:
        print('sending login post request')
        response = requests.post("http://localhost:3002/Login/",
                                 json={
                                     'id': req['id'],
                                     'pwd': req['pwd']
                                 })

        print('response received for login')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_login(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_register(req):
    passed, validation_error = validator.validate_register(req)
    if passed:
        print('sending register post request')
        response = requests.post("http://localhost:3002/Register/",
                                 json=req)
        print('response received for register')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_register(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_getProjects(req):
    passed, validation_error = validator.validate_getProjects(req)
    if passed:
        print('sending get projects post request')
        response = requests.post("http://localhost:3002/GetProjects/",
                                 # json={'id':user_id, 'type':user_type}
                                 json=req
                                 )

        print('response get projects for register')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_getProjectDetailed(req):
    passed, validation_error = validator.validate_getProjectDetailed(req)
    if passed:
        print('sending get projects detailed post request')
        response = requests.post("http://localhost:3002/GetProject/",
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


def submit_newProject(req):
    passed, validation_error = validator.validate_newProject(req)
    if passed:
        print('sending new projects post request')
        response = requests.post("http://localhost:3002/NewProject/",
                                 # json={'projectTitle' :req['projectTitle'],
                                 # 'projectStatus' : req['projectStatus'],
                                 # 'startDate' :req['startDate'],
                                 # 'endDate' : req['endDate'],
                                 # 'facultyID' : req['facultyID'],
                                 # 'studentID' : req['studentID']}
                                 json=req)

        print('response for new projects')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_updateProject(req):
    passed, validation_error = validator.validate_updateProject(req)
    if passed:
        print('sending upd projects post request')
        response = requests.post("http://localhost:3002/UpdProject/",
                                 # json={'projectTitle' :req['projectTitle'],
                                 # 'projectStatus' : req['projectStatus'],
                                 # 'startDate' :req['startDate'],
                                 # 'endDate' : req['endDate'],
                                 # 'facultyID' : req['facultyID'],
                                 # 'studentID' : req['studentID']}
                                 json=req
                                 )

        print('response for upd projects')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_getMeetings(req):
    passed, validation_error = validator.validate_getMeetings(req)
    if passed:
        print('sending get meeting post request')
        response = requests.post("http://localhost:3002/GetMeetings/",
                                 json=req
                                 )

        print('response get meeting ')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_newMeeting(req):
    passed, validation_error = validator.validate_newMeeting(req)
    if passed:
        print('sending new meeting post request')
        response = requests.post("http://localhost:3002/NewMeeting/",
                                 # json={
                                 #     'projectID': req['projectID'],
                                 #     'startTime': req['startTime'],
                                 #     'endTime': req['endTime'],
                                 #     'link': req['link'],
                                 #     'remarks': req['remarks'],
                                 # }
                                 json=req
                                 )
        print('response for new meeting')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_updateMeeting(req):
    passed, validation_error = validator.validate_updateMeeting(req)
    if passed:
        print('sending upd meeting post request')
        response = requests.post("http://localhost:3002/UpdMeeting/",
                                 # json={
                                 #     'projectID': req['projectID'],
                                 #     'status': req['status'],
                                 #     'startTime': req['startTime'],
                                 #     'endTime': req['endTime'],
                                 #     'link': req['link'],
                                 #     'remarks': req['remarks'],
                                 # }
                                 json=req)
        print('response for upd meeting')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_newSuggestion(req):
    passed, validation_error = validator.validate_newSuggestion(req)
    if passed:
        print('sending new suggestion request')
        response = requests.post("http://localhost:3002/NewSuggestion/",
                                 # json={
                                 #     'projectID': req['projectID'],
                                 #     'facultyID': req['facultyID'],
                                 #     'suggestion': req['suggestion'],
                                 # }
                                 json=req)
        print('response for new suggstion')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_getSuggestions(req):
    passed, validation_error = validator.validate_getSuggestions(req)
    if passed:
        print('sending get suggestions request')
        response = requests.post("http://localhost:3002/GetSuggestions/",
                                 # json={
                                 #     'projectID': req['projectID'],
                                 # }
                                 json=req)
        print('response for get suggstions')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def check_res_login(res_json):
    if res_json['status']:
        if res_json['valid']:
            return True, ''
        else:
            return False, 'ID and Password don\'t match'
    else:
        print(res_json['errMsg'])
        return False, 'Internal Error'


def check_res_register(res_json):
    if res_json['status']:
        return True, ''
    else:
        print(res_json['errMsg'])
        if 'message' in res_json['errMsg'] and "Duplicate" in res_json['errMsg']['message']:
            return False, 'ID Already exists'
        return False, 'Internal Error'


def check_res_default(res_json):
    if res_json['status']:
        return True, ''
    else:
        print(res_json['errMsg'])
        return False, 'Internal Error'
