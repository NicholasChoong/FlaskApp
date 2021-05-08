from app import app, db
from app.models import User, Result, Log
from app.api.errors import bad_request, error_response
from flask import jsonify, url_for, request


@app.route("/api/results/", methods=["GET"])
def list_results():
    print("getting results")
    resultList = Result.query.all()
    results = []
    for result in resultList:
        # user_name = User.query.filter_by(user_id=result.user_id).first()
        results.append(
            {
                "result_id": result.result_id,
                "marks": result.marks,
                "correct_questions": result.correct_questions,
                "date": result.date,
                "user_id": result.user_id,
                "user_name": User.query.get(result.user_id).__str__(),
            }
        )
    results.sort(key=lambda x: x["result_id"])
    return jsonify({"resultList": results})