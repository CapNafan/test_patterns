from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):
    _PAGE_URL = "https://demo.opensource-socialnetwork.org/login"

    _LOGIN = "//input[@value='Login']"

    def wait_for_page_to_load(self):
        (WebDriverWait(self.driver, timeout=10)
         .until(ec.presence_of_element_located(self._LOGIN)))

    def click_login_button(self):
        login_button = self.driver.find_element(*self._LOGIN)
        login_button.click()
