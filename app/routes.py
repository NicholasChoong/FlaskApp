from flask import render_template, flash, redirect, url_for
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.controllers import UserController, ResultController, LogController
from flask import request
from werkzeug.urls import url_parse


@app.route("/favicon.ico")
def favicon():
    return redirect(url_for("static", filename="favicon.ico"), code=302)


@app.route("/")
@app.route("/index")
def index():
    if not current_user.is_authenticated:
        return render_template("index.html", projects=[])
    return ProjectController.project_list()


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


# @app.route("/new_project", methods=["GET", "POST"])
# @login_required
# def new_project():
#     if not current_user.is_authenticated:
#         return redirect(url_for("login"))
#     return ProjectController.new_project()


# @app.route("/edit_project", methods=["GET", "POST"])
# @login_required
# def edit_project():
#     if not current_user.is_authenticated:
#         return redirect(url_for("login"))
#     return ProjectController.edit_project()


# @app.route("/delete_project", methods=["GET"])
# @login_required
# def delete_project():
#     if not current_user.is_authenticated:
#         return redirect(url_for("login"))
#     return ProjectController.delete_project()
