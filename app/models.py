import base64
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import url_for
from datetime import datetime, timedelta
import os


@login.user_loader
def load_user(id):
    return User.query.get(id)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(128), primary_key=True)
    first_name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    isAdmin = db.Column(db.Boolean, default=False)
    # token authetication for api
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    ###Token support methods for api

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode("utf-8")
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user

    """Adding in dictionary methods to convert to JSON
     Format
     {
     'id':'19617810',
     'first_name':'Timothy',
     'surname': 'French',
     'prefered_name':'Tim',
     'cits3403':False,
     'pin':'0000',
     '_links':{
       'project': 'api/student/19617810/project'
      }
    }"""

    def to_dict(self):
        data = {
            "id": self.id,
            "password_hash": self.password_hash,
            "first_name": self.first_name,
            "surname": self.surname,
            "isAdmin": self.isAdmin,
        }
        return data

    def from_dict(self, data):
        if "id" in data:
            self.user_id = data["id"]
        if "first_name" in data:
            self.first_name = data["first_name"]
        if "surname" in data:
            self.surname = data["surname"]
        if "isAdmin" in data:
            self.isAdmin = data["isAdmin"]
        if "password_hash" in data:
            self.set_password(data["password_hash"])

    def __repr__(self):
        return f"[id: {self.id}, name: {self.__str__()}, isAdmin: {self.isAdmin}]"

    def __str__(self):
        return self.first_name + " " + self.surname


class Result(db.Model):
    __tablename__ = "results"
    result_id = db.Column(db.Integer, primary_key=True)
    marks = db.Column(db.Integer)
    correct_questions = db.Column(db.String(256))  # A string of booleans
    date = db.Column(db.DateTime, default=datetime.utcnow)  # date and time

    user_id = db.Column(db.String(128), db.ForeignKey("users.id"))

    def to_dict(self):
        data = {
            "result_id": self.result_id,
            "marks": self.marks,
            "date": self.date,
            "user_id": self.id,
            "user_name": User.query.get(self.user_id).__str__(),
        }
        return data

    def from_dict(self, data):
        if "result_id" in data:
            self.result_id = data["result_id"]
        if "marks" in data:
            self.marks = data["marks"]
        if "correct_questions" in data:
            self.correct_questions = data["correct_questions"]
        if "date" in data:
            self.date = data["date"]
        if "user_id" in data:
            self.user_id = data["user_id"]

    def __repr__(self):
        return f"[result_id: {self.result_id}, marks: {self.marks}, date: {self.date}, name: {User.query.get(self.user_id).__str__()}]"

    def __str__(self):
        return f"result {self.result_id}: {self.marks}"


class Log(db.Model):
    __tablename__ = "logs"
    log_id = db.Column(db.Integer, primary_key=True)
    login_key = db.Column(db.Integer, unique=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)  # date and time

    user_id = db.Column(db.String(128), db.ForeignKey("users.id"))

    def to_dict(self):
        data = {
            "log_id": self.log_id,
            "login_key": self.login_key,
            "date": self.date,
            "user_id": self.user_id,
        }
        return data

    def __repr__(self):
        return f"[log_id: {self.log_id}, login_key: {self.login_key}, user_id: {self.user_id}, date: {self.date}]"
