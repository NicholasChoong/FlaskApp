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
    questions = [
        Question(
            question="Pick 1",
            answer_type="MCQ",
            answer_choice_1="1",
            answer_choice_2="2",
            answer_choice_3="3",
            answer_choice_4="4",
            answer="1",
        ),
        Question(
            question="Pick 2",
            answer_type="MCQ",
            answer_choice_1="1",
            answer_choice_2="2",
            answer_choice_3="3",
            answer_choice_4="4",
            answer="2",
        ),
        Question(
            question="Pick 3",
            answer_type="MCQ",
            answer_choice_1="1",
            answer_choice_2="2",
            answer_choice_3="3",
            answer_choice_4="4",
            answer="3",
        ),
        Question(
            question="Pick 4",
            answer_type="MCQ",
            answer_choice_1="1",
            answer_choice_2="2",
            answer_choice_3="3",
            answer_choice_4="4",
            answer="4",
        ),
        Question(
            question="Pick 5",
            answer_type="MCQ",
            answer_choice_1="5",
            answer_choice_2="6",
            answer_choice_3="7",
            answer_choice_4="8",
            answer="1",
        ),
        Question(
            question="Pick 6",
            answer_type="MCQ",
            answer_choice_1="5",
            answer_choice_2="6",
            answer_choice_3="7",
            answer_choice_4="8",
            answer="2",
        ),
        Question(
            question="Pick 7",
            answer_type="MCQ",
            answer_choice_1="5",
            answer_choice_2="6",
            answer_choice_3="7",
            answer_choice_4="8",
            answer="3",
        ),
    ]
    if questions[0].answer_type == "MCQ":
        question_1 = RadioField(
            str(questions[0].question),
            choices=[
                ("1", f"{questions[0].answer_choice_1}"),
                ("2", f"{questions[0].answer_choice_2}"),
                ("3", f"{questions[0].answer_choice_3}"),
                ("4", f"{questions[0].answer_choice_4}"),
            ],
        )
    elif questions[0].answer_type == "SAQ":
        question_1 = TextField(
            questions[0].question,
            validators=[regexp(f"^\w{{{len(questions[0].answer)}}}$")],
        )

    if questions[1].answer_type == "MCQ":
        question_2 = RadioField(
            str(questions[1].question),
            choices=[
                ("1", f"{questions[1].answer_choice_1}"),
                ("2", f"{questions[1].answer_choice_2}"),
                ("3", f"{questions[1].answer_choice_3}"),
                ("4", f"{questions[1].answer_choice_4}"),
            ],
        )
    elif questions[1].answer_type == "SAQ":
        question_2 = TextField(
            questions[1].question,
            validators=[regexp(f"^\w{{{len(questions[1].answer)}}}$")],
        )

    if questions[2].answer_type == "MCQ":
        question_3 = RadioField(
            str(questions[2].question),
            choices=[
                ("1", f"{questions[2].answer_choice_1}"),
                ("2", f"{questions[2].answer_choice_2}"),
                ("3", f"{questions[2].answer_choice_3}"),
                ("4", f"{questions[2].answer_choice_4}"),
            ],
        )
    elif questions[2].answer_type == "SAQ":
        question_3 = TextField(
            questions[2].question,
            validators=[regexp(f"^\w{{{len(questions[2].answer)}}}$")],
        )

    if questions[3].answer_type == "MCQ":
        question_4 = RadioField(
            str(questions[3].question),
            choices=[
                ("1", f"{questions[3].answer_choice_1}"),
                ("2", f"{questions[3].answer_choice_2}"),
                ("3", f"{questions[3].answer_choice_3}"),
                ("4", f"{questions[3].answer_choice_4}"),
            ],
        )
    elif questions[3].answer_type == "SAQ":
        question_4 = TextField(
            questions[3].question,
            validators=[regexp(f"^\w{{{len(questions[3].answer)}}}$")],
        )

    if questions[4].answer_type == "MCQ":
        question_5 = RadioField(
            str(questions[4].question),
            choices=[
                ("1", f"{questions[4].answer_choice_1}"),
                ("2", f"{questions[4].answer_choice_2}"),
                ("3", f"{questions[4].answer_choice_3}"),
                ("4", f"{questions[4].answer_choice_4}"),
            ],
        )
    elif questions[4].answer_type == "SAQ":
        question_5 = TextField(
            questions[4].question,
            validators=[regexp(f"^\w{{{len(questions[4].answer)}}}$")],
        )

    if questions[5].answer_type == "MCQ":
        question_6 = RadioField(
            str(questions[5].question),
            choices=[
                ("1", f"{questions[5].answer_choice_1}"),
                ("2", f"{questions[5].answer_choice_2}"),
                ("3", f"{questions[5].answer_choice_3}"),
                ("4", f"{questions[5].answer_choice_4}"),
            ],
        )
    elif questions[5].answer_type == "SAQ":
        question_6 = TextField(
            questions[5].question,
            validators=[regexp(f"^\w{{{len(questions[5].answer)}}}$")],
        )

    if questions[6].answer_type == "MCQ":
        question_7 = RadioField(
            str(questions[6].question),
            choices=[
                ("1", f"{questions[6].answer_choice_1}"),
                ("2", f"{questions[6].answer_choice_2}"),
                ("3", f"{questions[6].answer_choice_3}"),
                ("4", f"{questions[6].answer_choice_4}"),
            ],
        )
    elif questions[6].answer_type == "SAQ":
        question_7 = TextField(
            questions[6].question,
            validators=[regexp(f"^\w{{{len(questions[6].answer)}}}$")],
        )
    submit = SubmitField("Submit Answers")
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
