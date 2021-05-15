from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"

# create all tables from models
@app.before_first_request
def create_tables():
    from app.models import User, Log, Question, Attempt

    db.create_all()
    db.session.add(
        Question(
            question="Pick 1",
            answer_type="MCQ",
            answer_choice_1="1",
            answer_choice_2="2",
            answer_choice_3="3",
            answer_choice_4="4",
            answer="1",
        )
    )
    db.session.add(
        Question(
            question="Pick 2",
            answer_type="MCQ",
            answer_choice_1="1",
            answer_choice_2="2",
            answer_choice_3="3",
            answer_choice_4="4",
            answer="2",
        )
    )
    db.session.add(
        Question(
            question="Pick 3",
            answer_type="MCQ",
            answer_choice_1="1",
            answer_choice_2="2",
            answer_choice_3="3",
            answer_choice_4="4",
            answer="3",
        )
    )
    db.session.add(
        Question(
            question="Pick 4",
            answer_type="MCQ",
            answer_choice_1="1",
            answer_choice_2="2",
            answer_choice_3="3",
            answer_choice_4="4",
            answer="4",
        )
    )
    db.session.add(
        Question(
            question="Pick 5",
            answer_type="MCQ",
            answer_choice_1="5",
            answer_choice_2="6",
            answer_choice_3="7",
            answer_choice_4="8",
            answer="1",
        )
    )
    db.session.add(
        Question(
            question="Pick 6",
            answer_type="MCQ",
            answer_choice_1="5",
            answer_choice_2="6",
            answer_choice_3="7",
            answer_choice_4="8",
            answer="2",
        )
    )
    db.session.add(
        Question(
            question="Pick 7",
            answer_type="MCQ",
            answer_choice_1="5",
            answer_choice_2="6",
            answer_choice_3="7",
            answer_choice_4="8",
            answer="3",
        )
    )
    db.session.commit()


from app import routes, models