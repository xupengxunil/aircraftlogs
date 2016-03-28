from app import db
from passlib.hash import sha256_crypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    pwd_hash = db.Column(db.String(100))

    def __init__(self, username, first_name, last_name, email, password):
        self.username = username.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.lower()
        self.set_password(password)

    def set_password(self, password):
        self.pwd_hash = sha256_crypt.encrypt((str(password)))

    def check_password(self, password):
        return sha256_crypt.verify(password, self.pwd_hash)

    def __repr__(self):
        return '<User %r>' % self.first_name
