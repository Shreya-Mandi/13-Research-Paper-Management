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
def submit_register(id, pwd,type,details):
    passed, validation_error = validator.validate_register(id, pwd,type,details)
    if passed:
        print('sending register post request')
        response = requests.post("http://localhost:3002/GetProjects/",
                               json={'id':st.session_state['id'], 'type':st.session_state['type']})
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