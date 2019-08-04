import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium.webdriver import Chrome
import pytest
from PyTest.Pages.loginPage import LoginPage
from PyTest.Pages.homePage import HomePage
from PyTest.environ_vars import EnvironmentVariables
import pytest_html


@pytest.fixture()
def environment_setup():
    env_variables = EnvironmentVariables()
    global victorops_username
    victorops_username = env_variables.victorops_username
    global victorops_password
    victorops_password = env_variables.victorops_password
    global baseurl
    baseurl= env_variables.baseurl
    global driver
    path = "/usr/local/bin/chromedriver"
    driver = Chrome(executable_path=path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Successfully completed test")

def test_valid_login(environment_setup):
    print(os.environ)
    home_url = baseurl + "membership/#/"
    driver.get(home_url)
    login = LoginPage(driver)
    login.enter_username(victorops_username)
    login.enter_password(victorops_password)
    login.click_sign_in()
    homepage = HomePage(driver)
    homepage.wait_for_homepage_to_load()
    assert homepage.user_specific_url == driver.current_url
    assert homepage.user_button_is_displayed() == True

if __name__ == '__main__':
    pytest.main(pytest_html)


