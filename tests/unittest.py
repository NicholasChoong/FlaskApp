import unittest, os
from app import app, db
from app.models import User


class userModelTest(unittest.TestCase):
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
            basedir, "test.db"
        )
        self.app = app.test_client()  # creates a virtual test environment
        db.create_all()
        s1 = User(id="OwO", first_name="Test", surname="Case")
        s2 = User(id="wOw", first_name="Unit", surname="Test")
        db.session.add(s1)
        db.session.add(s2)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        s = User.query.get("OwO")
        s.set_password("test")
        self.assertFalse(s.check_password("case"))
        self.assertTrue(s.check_password("test"))

    def test_is_committed(self):
        s = User.query.get("OwO")
        self.assertFalse(s.is_committed())
        s2 = User.query.get("wOw")
        self.assertTrue(s.is_committed())


if __name__ == "__main__":
    unittest.main(verbosity=2)
