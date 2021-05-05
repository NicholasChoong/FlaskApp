import base64
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import url_for
from datetime import datetime, timedelta
import os


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String(8), primary_key=True)
    first_name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    isAdmin = db.Column(db.Boolean, default=False)
    # token authetication for api
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    result = db.relationship("Assessment", backref="user", lazy="dynamic")

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
            "user_id": self.user_id,
            "first_name": self.first_name,
            "surname": self.surname,
            "isAdmin": self.isAdmin,
            "_links": {"project": url_for("get_student_project", id=self.id)},
        }
        return data

    def from_dict(self, data):
        if "prefered_name" in data:
            self.prefered_name = data["prefered_name"]
        if "pin" in data:
            self.set_password(data["pin"])

    def __repr__(self):
        return (
            f"[User ID:{self.user_id}, Name:{self.__str__()}, is Admin:{self.isAdmin}]"
        )

    def __str__(self):
        return self.first_name + " " + self.surname


class Assessment(db.Model):
    __tablename__ = "assessments"
    assessment_id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(256))

    """returns a list of questions"""

    def to_dict(self):
        data = {
            "assessment_id": self.assessment_id,
            "question": self.question,
        }
        return data

    def from_dict(self, data):
        if "question" in data:
            self.question = data["question"]

    def __repr__(self):
        return f"[Assessment ID:{self.assessment_id}, Question:{self.question}]"

    def __str__(self):
        return f"Assessment {self.assessment_id}: {self.question}"


class Log(db.Model):
    __tablename__ = "logs"
    login_key = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(8), db.ForeignKey("users.user_id"))
    time = db.Column(db.String(64))  # date and time

    def __repr__(self):
        return f"[Login Key:{self.login_key}, User ID:{self.user_id}, time:{self.time}]"