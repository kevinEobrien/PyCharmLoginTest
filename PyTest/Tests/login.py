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
        home_url= "https://stportal.victorops.com/membership/#/"
        driver.get(home_url)

        login = LoginPage(driver)
        login.enter_username("keobrien")
        login.enter_password("P@ssw0rd22")
        login.click_sign_in()

        homepage = HomePage(driver)
        while driver.current_url == home_url:
            driver.implicitly_wait(1)
            if driver.current_url != home_url:
                break
        self.assertEqual(homepage.user_specific_url, driver.current_url)
        self.assertEqual(homepage.user_button_is_displayed(), True)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Successfully completed test")

if __name__ == '__main__':
    unittest.main()


