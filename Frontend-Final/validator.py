from datetime import datetime


def validate_login(req):
    if not req['id'].isalnum():
        print('validate login-user id is not alpha numerical')
        return False, 'ID and Password do not match'
    if not (len(req['id']) == 13 or len(req['id']) == 8):
        print('validate login-user id not of correct length')
        return False, 'ID and Password do not match'
    if not len(req['pwd']) >= 5:
        print('validate login-user pwd not of correct length')
        return False, 'ID and Password do not match'
    return True, ''


def validate_register(req):
    if not req['id'].isalnum():
        print('validate register- userid is not alpha numerical')
        return False, 'Invalid ID, check id no special chars'
    if not len(req['pwd']) >= 5:
        print('validate register- user pwd must be larger than  or equal to 5 chars')
        return False, 'Invalid Password, must be at least 5 characters'
    if not req['details']['firstName'].isalpha():
        print('validate register- first name should be alphabets')
        return False, 'Invalid firstname, must be only alphabets'
    if not req['details']['lastName'].isalpha():
        print('validate register- last name should be alphabet')
        return False, 'Invalid lastname, must be only alphabets'

    if req['type'] == 'student':
        if not len(req['id']) == 13:
            print('validate register- userid is not 13 len')
            return False, 'Invalid ID, check id length'
        if not (1 <= req['details']['sem'] <= 8):
            print('validate register- check sem range')
            return False, 'Invalid semester, must be only 1-8'
        if isinstance(req['details']['sec'], str):
            if not (req['details']['sec'].isalpha() and len(req['details']['sec']) == 1):
                print('validate register- check sec range')
                return False, 'Invalid sec, must be only alphabet characters a-z'
        else:
            print('validate register- check sec range')
            return False, 'Invalid sec, must be only alphabet characters a-z'
    if req['type'] == 'faculty':
        if not len(req['id']) == 8:
            print('validate register- userid is not 8 len')
            return False, 'Invalid ID, check id length'
        if not (req['details']['domain'].isalpha()):
            print('validate register- only letters in domain')
            return False, 'Invalid domain, must be only alphabets'
    return True, ''


def validate_newProject(req):
    if not (all(x.isalpha() or x.isspace() or x.isnumeric() for x in req['projectTitle'])):
        print('validate create project module- not alpha num')
        return False, 'Invalid title, should contain only alphabets and numerals'
    try:
        start_date = datetime.strptime(req['startDate'], '%Y-%m-%d')
        end_date = None
        if 'endDate' in req.keys():
            end_date = datetime.strptime(req['endDate'], '%Y-%m-%d')
        current_time = datetime.now()
        if start_date >= current_time:
            print('validate create project module- start date is invalid')
            return False, 'Start date should be before the current time'
        if end_date and end_date <= start_date:
            return False, 'End date should be after the start date'
    except ValueError:
        return False, 'Invalid date format. Date should be in YYYY-MM-DD format'
    return True, ''


def validate_updateProject(req):
    if 'projectTitle' in req.keys():
        if not (all(x.isalpha() or x.isspace() or x.isnumeric() for x in req['projectTitle'])):
            print('validate create project module- not alpha num')
            return False, 'Invalid title, should contain only alphabets and numerals'
    try:
        start_date = None
        if 'startDate' in req.keys():
            start_date = datetime.strptime(req['startDate'], '%Y-%m-%d')
        end_date = None
        if 'endDate' in req.keys():
            end_date = datetime.strptime(req['endDate'], '%Y-%m-%d')
        current_time = datetime.now()
        if start_date and start_date >= current_time:
            print('validate create project module- start date is invalid')
            return False, 'Start date should be before the current time'
        if (end_date and start_date) and end_date <= start_date:
            print('validate create project module- end date is invalid')
            return False, 'End date should be after the start date'
    except ValueError:
        return False, 'Invalid date format. Date should be in YYYY-MM-DD format'
    return True, ''


def validate_newMeeting(req):
    current_time = datetime.now()
    try:

        start_time = datetime.strptime(req['startTime'], '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(req['endTime'], '%Y-%m-%d %H:%M:%S')
        if start_time and start_time <= current_time:
            return False, 'Start time should be after the current time'
        if end_time and end_time <= start_time:
            return False, 'End time should be after the start time'
    except ValueError:
        return False, 'Invalid timestamp format. Date should be in YYYY-MM-DD HH:MM:SS format'
    if not req['link'].startswith('https://'):
        return False, 'Meeting link is invalid'
    return True, ''


def validate_updateMeeting(req):
    current_time = datetime.now()
    try:
        start_time = None
        if 'startTime' in req.keys():
            start_time = datetime.strptime(req['startTime'], '%Y-%m-%d %H:%M:%S')
        end_time = None
        if 'endTime' in req.keys():
            end_time = datetime.strptime(req['endTime'], '%Y-%m-%d %H:%M:%S')
        if start_time and start_time <= current_time:
            return False, 'Start time should be after the current time'
        if end_time and end_time <= start_time:
            return False, 'End time should be after the start time'
    except ValueError:
        return False, 'Invalid timestamp format. Date should be in YYYY-MM-DD HH:MM:SS format'
    if 'link' in req.keys():
        if not req['link'].startswith('https://'):
            return False, 'Meeting link is invalid'
    return True, ''
