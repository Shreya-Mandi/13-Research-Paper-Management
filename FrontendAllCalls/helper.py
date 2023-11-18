import requests
import validator


def submit_login(user_id, user_password):
    passed, validation_error = validator.validate_login(user_id, user_password)
    if passed:
        print('sending login post request')
        response = requests.post("http://localhost:3002/Login/",
                                 json={
                                     'id': user_id,
                                     'pwd': user_password
                                 })

        print('response received for login')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_login(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}

def submit_register(id, pwd,type,details):
    passed, validation_error = validator.validate_register(id, pwd,type,details)
    if passed:
        print('sending register post request')
        response = requests.post("http://localhost:3002/Register/",
                                 json={
                                     'id': id,
                                     'pwd': pwd,
                                     'type': type,
                                     'details': details
                                 })
        json = {
            'id': id,
            'pwd': pwd,
            'type': type,
            'details': details
        }
        print(json)
        print('response received for register')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_register(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}
def submit_getProjects(user_id,user_type):
    passed, validation_error = validator.validate_getProjects(id,type)
    if passed:
        print('sending get projects post request')
        response = requests.post("http://localhost:3002/GetProjects/",
                               json={'id':user_id, 'type':user_type})

        print('response get projects for register')
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
        json={'projectTitle' :req['projectTitle'],
        'projectStatus' : req['projectStatus'],
        'startDate' :req['startDate'],
        'endDate' : req['endDate'],
        'facultyID' : req['facultyID'],
        'studentID' : req['studentID']})

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
        json={'projectTitle' :req['projectTitle'],
        'projectStatus' : req['projectStatus'],
        'startDate' :req['startDate'],
        'endDate' : req['endDate'],
        'facultyID' : req['facultyID'],
        'studentID' : req['studentID']})

        print('response for upd projects')
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
                                     json={
                                         'projectID': req['projectID'],
                                         'startTime': req['startTime'],
                                         'endTime': req['endTime'],
                                         'link': req['link'],
                                         'remarks': req['remarks'],
                                     })
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
                                     json={
                                         'projectID': req['projectID'],
                                         'status': req['status'],
                                         'startTime': req['startTime'],
                                         'endTime': req['endTime'],
                                         'link': req['link'],
                                         'remarks': req['remarks'],
                                     })
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
                                 json={
                                     'projectID': req['projectID'],
                                     'facultyID': req['facultyID'],
                                     'suggestion': req['suggestion'],
                                 })
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
                                 json={
                                     'projectID': req['projectID'],
                                 })
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
            if "Duplicate" in res_json['errMsg']['message']:
                return False, 'ID Already exists'
            return False, 'Internal Error'

def check_res_default(res_json):
    if res_json['status']:
        return True, ''
    else:
        print(res_json['errMsg'])
        return False, 'Internal Error'