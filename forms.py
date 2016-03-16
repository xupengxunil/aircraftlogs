from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo


class RegistrationForm(Form):
    username = StringField('Username', [Length(min=4, max=20)])
    email = StringField('Email Address', [Length(min=6, max=100)])
    password = PasswordField('Password', [DataRequired(),
                                          EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Retype Password')

    accept_tos = BooleanField('I accept the Terms of Service and the Privacy Notice', [DataRequired()])
