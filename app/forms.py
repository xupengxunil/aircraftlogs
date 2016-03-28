from wtforms import Form, StringField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo


class RegistrationForm(Form):
    first_name = StringField('First Name', [DataRequired()])
    last_name = StringField('Last Name', [DataRequired()])
    username = StringField('Username', [Length(min=4, max=20)])
    email = StringField('Email Address', [Length(min=6, max=100)])
    password = PasswordField('Password', [DataRequired(),
                                          EqualTo('confirm',
                                                  message='Passwords must match')])
    confirm = PasswordField('Retype Password', [DataRequired()])


class LoginForm(Form):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
