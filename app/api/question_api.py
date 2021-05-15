from app import app, db
from app.models import User, Log, Question, Attempt
from app.api.errors import bad_request, error_response
from flask import jsonify, url_for, request, g, abort
from app.api.auth import token_auth

@app.route("/api/user/<id>/attempt/", methods=["POST"])
@token_auth.login_required
def new_attempts():
    pass