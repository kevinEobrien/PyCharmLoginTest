from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.user_specific_url = "https://stportal.victorops.com/client/sdet"
        self.user_button_xpath = "//button[contains (. ,'keobrien')]"
        self.home_url="https://stportal.victorops.com/membership/#/"

    def user_button_is_displayed(self):
        user_button = self.driver.find_element(By.XPATH, self.user_button_xpath)
        if user_button.is_displayed():
            result = True
        else :
            result = False

        return result

    def wait_for_homepage_to_load (self):
        while self.driver.current_url == self.home_url:
            self.driver.implicitly_wait(1)
            if self.driver.current_url != self.home_url:
                break


