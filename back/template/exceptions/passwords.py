from template.exceptions import APIError


class PasswordErrors(APIError):
    def __init__(self, message, status_code=None):
        APIError.__init__(self, 'Passwords', message, status_code)


class EmailPasswordMismatch(PasswordErrors):
    def __init__(self):
        PasswordErrors.__init__(self, "Email and password don't match", 401)


class PasswordRequired(PasswordErrors):
    def __init__(self):
        PasswordErrors.__init__(self, "Password is required", 401)


class PasswordTooShort(PasswordErrors):
    def __init__(self):
        PasswordErrors.__init__(self, "Min 8 characters", 401)


class LoginWithGoogle(PasswordErrors):
    def __init__(self):
        PasswordErrors.__init__(self, "Please log in with google", 401)
