from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, regexp, EqualTo
from app.models import User, Result, Log

"""class to hold elements and validators for login form"""

MSG = "must be between 8-16 characters and no special characters"


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            regexp(
                "^\w{8,16}$",
                message=MSG,
            ),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            regexp(
                "^\w{8-16}$",
                message=MSG,
            )
        ],
    )
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


"""class to hold elements and validators for registration form"""


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), regexp("^\w{8,16}$", message=MSG)],
    )
    password = PasswordField(
        "Current Password",
        validators=[regexp("^\w{8,16}$", message=MSG)],
        default="0000",
    )
    new_password = PasswordField(
        "New Password", validators=[regexp("^\w{8,16}$", message=MSG)]
    )
    repeat_new_password = PasswordField(
        "Confirm Password",
        validators=[EqualTo("new_password", message="Passwords must match")],
    )
    submit = SubmitField("Sign up")