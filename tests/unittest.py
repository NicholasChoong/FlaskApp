import unittest, os
from app import app, db
from app.models import User, Log, Question, Attempt
from app.controllers import (
    UserController,
    LogController,
    AttemptController,
    ReviewController,
)


class ModelTest(unittest.TestCase):
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
            basedir, "test.db"
        )
        self.app = app.test_client()  # creates a virtual test environment
        db.create_all()
        s1 = User(id="OwO", surname="Case")
        s2 = User(id="wOw", first_name="Unit", surname="Test", isAdmin=True)

        t1 = Attempt(user_id="OwO", answer_1="potato", correct_1=True)
        t2 = Attempt(user_id="OwO", answer_1="potato", correct_1=True)
        t3 = Attempt(user_id="OwO", answer_1="potato", correct_1=True)

        q1 = Question(
            question="Who is Steve Jobs?", answer_type="SAQ", answer="Founder of Apple"
        )
        q2 = Question(
            question="Pick 1",
            answer_type="MCQ",
            answer_choice_1="1",
            answer_choice_2="2",
            answer_choice_3="3",
            answer_choice_4="4",
            answer="1",
        )

        db.session.add(s1)
        db.session.add(s2)
        db.session.add(t1)
        db.session.add(t2)
        db.session.add(t3)
        db.session.add(q1)
        db.session.add(q2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        s = User.query.get("OwO")
        s.set_password("test")
        self.assertFalse(s.check_password("case"))
        self.assertTrue(s.check_password("test"))

    def test_user_is_admin(self):
        s = User.query.get("OwO")
        self.assertFalse(s.isAdmin())
        s2 = User.query.get("wOw")
        self.assertTrue(s2.is_committed())

    def test_attempt(self):
        t = Attempt.query.all()
        self.assertEqual(t[0].attempt_id, 1, "Attempt_id should be 1")
        self.assertEqual(t.answer_1, "potato", "Asnwer_1 should be potato")
        self.assertTrue(t.correct_1)
        self.assertEqual(t.user_id.id, "OwO", "User_id should be OwO")
        self.assertEqual(t[1].attempt_id, 2, "Attempt_id should be 2")
        self.assertEqual(t[2].attempt_id, 3, "Attempt_id should be 3")

    def test_question(self):
        q = Question.query.all()
        self.assertEqual(q[0].question_id, 1, "Quesiton ID should be 1")
        self.assertEqual(q[0].question, "Who is Steve Jobs?")
        self.assertEqual(q[0].answer_type, "SAQ")
        self.assertEqual(q[0].answer, "Founder of Apple")
        self.assertEqual(q[1].question_id, 2, "question id should be 2")
        self.assertEqual(q[1].answer_type, "MCQ")
        self.assertEqual(q[1].answer_choice_1, "1", "Option should be 1")
        self.assertEqual(q[1].answer_choice_2, "2", "Option should be 2")
        self.assertEqual(q[1].answer_choice_3, "3", "Option should be 3")
        self.assertEqual(q[1].answer_choice_4, "4", "Option should be 4")
        self.assertEqual(q[1].answer_choice_4, "4", "Option should be 4")
        self.assertEqual(q[1].answer, "1", "Answer should be 1")


if __name__ == "__main__":
    unittest.main(verbosity=2)
