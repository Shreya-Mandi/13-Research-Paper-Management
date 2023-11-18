def validate_login(user_id, user_password):
    if len(user_id) != 13 and len(user_id) != 8:
        return False, 'id and password dont match'
    return True, ''
