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
    admin = User(
        id="UWAadmin",
        first_name="UWA",
        surname="admin",
        isAdmin=True,
    )
    admin.set_password("UWAadmin")
    # db.session.add(
    #     Question(
    #         question="Which component needs a fan or many fans to cool down?",
    #         answer_type="MCQ",
    #         answer_choice_1="M.2 Solid State Drive",
    #         answer_choice_2="Random Access Memory",
    #         answer_choice_3="Central Processing Unit",
    #         answer_choice_4="I/O Shield",
    #         answer="Central Processing Unit",
    #     )
    # )
    # db.session.add(
    #     Question(
    #         question="Which of the following is the first step of assembling a PC?",
    #         answer_type="MCQ",
    #         answer_choice_1="Installing a CPU to a motherboard",
    #         answer_choice_2="Installing a motherboard to a PC case",
    #         answer_choice_3="Connecting power and SATA cables to various components",
    #         answer_choice_4="Applying thermal paste onto the CPU",
    #         answer="Installing a CPU to a motherboard",
    #     )
    # )
    # db.session.add(
    #     Question(
    #         question="In figure 1, which slots should the RAMs be installed in?",
    #         answer_type="MCQ",
    #         answer_choice_1="8",
    #         answer_choice_2="5",
    #         answer_choice_3="7",
    #         answer_choice_4="4",
    #         answer="8",
    #     )
    # )
    # db.session.add(
    #     Question(
    #         question="In figure 1, which slots should the GPUs be installed in?",
    #         answer_type="MCQ",
    #         answer_choice_1="6",
    #         answer_choice_2="3",
    #         answer_choice_3="7",
    #         answer_choice_4="5",
    #         answer="7",
    #     )
    # )
    # db.session.add(
    #     Question(
    #         question="In figure 1, what is 3?",
    #         answer_type="MCQ",
    #         answer_choice_1="6-pin connectors",
    #         answer_choice_2="HDMI",
    #         answer_choice_3="Bluetooth",
    #         answer_choice_4="SATA connectors",
    #         answer="SATA connectors",
    #     )
    # )
    # db.session.add(
    #     Question(
    #         question="Do you need to apply thermal paste if you are using stock cooler for your CPU?",
    #         answer_type="MCQ",
    #         answer_choice_1="Yes",
    #         answer_choice_2="No",
    #         answer_choice_3="I don't know",
    #         answer_choice_4="I do not need a cooler for my CPU",
    #         answer="No",
    #     )
    # )
    # db.session.add(
    #     Question(
    #         question="A ___________ is a main printed circuit board that allows communications between different electronic components",
    #         answer_type="SAQ",
    #         answer="motherboard",
    #     )
    # )
    # db.session.add(admin)
    # db.session.commit()


from app import routes, models