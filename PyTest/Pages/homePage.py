from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.user_specific_url = "https://stportal.victorops.com/client/sdet"
        self.user_button_xpath = "//button[contains (. ,'keobrien')]"

    def user_button_is_displayed(self):
        user_button = self.driver.find_element(By.XPATH, self.user_button_xpath)
        if user_button.is_displayed():
            result = True
        else :
            result = False

        return result



