import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium.webdriver import Chrome
import pytest
from PyTest.Pages.loginPage import LoginPage
from PyTest.Pages.homePage import HomePage
import pytest_html


@pytest.fixture()
def environment_setup():
    username = "VICTOROPS_USERNAME"
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
    home_url = "https://stportal.victorops.com/membership/#/"
    driver.get(home_url)
    login = LoginPage(driver)
    login.enter_username("keobrien")
    login.enter_password("P@ssw0rd1000")
    login.click_sign_in()
    homepage = HomePage(driver)
    homepage.wait_for_homepage_to_load()
    assert homepage.user_specific_url == driver.current_url
    assert homepage.user_button_is_displayed()

if __name__ == '__main__':
    pytest.main(pytest_html)


