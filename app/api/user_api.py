from app import app, db
from app.models import User, Result, Log
from app.api.errors import bad_request, error_response
from flask import jsonify, url_for, request, g, abort
from app.api.auth import token_auth


@app.route("/api/users/<user_id>", methods=["GET"])
@token_auth.login_required
def get_user(user_id):
    print(g.current_user)
    if g.current_user.id != user_id:
        abort(403)
    return jsonify(User.query.get_or_404(user_id).to_dict())


@app.route("/api/users", methods=["POST"])
def register_user():
    data = request.get_json() or {}
    if "user_id" not in data or "password_hash" not in data:
        return bad_request("Must include username and password")
    user = User.query.get(data["user_id"])
    if user is None:
        return bad_request("Unknown user")
    if user.password_hash is not None:
        return bad_request("User already registered")
    user.from_dict(data)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201  # creating a new resource should chare the location....
    response.headers["Location"] = url_for("get_user", id=user.user_id)
    return response


@app.route("/api/users/<user_id>", methods=["PUT"])
@token_auth.login_required
def update_user(user_id):
    if g.current_user.id != user_id:
        abort(403)
    data = request.get_json() or {}
    user = User.query.get(user_id)
    if user is None:
        return bad_request("Unknown user")
    if user.password_hash is None:
        return bad_request("User not registered")
    user.from_dict(data)
    db.session.commit()
    return jsonify(user.to_dict())


@app.route("/api/users/<user_id>/results", methods=["GET"])
@token_auth.login_required
def get_user_results(user_id):
    if g.current_user.id != user_id:
        abort(403)
    user = User.query.get(user_id)
    results = Result.query.filter_by(user_id=user_id)
    if user is None:
        return error_response(404, "User not found.")
    if results is None:
        return error_response(404, "User has not done any assessments.")
    # User.query.filter_by(user_id=log.user_id).first()
    data = {}
    for result in results:
        result_dict = result.to_dict()
        result_dict["user_name"] = User.query.get(result.user_id).__str__()
        data[f"{result.result_id}"] = result_dict
    return jsonify(data)


number_of_questions = 10


@app.route("/api/users/<user_id>/results", methods=["POST"])
@token_auth.login_required
def new_result(user_id):
    if g.current_user.id != user_id:
        abort(403)
    data = request.get_json() or {}
    if "marks" not in data or "result_id" not in data:
        return bad_request("Must include marks and result_id")
    user = User.query.get(user_id)
    if user is None:
        return bad_request("Unknown user, or wrong id")
    result = Result()
    result.marks = -1
    result.correct_questions = "0" * number_of_questions
    db.session.add(result)
    db.session.flush()  # generates pk for new project
    db.session.commit()
    response = jsonify(result.to_dict())
    response.status_code = 201  # creating a new resource should chare the location....
    response.headers["Location"] = url_for("new_user_results", id=user.id)
    return response


@app.route("/api/users/<user_id>/results", methods=["PUT"])
@token_auth.login_required
def update_user_result(user_id):
    if g.current_user.id != user_id:
        abort(403)
    print(request.data)
    data = request.get_json() or {}
    print(data)
    if "marks" not in data or "result_id" not in data:
        return bad_request("Must include marks and result_id")
    user = User.query.get(user_id)
    if user is None:
        return bad_request("Unknown user, or wrong id")
    result = Result.query.filter_by(user_id=user_id)[-1]
    result.marks = data["marks"]
    result.correct_questions = data["correct_questions"]
    db.session.commit()
    return jsonify(result.to_dict())


@app.route("/api/users/<user_id>/results", methods=["DELETE"])
@token_auth.login_required
def delete_user_results(user_id):
    if g.current_user.id != user_id:
        abort(403)
    user = User.query.get(user_id)
    if user is None:
        return bad_request("Unknown user, or wrong id")
    result = Result.query.filter_by(user_id=user_id)
    if result is None:
        return bad_request("Result not found")
    db.session.delete(result)
    db.session.commit()
    return jsonify(result.to_dict())
