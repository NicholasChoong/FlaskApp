from flask import Flask

# from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import base64
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime, timedelta
import os
from flask import url_for

app = Flask(__name__)
# app.config.from_object(Config)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.db")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String(128), primary_key=True)
    first_name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    isAdmin = db.Column(db.Boolean, default=False)
    # token authetication for api
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)

    results = db.relationship("Result", backref="user", lazy="dynamic")
    logs = db.relationship("Log", backref="user", lazy="dynamic")

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
            "password_hash": self.password_hash,
            "first_name": self.first_name,
            "surname": self.surname,
            "isAdmin": self.isAdmin,
            "_links": {"Reslts": url_for("get_user_results", id=self.user_id)},
        }
        return data

    def from_dict(self, data):
        if "user_id" in data:
            self.user_name = data["user_id"]
        if "first_name" in data:
            self.user_name = data["first_name"]
        if "surname" in data:
            self.user_name = data["surname"]
        if "isAdmin" in data:
            self.user_name = data["isAdmin"]
        if "password_hash" in data:
            self.set_password(data["password_hash"])

    def __repr__(self):
        return (
            f"[User ID: {self.user_id}, Name: {self.__str__()}, Admin: {self.isAdmin}]"
        )

    def __str__(self):
        return self.first_name + " " + self.surname


class Result(db.Model):
    __tablename__ = "results"
    result_id = db.Column(db.Integer, primary_key=True)
    marks = db.Column(db.Integer)
    correct_questions = db.Column(db.String(256))  # A string of booleans
    date = db.Column(db.DateTime, default=datetime.utcnow)  # date and time

    user_id = db.Column(db.String(128), db.ForeignKey("users.user_id"))

    answers = db.relationship("Answer", backref="result", lazy="dynamic")

    def to_dict(self):
        data = {
            "result_id": self.result_id,
            "marks": self.marks,
            "date": self.date,
            "user_id": self.user_id,
            "user_name": str(User.query.get(self.user_id).__str__()),
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
        return f"[Result ID: {self.result_id}, Marks: {self.marks}, Date: {self.date}, Name: {str(User.query.get(self.user_id).__str__())}]"

    def __str__(self):
        return f"Result {self.result_id}: {self.marks}"


class Answer(db.Model):
    __tablename__ = "answers"
    answer_id = db.Column(db.Integer, primary_key=True)

    result_id = db.Column(db.Integer, db.ForeignKey("results.result_id"))


class Log(db.Model):
    __tablename__ = "logs"
    log_id = db.Column(db.Integer, primary_key=True)
    login_key = db.Column(db.Integer, unique=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)  # date and time

    user_id = db.Column(db.String(128), db.ForeignKey("users.user_id"))

    def to_dict(self):
        data = {
            "log_id": self.log_id,
            "login_key": self.login_key,
            "date": self.date,
            "user_id": self.user_id,
        }
        return data

    def __repr__(self):
        return f"[Log ID: {self.log_id}, Login Key: {self.login_key}, User ID: {self.user_id}, Date: {self.date}]"


admin = User(
    user_id="admin1234",
    first_name="Jojn",
    surname="jej",
    password_hash="admin1234",
    isAdmin=True,
    token="awdwds",
)

res = Result(marks=8, correct_questions="1111001111", user_id="admin")

lg = Log(login_key="12313", user_id="admin")

db.create_all()
db.session.add(admin)
db.session.add(res)
db.session.add(
    User(
        user_id="Guest12345",
        first_name="Jojn",
        surname="jej",
        password_hash="admin12345",
        isAdmin=False,
    )
)
db.session.add(Result(marks=8, correct_questions="1111101111", user_id="admin1234"))
db.session.add(Result(marks=8, correct_questions="1111101111", user_id="admin1234"))
db.session.add(Result(marks=8, correct_questions="1111101111", user_id="admin1234"))
db.session.add(Result(marks=8, correct_questions="1111101111", user_id="admin1234"))
db.session.add(Result(marks=8, correct_questions="1111101111", user_id="admin1234"))
db.session.add(
    User(
        user_id="guest1234",
        first_name="John",
        surname="Doe",
        password_hash="guest1234",
        isAdmin=False,
        token="trthre",
    )
)
db.session.add(lg)
db.session.commit()


from app import *

User.query.all()
Result.query.all()
Result.query.filter_by(user_id=id)
Result.query.filter_by(user_id="admin").all()
Result.query.filter_by(user_id="admin").all()[-1]
Result.query.filter_by(user_id="admin")[-1]
Log.query.all()

admin = User.query.get("admin1234")
# Get results from user id
admin.results.first()
admin.results.all()
admin.results.filter_by(result_id=6).all()
