from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    SelectField,
    RadioField,
    TextField,
)
from wtforms.validators import DataRequired, regexp, EqualTo
from app.models import User, Log, Question, Attempt
from sqlalchemy.exc import OperationalError

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
    question_1 = RadioField(
        "Which component needs a fan or many fans to cool down?",
        choices=[
            "M.2 Solid State Drive",
            "Random Access Memory",
            "Central Processing Unit",
            "I/O Shield",
        ],
    )
    question_2 = RadioField(
        "Which of the following is the first step of assembling a PC?",
        choices=[
            "Installing a CPU to a motherboard",
            "Installing a motherboard to a PC case",
            "Connecting power and SATA cables to various components",
            "Applying thermal paste onto the CPU",
        ],
    )
    question_3 = RadioField(
        "In figure 1, which slots should the RAMs be installed in?",
        choices=[
            "8",
            "5",
            "7",
            "4",
        ],
    )
    question_4 = RadioField(
        "In figure 1, which slots should the GPUs be installed in?",
        choices=[
            "6",
            "3",
            "7",
            "5",
        ],
    )
    question_5 = RadioField(
        "In figure 1, what is 3?",
        choices=[
            "6-pin connectors",
            "HDMI",
            "Bluetooth",
            "SATA connectors",
        ],
    )
    question_6 = RadioField(
        "Do you need to apply thermal paste if you are using stock cooler for your CPU?",
        choices=[
            "Yes",
            "No",
            "I don't know",
            "I do not need a cooler for my CPU",
        ],
    )
    question_7 = TextField(
        "A ___________ is a main printed circuit board that allows communications between different electronic components",
        validators=[regexp("^\w{11}$")],
    )
    submit = SubmitField("Submit Answers")
