from app import app, db
from app.models import User, Log, Question, Attempt
from app.api.errors import bad_request, error_response
from flask import jsonify, url_for, request, g, abort
from app.api.auth import token_auth


@app.route("/api/users/<id>", methods=["GET"])
@token_auth.login_required
def get_user(id):
    print(g.current_user)
    if g.current_user.id != id:
        abort(403)
    return jsonify(User.query.get_or_404(id).to_dict())


@app.route("/api/users", methods=["POST"])
def register_user():
    data = request.get_json() or {}
    if "id" not in data or "password_hash" not in data:
        return bad_request("Must include username and password")
    user = User.query.get(data["id"])
    if user is None:
        return bad_request("Unknown user")
    if user.password_hash is not None:
        return bad_request("User already registered")
    user.from_dict(data)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201  # creating a new resource should chare the location....
    response.headers["Location"] = url_for("get_user", id=user.id)
    return response


@app.route("/api/users/<id>/attempts", methods=["POST"])
@token_auth.login_required
def new_user_attempt(id):
    if g.current_user.id != id:
        abort(403)
    data = request.get_json() or {}
    # if "marks" not in data or "result_id" not in data:
    #     return bad_request("Must include marks and result_id")
    user = User.query.get(id)
    if user is None:
        return bad_request("Unknown user, or wrong id")
    attempt = Attempt()
    attempt.from_dict(data)
    questions = Question.query.all()
    attempt.correct_1 = questions[0].answer == attempt.answer_1
    attempt.correct_2 = questions[1].answer == attempt.answer_2
    attempt.correct_3 = questions[2].answer == attempt.answer_3
    attempt.correct_4 = questions[3].answer == attempt.answer_4
    attempt.correct_5 = questions[4].answer == attempt.answer_5
    attempt.correct_6 = questions[5].answer == attempt.answer_6
    attempt.correct_7 = questions[6].answer == attempt.answer_7
    db.session.flush()
    db.session.commit()
    response = jsonify(attempt.to_dict())
    response.status_code = 201  # creating a new resource should chare the location....
    response.headers["Location"] = url_for("new_user_attempt", id=user.id)
    return response


@app.route("/api/users/<id>/attempts", methods=["GET"])
@token_auth.login_required
def get_user_attempts(id):
    if g.current_user.id != id:
        abort(403)
    user = User.query.get(id)
    attempts = Attempt.query.filter_by(user_id=id)
    if user is None:
        return error_response(404, "User not found.")
    if attempts is None:
        return error_response(404, "User has not done any assessments.")
    data = {}
    for attempt in attempts:
        attempt_dict = attempt.to_dict()
        data[f"{attempt.attempt_id}"] = attempt_dict
    return jsonify(data)
