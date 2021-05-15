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
    questions = Question.query.all()
    if questions[0].answer_type == "MCQ":
        question_1 = RadioField(
            str(questions[0].question).encode("ascii", "ignore"),
            choices=[
                ("1", f"{questions[0].answer_choice_1}"),
                ("2", f"{questions[0].answer_choice_2}"),
                ("3", f"{questions[0].answer_choice_3}"),
                ("4", f"{questions[0].answer_choice_4}"),
            ],
        )
    elif questions[0].answer_type == "SAQ":
        question_1 = TextField(questions[0].question, validators=)

    question_2 = RadioField(
        str(questions[1].question).encode("ascii", "ignore"),
        choices=[
            ("1", f"{questions[1].answer_choice_1}"),
            ("2", f"{questions[1].answer_choice_2}"),
            ("3", f"{questions[1].answer_choice_3}"),
            ("4", f"{questions[1].answer_choice_4}"),
        ],
    )
    question_3 = RadioField(
        str(questions[2].question).encode("ascii", "ignore"),
        choices=[
            ("1", f"{questions[2].answer_choice_1}"),
            ("2", f"{questions[2].answer_choice_2}"),
            ("3", f"{questions[2].answer_choice_3}"),
            ("4", f"{questions[2].answer_choice_4}"),
        ],
    )
    question_4 = RadioField(
        str(questions[2].question).encode("ascii", "ignore"),
        choices=[
            ("1", f"{questions[3].answer_choice_1}"),
            ("2", f"{questions[3].answer_choice_2}"),
            ("3", f"{questions[3].answer_choice_3}"),
            ("4", f"{questions[3].answer_choice_4}"),
        ],
    )
    question_5 = RadioField(
        str(questions[2].question).encode("ascii", "ignore"),
        choices=[
            ("1", f"{questions[4].answer_choice_1}"),
            ("2", f"{questions[4].answer_choice_2}"),
            ("3", f"{questions[4].answer_choice_3}"),
            ("4", f"{questions[4].answer_choice_4}"),
        ],
    )
    question_6 = RadioField(
        str(questions[2].question).encode("ascii", "ignore"),
        choices=[
            ("1", f"{questions[5].answer_choice_1}"),
            ("2", f"{questions[5].answer_choice_2}"),
            ("3", f"{questions[5].answer_choice_3}"),
            ("4", f"{questions[5].answer_choice_4}"),
        ],
    )
    question_7 = RadioField(
        str(questions[2].question).encode("ascii", "ignore"),
        choices=[
            ("1", f"{questions[6].answer_choice_1}"),
            ("2", f"{questions[6].answer_choice_2}"),
            ("3", f"{questions[6].answer_choice_3}"),
            ("4", f"{questions[6].answer_choice_4}"),
        ],
    )
    # Experimental
    # Dynamic design
    # questions_dict = {}
    # for i, question in enumerate(questions):
    #     questions_dict[f"question_{i+1}"] = RadioField(
    #         str(question.question).encode("ascii", "ignore"),
    #         choices=[
    #             ("1", f"{question.answer_choice_1}"),
    #             ("2", f"{question.answer_choice_2}"),
    #             ("3", f"{question.answer_choice_3}"),
    #             ("4", f"{question.answer_choice_4}"),
    #         ],
    #     )

    submit = SubmitField("Submit Answers")