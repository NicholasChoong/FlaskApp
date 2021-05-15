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
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # date and time
    # token authetication for api
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    results = db.relationship("Result", backref="user", lazy="dynamic")
    logs = db.relationship("Log", backref="user", lazy="dynamic")
    attempts = db.relationship("Attempt", backref="user", lazy="dynamic")

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
            "date": self.date,
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
        if "date" in data:
            self.date = data["date"]

    def __repr__(self):
        return f"[id: {self.id}, name: {self.__str__()}, isAdmin: {self.isAdmin}]"

    def __str__(self):
        return self.first_name + " " + self.surname


class Result(db.Model):
    __tablename__ = "results"
    result_id = db.Column(db.Integer, primary_key=True)
    marks = db.Column(db.Integer, default=0)
    correct_questions = db.Column(db.String(256))  # A string of booleans
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # date and time

    user_id = db.Column(db.String(128), db.ForeignKey("users.id"))
    attempt = db.relationship(
        "Attempt", backref="result", uselist=False
    )  ## one-to-one relation

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


class Attempt(db.Model):
    __tablename__ = "attempts"
    attempt_id = db.Column(db.Integer, primary_key=True)
    answer_1 = db.Column(db.String(256), nullable=True)
    answer_2 = db.Column(db.String(256), nullable=True)
    answer_3 = db.Column(db.String(256), nullable=True)
    answer_4 = db.Column(db.String(256), nullable=True)
    answer_5 = db.Column(db.String(256), nullable=True)
    answer_6 = db.Column(db.String(256), nullable=True)
    answer_7 = db.Column(db.String(256), nullable=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # date and time

    result_id = db.Column(db.Integer, db.ForeignKey("results.result_id"))
    user_id = db.Column(db.String(128), db.ForeignKey("users.id"))

    def to_dict(self):
        data = {
            "attempt_id": self.attempt_id,
            "answer_1": self.answer_1,
            "answer_2": self.answer_2,
            "answer_3": self.answer_3,
            "answer_4": self.answer_4,
            "answer_5": self.answer_5,
            "answer_6": self.answer_6,
            "answer_7": self.answer_7,
            "date": self.date,
            "result_id": self.result_id,
            "user_id": self.user_id,
        }
        return data

    def from_dict(self, data):
        if "attempt_id" in data:
            self.attempt_id = data["attempt_id"]
        if "answer_1" in data:
            self.answer_1 = data["answer_1"]
        if "answer_2" in data:
            self.answer_2 = data["answer_2"]
        if "answer_3" in data:
            self.answer_3 = data["answer_3"]
        if "answer_4" in data:
            self.answer_4 = data["answer_4"]
        if "answer_5" in data:
            self.answer_5 = data["answer_5"]
        if "answer_6" in data:
            self.answer_6 = data["answer_6"]
        if "answer_7" in data:
            self.answer_7 = data["answer_7"]
        if "date" in data:
            self.date = data["date"]
        if "result_id" in data:
            self.result_id = data["result_id"]
        if "user_id" in data:
            self.user_id = data["user_id"]

    def __repr__(self):
        return f"[attempt_id: {self.attempt_id}, marks: {Result.query.get(self.result_id).marks}, date: {self.date}, name: {User.query.get(self.user_id).__str__()}]"


class Answer(db.Model):
    """User Answers"""

    __tablename__ = "answers"
    answer_id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String(256), nullable=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # date and time
    question_id = db.Column(db.String(128), db.ForeignKey("questions.question_id"))

    def to_dict(self):
        data = {
            "answer_id": self.answer_id,
            "answer": self.answer,
            "date": self.date,
            "question_id": self.question_id,
        }
        return data

    def from_dict(self, data):
        if "answer_id" in data:
            self.answer_id = data["answer_id"]
        if "answer" in data:
            self.answer = data["answer"]
        if "date" in data:
            self.date = data["date"]
        if "question_id" in data:
            self.question_id = data["question_id"]

    def __repr__(self):
        return f"[question_id: {self.question_id}, question: {self.question}, answer: {self.answer}, date: {self.date}]"


class Question(db.Model):
    __tablename__ = "questions"
    question_id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(256))
    answer_type = db.Column(db.String(256))
    answer_choice_1 = db.Column(db.String(256), nullable=True)
    answer_choice_2 = db.Column(db.String(256), nullable=True)
    answer_choice_3 = db.Column(db.String(256), nullable=True)
    answer_choice_4 = db.Column(db.String(256), nullable=True)
    answer = db.Column(db.String(256))
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # date and time

    attempted_answers = db.relationship("Answer", backref="questions", lazy="dynamic")

    def to_dict(self):
        data = {
            "question_id": self.question_id,
            "question": self.question,
            "answer_type": self.answer_type,
            "answer_choice_1": self.answer_choice_1,
            "answer_choice_2": self.answer_choice_2,
            "answer_choice_3": self.answer_choice_3,
            "answer_choice_4": self.answer_choice_4,
            "answer": self.answer,
            "date": self.date,
        }
        return data

    def from_dict(self, data):
        if "question_id" in data:
            self.question_id = data["question_id"]
        if "question" in data:
            self.question = data["question"]
        if "answer_type" in data:
            self.answer_type = data["answer_type"]
        if "answer_choice_1" in data:
            self.answer_choice_1 = data["answer_choice_1"]
        if "answer_choice_2" in data:
            self.answer_choice_2 = data["answer_choice_2"]
        if "answer_choice_3" in data:
            self.answer_choice_3 = data["answer_choice_3"]
        if "answer_choice_4" in data:
            self.answer_choice_4 = data["answer_choice_4"]
        if "answer" in data:
            self.answer = data["answer"]
        if "date" in data:
            self.date = data["date"]

    def __repr__(self):
        return f"[question_id: {self.question_id}, question: {self.question}, answer: {self.answer}, date: {self.date}]"


class Log(db.Model):
    __tablename__ = "logs"
    log_id = db.Column(db.Integer, primary_key=True)
    login_key = db.Column(db.Integer, unique=True)
    date = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # date and time

    user_id = db.Column(db.String(128), db.ForeignKey("users.id"))

    def to_dict(self):
        data = {
            "log_id": self.log_id,
            "login_key": self.login_key,
            "date": self.date,
            "user_id": self.user_id,
        }
        return data

    def from_dict(self, data):
        if "log_id" in data:
            self.log_id = data["log_id"]
        if "login_key" in data:
            self.login_key = data["login_key"]
        if "date" in data:
            self.date = data["date"]
        if "user_id" in data:
            self.user_id = data["user_id"]

    def __repr__(self):
        return f"[log_id: {self.log_id}, login_key: {self.login_key}, user_id: {self.user_id}, date: {self.date}]"
