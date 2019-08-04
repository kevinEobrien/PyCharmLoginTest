from selenium.webdriver.common.by import By
from PyTest.environ_vars import EnvironmentVariables

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        env_variables = EnvironmentVariables()
        self.username_domain = env_variables.vicortops_user_domain
        self.user_button_xpath = "//button[contains (. ," + env_variables.victorops_username + ")]"
        self.user_specific_url = env_variables.baseurl + "client/" + self.username_domain
        self.home_url = env_variables.baseurl + "membership/#/"
        self.homepage_title = "Timeline - " + self.username_domain.upper()

    def user_button_is_displayed(self):
        user_button = self.driver.find_element(By.XPATH, self.user_button_xpath)
        if user_button.is_displayed():
            result = True
        else:
            result = False

        return result

    def wait_for_homepage_to_load (self):
        while self.driver.current_url == self.home_url:
            self.driver.implicitly_wait(1)
            if self.driver.current_url != self.home_url:
                break
