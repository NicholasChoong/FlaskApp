from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, regexp, EqualTo
from app.models import User, Result, Log, Result, Question, Attempt

"""class to hold elements and validators for login form"""

MSG = "must be less than 128 charecter"


class LoginForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), regexp("^\w{1,128}$", message=MSG)]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            regexp(
                "^\w{1,128}$",
                message=MSG,
            ),
        ],
    )
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


"""class to hold elements and validators for registration form"""


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), regexp("^\w{1,128}$", message=MSG)]
    )
    first_name = StringField("First name", validators=[])
    surname = StringField("Surname", validators=[])
    password = PasswordField(
        "Current Password",
        validators=[DataRequired(), regexp("^\w{1,128}$", message=MSG)],
        default="password",
    )
    new_password = PasswordField(
        "New Password", validators=[DataRequired(), regexp("^\w{1,128}$", message=MSG)]
    )
    repeat_new_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("new_password", message="Passwords must match"),
        ],
    )
    submit = SubmitField("Sign up")


class QuizForm(FlaskForm):
    pass