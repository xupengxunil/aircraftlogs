from wtforms import Form, BooleanField, StringField, PasswordField
from wtforms.validators import Length, DataRequired, EqualTo

from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    first_name = db.Column(db.String(50), index=True)
    last_name = db.Column(db.String(50), index=True)
    email = db.Column(db.String(100), index=True, unique=True)

    def __init__(self, username, first_name, email):
        self.username = username
        self.first_name = first_name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.first_name


class RegistrationForm(Form):
    username = StringField('Username', [Length(min=4, max=20)])
    email = StringField('Email Address', [Length(min=6, max=100)])
    password = PasswordField('Password', [DataRequired(),
                                          EqualTo('confirm',
                                                  message='Passwords must match')])
    confirm = PasswordField('Retype Password')

    accept_tos = BooleanField('I accept the Terms of Service and the Privacy Notice',
                              [DataRequired()])


class LoginForm(Form):
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])

