from app import app, db
from app.models import User, Log, Question, Attempt
from app.api.errors import bad_request, error_response
from flask import jsonify, url_for, request, g, abort
from app.api.auth import token_auth


@app.route("/api/quiz/", methods=["GET"])
@token_auth.login_required
def get_questions():
    questions = Question.query.all()
    if questions is None:
        return error_response(404, "There are no questions")
    data = {}
    for question in questions:
        question_dict = question.to_dict()
        data[f"{question.question_id}"] = question_dict
    return jsonify(data)