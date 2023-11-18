import validators
from datetime import datetime


def validate_login(user_id, user_password):
    if len(user_id) != 13 or not user_id.isalnum() or len(user_password) != 8:
        return False, 'ID and Password do not match'
    return True, ''


def validate_registration(user_id, user_password, first_name, last_name, semester, section, domain):
    if not (len(user_id) == 13 and user_id.isalnum()):
        return False, 'ID should be 13 characters and alphanumeric'
    if not (len(user_password) >= 5 and user_password.isalnum()):
        return False, 'Password should be at least 5 characters and alphanumeric'
    if not (first_name.isalpha()):
        return False, 'First name should contain only alphabets'
    if not (last_name.isalpha()):
        return False, 'Last name should contain only alphabets'
    if not (semester.isdigit() and 1 <= int(semester) <= 8):
        return False, 'Semester should be a number between 1 and 8'
    if not (len(section) == 1 and section.isalpha()):
        return False, 'Section should be a single alphabet'
    if not (domain.isalpha()):
        return False, 'Domain should contain only alphabets'
    return True, ''

def validate_project(title, status, start_date, end_date):
    if not (title.isalnum()):
        return False, 'Title should contain only alphabets and numerals'
    if not (status.isalnum()):
        return False, 'Status should contain only alphabets and numerals'
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        current_time = datetime.now()
        if start_date >= current_time:
            return False, 'Start date should be before the current time'
        if end_date <= start_date:
            return False, 'End date should be after the start date'
    except ValueError:
        return False, 'Invalid date format. Date should be in YYYY-MM-DD format'
    return True, ''


def validate_update_project(project_title, start_date, end_date):
    if project_title is not None and not project_title.isalnum():
        return False, 'Project title should contain only alphabets and numerals'
    if start_date is not None:
        try:
            datetime.strptime(start_date, '%Y-%m-%d')
            current_time = datetime.now().strftime('%Y-%m-%d')
            if start_date >= current_time:
                return False, 'Start date should be before the current time'
        except ValueError:
            return False, 'Invalid start date format. Date should be in YYYY-MM-DD format'
    if end_date is not None:
        try:
            datetime.strptime(end_date, '%Y-%m-%d')
            if start_date is not None:
                if end_date <= start_date:
                    return False, 'End date should be after the start date'
        except ValueError:
            return False, 'Invalid end date format. Date should be in YYYY-MM-DD format'
    return True, ''


def validate_meeting_request(start_time, end_time, meeting_link):
    current_time = datetime.now()
    try:
        start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        if start_time <= current_time:
            return False, 'Start time should be after the current time'
        if end_time <= start_time:
            return False, 'End time should be after the start time'
    except ValueError:
        return False, 'Invalid timestamp format. Date should be in YYYY-MM-DD HH:MM:SS format'
    if not meeting_link.startswith('https://'):
        return False, 'Meeting link is invalid'
    return True, ''


def validate_update_meeting(start_time, end_time, meeting_link):
    current_time = datetime.now()
    if start_time is not None:
        try:
            start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            if start_time <= current_time:
                return False, 'Start time should be after the current time'
        except ValueError:
            return False, 'Invalid start time format. Date should be in YYYY-MM-DD HH:MM:SS format'
    if end_time is not None:
        try:
            end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
            if start_time is not None and end_time <= start_time:
                return False, 'End time should be after the start time'
        except ValueError:
            return False, 'Invalid end time format. Date should be in YYYY-MM-DD HH:MM:SS format'
    if meeting_link is not None and not meeting_link.startswith('https://'):
        return False, 'Meeting link is invalid'
    return True, ''
