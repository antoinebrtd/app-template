from template.exceptions import APIError


class UsersError(APIError):
    def __init__(self, message, status_code=None):
        APIError.__init__(self, 'Users', message, status_code)


class EmailAddressAlreadyTaken(UsersError):
    def __init__(self):
        UsersError.__init__(self, 'An account with this email address already exists.')


class UserNotFound(UsersError):
    def __init__(self):
        UsersError.__init__(self, 'No account associated to this email address.', 400)
