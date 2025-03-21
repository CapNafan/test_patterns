from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data.links import Links

import allure


class LoginPage(BasePage):
    _PAGE_URL = Links.LOGIN

    _LOGIN = "//input[@value='Login']"

    def wait_for_page_to_load(self):
        (WebDriverWait(self.driver, timeout=10)
         .until(ec.element_to_be_clickable(self._LOGIN)))

    @allure.step("Enter login")
    def click_login_button(self):
        login_button = self.driver.find_element(*self._LOGIN)
        login_button.click()
