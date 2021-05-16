import unittest, os, time
from app import app, db
from app.models import User, Attempt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


basedir = os.path.abspath(os.path.dirname(__file__))

# To do, find simple way for switching from test context to development to production.


class SystemTest(unittest.TestCase):
    driver = None

    def setUp(self):
        self.driver = webdriver.Firefox(
            executable_path=os.path.join(basedir, "geckodriver.exe")
        )
        if not self.driver:
            self.skipTest("Web browser not available")
        else:
            # db.init_app(app)
            # db.create_all()
            # db.session.commit()
            self.driver.maximize_window()
            self.driver.get("http://localhost:5000/")

    def tearDown(self):
        if self.driver:
            self.driver.close()
            User1 = User.query.get("potat")
            User2 = User.query.get("yes")
            db.session.delete(User1)
            db.session.delete(User2)
            db.session.commit()
            db.session.remove()

    def test_logintest(self):
        self.driver.get("http://127.0.0.1:5000/")
        assert self.driver.title == "PC Wiki"
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.CSS_SELECTOR, "#signup-form #floatingInput").click()
        self.driver.find_element(By.CSS_SELECTOR, "#signup-form #floatingInput").send_keys("potat")
        self.driver.find_element(By.ID, "signupPass1").click()
        self.driver.find_element(By.ID, "signupPass1").send_keys("yes")
        self.driver.find_element(By.ID, "signupPass2").click()
        self.driver.find_element(By.ID, "signupPass2").send_keys("yes")
        self.driver.find_element(By.ID, "signUpButton").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "floatingInput").click()
        self.driver.find_element(By.ID, "floatingInput").send_keys("potat")
        self.driver.find_element(By.ID, "floatingPassword").click()
        self.driver.find_element(By.ID, "floatingPassword").send_keys("yes")
        self.driver.find_element(By.NAME, "Remember Me").click()
        self.driver.find_element(By.NAME, "Sign In").click()
        self.driver.find_element(By.LINK_TEXT, "Learn").click()
        self.driver.find_element(By.LINK_TEXT, "Home").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.CSS_SELECTOR, "#signup-form #floatingInput").click()
        self.driver.find_element(By.CSS_SELECTOR, "#signup-form #floatingInput").send_keys("potat")
        self.driver.find_element(By.ID, "signupPass1").click()
        self.driver.find_element(By.ID, "signupPass1").send_keys("yes")
        self.driver.find_element(By.ID, "signupPass2").click()
        self.driver.find_element(By.ID, "signupPass2").send_keys("yes")
        self.driver.find_element(By.ID, "signUpButton").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, "ul:nth-child(3) > li")
        assert len(elements) > 0
    
    def test_quizTest(self):
        self.driver.get("http://127.0.0.1:5000/")
        assert self.driver.title == "PC Wiki"
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.CSS_SELECTOR, "#signup-form #floatingInput").click()
        self.driver.find_element(By.CSS_SELECTOR, "#signup-form #floatingInput").send_keys("yes")
        self.driver.find_element(By.ID, "signupPass1").click()
        self.driver.find_element(By.ID, "signupPass1").send_keys("yes")
        self.driver.find_element(By.ID, "signupPass2").click()
        self.driver.find_element(By.ID, "signupPass2").send_keys("yes")
        self.driver.find_element(By.ID, "signUpButton").click()
        self.driver.find_element(By.CSS_SELECTOR, ".p-3").click()
        self.driver.find_element(By.LINK_TEXT, "Quiz").click()
        self.driver.find_element(By.ID, "question_1-0").click()
        self.driver.find_element(By.ID, "question_2-1").click()
        self.driver.find_element(By.ID, "question_3-2").click()
        self.driver.find_element(By.ID, "question_4-3").click()
        self.driver.find_element(By.ID, "question_5-0").click()
        self.driver.find_element(By.ID, "question_6-0").click()
        self.driver.find_element(By.NAME, "question_7").click()
        self.driver.find_element(By.NAME, "question_7").send_keys("7")
        self.driver.find_element(By.ID, "quiz-submission").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".accordion-button")
        assert len(elements) > 0
        self.driver.find_element(By.CSS_SELECTOR, ".accordion-button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".accordion-button").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        elements = self.driver.find_elements(By.LINK_TEXT, "Login")
        assert len(elements) > 0

if __name__ == "__main__":
    unittest.main(verbosity=2)
