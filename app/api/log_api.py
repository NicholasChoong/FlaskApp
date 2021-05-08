from app import app, db
from app.models import User, Result, Log
from app.api.errors import bad_request, error_response
from flask import jsonify, url_for, request


@app.route("/api/logs/", methods=["GET"])
def list_logs():
    print("getting logs")
    logList = Log.query.all()
    logs = []
    for log in logList:
        # user_name = User.query.filter_by(user_id=log.user_id).first()
        logs.append(
            {
                "log_id": log.log_id,
                "login_key": log.login_key,
                "date": log.date,
                "user_id": log.user_id,
                "user_name": User.query.get(log.user_id).__str__(),
            }
        )
    logs.sort(key=lambda x: x["log_id"])
    return jsonify({"logList": logs})