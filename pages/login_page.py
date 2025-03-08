from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):
    _PAGE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    _USERNAME_INPUT = ("xpath", "//input[@name='username']")
    _PASSWORD_INPUT = ("xpath", "//input[@name='password']")
    _SUBMIT = ("xpath", "//button[@type='submit']")

    def wait_for_page_to_load(self):
        (WebDriverWait(self.driver, timeout=10)
         .until(ec.presence_of_element_located(self._SUBMIT)))

    def enter_login(self, login):
        login_field = self.driver.find_element(*self._USERNAME_INPUT)
        login_field.send_keys(login)

    def enter_password(self, password):
        login_field = self.driver.find_element(*self._PASSWORD_INPUT)
        login_field.send_keys(password)

    def click_submit_button(self):
        submit_button = self.driver.find_element(*self._SUBMIT)
        submit_button.click()
