from app import app, db
from app.models import User, Log, Question, Attempt
from app.api.errors import bad_request, error_response
from flask import jsonify, url_for, request


@app.route("/api/attempts/", methods=["GET"])
def list_attempts():
    print("getting results")
    attempts = Attempt.query.all()
    if attempts is None:
        return error_response(404, "No one has attempted the quiz yet. :(")
    data = {}
    for attempt in attempts:
        attempt_dict = attempt.to_dict()
        data[f"{attempt.attempt_id}"] = attempt_dict
    return jsonify(data)