from selenium import webdriver
import unittest
from PyTest.Pages.loginPage import LoginPage
from PyTest.Pages.homePage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver

        driver.get("https://stportal.victorops.com/membership/#/")

        login = LoginPage(driver)
        login.enter_username("keobrien")
        login.enter_password("P@ssw0rd2")
        login.click_sign_in()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Successfully completed test")

if __name__ == '__main__':
    unittest.main()


