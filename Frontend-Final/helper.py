import requests
import validator


def submit_getUsers():
    print('sending new get users get request')
    response = requests.get("http://localhost:3002/GetUsers/")

    print('response for get users')
    res_json = response.json()
    print(res_json)
    status, res_error = check_res_default(res_json)
    return status, res_error, res_json


def submit_login(req):
    passed, validation_error = validator.validate_login(req)
    if passed:
        print('sending login post request')
        response = requests.post("http://localhost:3002/Login/", json=req)

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
        response = requests.post("http://localhost:3002/Register/", json=req)
        print('response received for register')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_register(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_getProjects(req):
    print('sending get projects post request')
    response = requests.post("http://localhost:3002/GetProjects/", json=req)

    print('response get projects for register')
    res_json = response.json()
    print(res_json)
    status, res_error = check_res_default(res_json)
    return status, res_error, res_json


def submit_newProject(req):
    passed, validation_error = validator.validate_newProject(req)
    if passed:
        print('sending new projects post request')
        response = requests.post("http://localhost:3002/NewProject/", json=req)

        print('response for new projects')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_getProjectDetailed(req):
    print('sending get projects detailed post request')
    response = requests.post("http://localhost:3002/GetProject/", json=req)

    print('response for get projects detailed')
    res_json = response.json()
    print(res_json)
    status, res_error = check_res_default(res_json)
    return status, res_error, res_json


def submit_updateProject(req):
    passed, validation_error = validator.validate_updateProject(req)
    if passed:
        print('sending upd projects post request')
        response = requests.post("http://localhost:3002/UpdProject/", json=req)

        print('response for upd projects')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_delProject(req):
    print('sending del projects post request')
    response = requests.post("http://localhost:3002/DelProject/", json=req)

    print('response for del projects')
    res_json = response.json()
    print(res_json)
    status, res_error = check_res_default(res_json)
    return status, res_error, res_json


def submit_newMeeting(req):
    passed, validation_error = validator.validate_newMeeting(req)
    if passed:
        print('sending new meeting post request')
        response = requests.post("http://localhost:3002/NewMeeting/", json=req)

        print('response for new meeting')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_getMeetings(req):
    print('sending get meeting post request')
    response = requests.post("http://localhost:3002/GetMeetings/", json=req)

    print('response get meeting ')
    res_json = response.json()
    print(res_json)
    status, res_error = check_res_default(res_json)
    return status, res_error, res_json


def submit_updateMeeting(req):
    passed, validation_error = validator.validate_updateMeeting(req)
    if passed:
        print('sending upd meeting post request')
        response = requests.post("http://localhost:3002/UpdMeeting/", json=req)

        print('response for upd meeting')
        res_json = response.json()
        print(res_json)
        status, res_error = check_res_default(res_json)
        return status, res_error, res_json
    else:
        return False, validation_error, {}


def submit_newSuggestion(req):
    print('sending new suggestion request')
    response = requests.post("http://localhost:3002/NewSuggestion/", json=req)

    print('response for new suggestion')
    res_json = response.json()
    print(res_json)
    status, res_error = check_res_default(res_json)
    return status, res_error, res_json


def submit_getSuggestions(req):
    print('sending get suggestions request')
    response = requests.post("http://localhost:3002/GetSuggestions/", json=req)

    print('response for get suggestions')
    res_json = response.json()
    print(res_json)
    status, res_error = check_res_default(res_json)
    return status, res_error, res_json


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
