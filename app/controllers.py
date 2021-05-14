from flask import render_template, flash, redirect, url_for, request
from app import app, db
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import LoginForm, RegistrationForm
from app.models import User, Result, Log
from werkzeug.urls import url_parse
from datetime import datetime


class UserController:
    def login():
        lform = LoginForm()
        rform = RegistrationForm()  # ??include current user data by default

        if lform.validate_on_submit():  # will return false for a get request
            user = User.query.get(lform.username.data)
            if user is None or not user.check_password(lform.password.data):
                flash("invalid username or password")
                return render_template(
                    "login.html", title="Login", signinform=lform, signupform=rform
                )
            login_user(user, remember=lform.remember_me.data)
            # next_page = request.args.get("next")
            # if not next_page or url_parse(next_page).netloc != "":
            #     next_page = "index"
            return redirect(url_for("index"))
        return render_template(
            "login.html", title="Login", signinform=lform, signupform=rform
        )
        # return redirect(url_for('static', filename='login.html'))

    def logout():
        logout_user()
        return redirect(url_for("index"))

    def register():
        form = RegistrationForm()  # ??include current user data by default
        lform = LoginForm()
        if form.validate_on_submit():  # will return false for a GET request
            user = User()
            user.id = form.username.data
            user.set_password(form.new_password.data)
            user.first_name = form.first_name.data
            user.surname = form.surname.data
            if user is None:
                flash("Username is unknown")
                return redirect(url_for("index"))
            if current_user.is_authenticated:
                if not user.check_password(form.password.data):
                    flash("Incorrect password")
                    return redirect(url_for("index"))
            # elif user.password_hash is not None:
            #     flash("User registered")
            #     return redirect(url_for("index"))
            if User.query.get(form.username.data) is not None:
                flash("Username is already taken")
                return render_template(
                    "login.html", title="Register", signupform=form, signinform=lform
                )
            db.session.add(user)
            db.session.flush()
            db.session.commit()
            login_user(user, remember=False)
            return redirect(url_for("index"))
        return render_template(
            "login.html", title="Register", signupform=form, signinform=lform
        )


