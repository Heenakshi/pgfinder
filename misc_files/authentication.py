def authorize(auth, role, user_role):
    if auth is True:
        if user_role == role:
            return True
        else:
            return "wrong_user"
    else:
        return "not_login"
