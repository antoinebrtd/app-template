from template.exceptions import APIError


class UsersError(APIError):
    def __init__(self, message, status_code=None):
        APIError.__init__(self, 'Users', message, status_code)


class UserAlreadyRegistered(UsersError):
    def __init__(self):
        UsersError.__init__(self, 'This user is already registered.')


class UserNotExisting(UsersError):
    def __init__(self):
        UsersError.__init__(self, 'This user does not exist.', 400)
