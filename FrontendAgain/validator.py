def validate_login(user_id, user_password):
    if len(user_id) != 13 and len(user_id) != 8:
        return False, 'id and password dont match'
    return True, ''

def validate_register(id, pwd,type,details):
    return True, ''

def validate_getProjects(id,type):
    return True, ''

def validate_newProject(req):
    return True, ''

def validate_updateProject(req):
    return True, ''

def validate_updateMeeting(req):
    return True, ''
def validate_newMeeting(req):
    return True, ''
def validate_newSuggestion(req):
    return True, ''
def validate_getSuggestions(req):
    return True, ''
