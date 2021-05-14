from flask import render_template, flash, redirect, url_for
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.controllers import (
    UserController,
    ResultController,
    LogController,
    AttemptController,
    QuestionController,
)
from flask import request
from werkzeug.urls import url_parse


@app.route("/favicon.ico")
def favicon():
    return redirect(url_for("static", filename="favicon.ico"), code=302)


@app.route("/")
@app.route("/index")
def index():
    # if not current_user.is_authenticated:
    #     return render_template("index.html", projects=[])
    return render_template("index.html", title="PC Wiki")


@app.route("/login", methods=["GET", "POST"])
def login():
    if not current_user.is_authenticated:
        return UserController.login()
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    return UserController.logout()


@app.route("/register", methods=["GET", "POST"])
def register():
    return UserController.register()


@app.route("/learn")
def learn():
    return render_template("content.html", title="Learning")


@app.route("/review")
def review():
    return render_template("review.html", title="Review")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    return render_template("quiz.html", title="quiz")  ##### placeholder
    # return AttemptController.quiz()