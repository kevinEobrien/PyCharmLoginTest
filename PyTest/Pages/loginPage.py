class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_input_id = "username"
        self.password_input_id = "password"
        self.sign_in_button_id = "ext--login-submit"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_input_id).clear()
        self.driver.find_element_by_id(self.username_input_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_input_id).clear()
        self.driver.find_element_by_id(self.password_input_id).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element_by_id(self.sign_in_button_id).click()