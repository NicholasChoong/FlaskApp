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
        "Pick 1",
        choice=[
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
        ],
    )
    question_2 = RadioField(
        "Pick 2",
        choice=[
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
        ],
    )
    question_3 = RadioField(
        "Pick 3",
        choice=[
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
        ],
    )
    question_4 = RadioField(
        "Pick 4",
        choice=[
            ("1", "1"),
            ("2", "2"),
            ("3", "3"),
            ("4", "4"),
        ],
    )
    question_5 = RadioField(
        "Pick 5",
        choice=[
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
        ],
    )
    question_6 = RadioField(
        "Pick 6",
        choice=[
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
        ],
    )
    question_7 = RadioField(
        "Pick 7",
        choice=[
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
        ],
    )
    submit = SubmitField("Submit Answers")

    # elif questions[6].answer_type == "SAQ":
    #     question_7 = TextField(
    #         questions[6].question,
    #         validators=[regexp(f"^\w{{{len(questions[6].answer)}}}$")],
    #     )
    # Experimental
    # Dynamic design
    # questions_dict = {}
    # for i, question in enumerate(questions):
    #     questions_dict[f"question_{i+1}"] = RadioField(
    #         str(question.question).encode("ascii", "ignore"),
    #         choice=[
    #             ("1", f"{question.answer_choice_1}"),
    #             ("2", f"{question.answer_choice_2}"),
    #             ("3", f"{question.answer_choice_3}"),
    #             ("4", f"{question.answer_choice_4}"),
    #         ],
    #     )
