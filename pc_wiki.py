from app import app, db
from app.models import User, Log, Question, Attempt


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Log": Log, "Question": Question, "Attempt": Attempt}