class ResultController:
    pass
    # def result_list():
    #     results = ResultController.get_all_results()
    #     return render_template("index.html", results=results)

    # def new_project():
    #     if not current_user.project_id == None:
    #         flash(current_user.prefered_name + " already has a project")
    #         return redirect(url_for("index"))
    #     form = ProjectForm()
    #     form.lab.choices = ProjectController.get_labs()
    #     if form.validate_on_submit():  # for post requests
    #         partners = [current_user]
    #         partners.append(
    #             Student.query.filter_by(id=form.partner1_number.data).first()
    #         )
    #         partners.append(
    #             Student.query.filter_by(id=form.partner2_number.data).first()
    #         )
    #         partners.append(
    #             Student.query.filter_by(id=form.partner3_number.data).first()
    #         )
    #         team = [p for p in partners if p != None]
    #         # illegal scenarios
    #         if len(team) < 2:
    #             flash("At least two students per group")
    #             return redirect(url_for("index"))
    #         distinct = False
    #         for partner in team:
    #             if partner.is_committed():
    #                 flash(partner.prefered_name + " already has a project assigned")
    #                 return redirect(url_for("index"))
    #             if partner.id != current_user.id:
    #                 distinct = True
    #         if not distinct:
    #             flash("At least two students per group")
    #             return redirect(url_for("index"))
    #         # check lab availability
    #         lab = Lab.query.filter_by(lab_id=form.lab.data).first()
    #         if lab is None or not lab.is_available():
    #             flash("Lab not available")
    #             return redirect(url_for("index"))
    #         # Everything is good, make commits
    #         ProjectController.make_project(form.project_description.data, lab, team)
    #         return redirect(url_for("index"))
    #     return render_template("new_project.html", student=current_user, form=form)

    # def make_project(description, lab, team):
    #     project = Project()
    #     project.description = description
    #     project.lab_id = lab.lab_id
    #     db.session.add(project)
    #     db.session.flush()  # generates pk for new project
    #     for student in team:
    #         student.project_id = project.project_id
    #     db.session.commit()
    #     return project

    # def edit_project():
    #     project = Project.query.filter_by(project_id=current_user.project_id).first()
    #     if project == None:
    #         flash(current_user.prefered_name + " does not have a project yet")
    #         redirect(url_for("new_project"))
    #     team = project.get_team()
    #     form = ProjectForm()  # initialise with parameters
    #     form.lab.choices = ProjectController.get_labs(project.lab_id)
    #     if form.validate_on_submit():  # for post requests
    #         lab = Lab.query.filter_by(lab_id=form.lab.data).first()
    #         if lab is None or not (lab.lab_id == project.lab_id or lab.is_available()):
    #             flash("Lab not available")
    #         else:
    #             project.description = form.project_description.data
    #             project.lab_id = lab.lab_id
    #             db.session.add(project)
    #             db.session.commit()
    #             return redirect(url_for("index"))
    #     return render_template(
    #         "edit_project.html", team=team, project=project, form=form
    #     )

    # def delete_project():
    #     project = Project.query.filter_by(project_id=current_user.project_id).first()
    #     if project is None:
    #         flash(current_user.prefered_name + " does not have a project")
    #     else:
    #         flash(
    #             current_user.prefered_name
    #             + "'s project "
    #             + project.description
    #             + " deleted."
    #         )
    #         for s in project.get_team():
    #             s.project_id = None
    #         db.session.delete(project)
    #         db.session.commit()
    #         return redirect(url_for("index"))

    # """Get's a string representing the team members"""

    # def get_team_string(team):
    #     team_str = team[0].prefered_name
    #     for i in range(1, len(team)):
    #         team_str = (
    #             team_str
    #             + (", " if i < len(team) - 1 else " & ")
    #             + team[i].prefered_name
    #         )
    #     return team_str

    # """returns list of registered projects as a list of dictionaries, with elements "project", "team" and "lab". Used by index to display project list."""

    # def get_all_results():
    #     result_list = Result.query.all()
    #     results = []
    #     for result in result_list:
    #         team_str = ProjectController.get_team_string(p.get_team())
    #         l = Lab.query.filter_by(lab_id=p.lab_id).first()
    #         dt = datetime.strptime(l.time, "%Y-%m-%dT%H:%M")
    #         time = dt.strftime("%A %d %b, %H:%M")
    #         lab = l.lab
    #         projects.append(
    #             {
    #                 "project_id": p.project_id,
    #                 "description": p.description,
    #                 "team": team_str,
    #                 "lab": lab,
    #                 "time": time,
    #             }
    #         )
    #     projects.sort(key=lambda p: p["time"] + p["lab"])
    #     return projects

    # """Returns available labs formatted for a select input, including the current lab"""

    # def get_labs(lab_id=None):
    #     labs = Lab.get_available_labs()
    #     if lab_id != None:
    #         lab = Lab.query.get(lab_id)
    #         dt = datetime.strptime(lab.time, "%Y-%m-%dT%H:%M")
    #         choices = [(str(lab.lab_id), dt.strftime("%A %d %b, %H:%M"))]
    #     else:
    #         choices = []
    #     for l in labs:
    #         dt = datetime.strptime(l.time, "%Y-%m-%dT%H:%M")
    #         choices.append((str(l.lab_id), dt.strftime("%A %d %b, %H:%M")))
    #     return choices
class ReviewController:
    def get_User_Results():
        Rev = Result.query.filter_by(user_id = current_user.id).all()
        return render_template("review.html", title="Review", Res = Rev)




class AttemptController:
    def quiz():
        pass


class QuestionController:
    pass


class LogController:
    def get_all_logs():
        pass
