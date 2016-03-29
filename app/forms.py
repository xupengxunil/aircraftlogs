from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo
from app.models import User


class RegistrationForm(Form):
    first_name = StringField('First Name',
                             [DataRequired("Please enter your first name.")])
    last_name = StringField('Last Name',
                            [DataRequired("Please enter your last name.")])
    username = StringField('Username',
                           [Length(min=4, max=20)])
    email = StringField('Email Address',
                        [Length(min=6, max=100)])
    password = PasswordField('Password',
                             [DataRequired("Please enter a password."),
                              EqualTo('confirm',
                                      message='Passwords must match.')])
    confirm = PasswordField('Retype Password',
                            [DataRequired("Please retype your password.")])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(
            username=self.username.data.lower()).first()
        if user:
            self.username.errors.append("That username is already taken")
            return False
        else:
            return True


class LoginForm(Form):
    username = StringField('Username', [DataRequired('Please enter your Username.')])
    password = PasswordField('Password', [DataRequired('Please enter your Password.')])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(
            username=self.username.data.lower()).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.username.errors.append("Invalid username or password.")
            return False
