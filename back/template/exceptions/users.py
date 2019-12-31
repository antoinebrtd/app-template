from template.exceptions import APIError


class UserError(APIError):
    def __init__(self, message, status_code=None):
        APIError.__init__(self, 'Users', message, status_code)


class EmailAddressAlreadyTaken(UserError):
    def __init__(self):
        UserError.__init__(self, 'An account with this email address already exists.', 400)


class UserNotFound(UserError):
    def __init__(self):
        UserError.__init__(self, 'No account associated to this email address.', 404)


class LoginWithGoogle(UserError):
    def __init__(self):
        UserError.__init__(self, "Please log in with google", 401)


class LoginWithFacebook(UserError):
    def __init__(self):
        UserError.__init__(self, "Please log in with Facebook", 401)


class InvalidConfirmationLink(UserError):
    def __init__(self):
        UserError.__init__(self, "Activation link invalid or expired", 404)


class AccountAlreadyActivated(UserError):
    def __init__(self):
        UserError.__init__(self, "Your account is already activated", 400)
