from selenium import webdriver
import unittest

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def login_test_valid(self):
        self.driver.get("https://stportal.victorops.com/membership/#/")
        self.driver.find_element_by_id("username").send_keys("keobrien")
        self.driver.find_element_by_id("password").send_keys("P@ssw0rd2")
        self.driver.find_element_by_id("ext--login-submit").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


