import allure

from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    _PAGE_URL = "https://demo.opensource-socialnetwork.org/home"

    _POST_BODY = "//textarea[@name='post']"
    _POST_BUTTON = "//input[@type='submit']"
    _PUBLISHED_POST_TEXT = "//div//p[contains(text(), '{value}')]"
    _ERROR_MESSAGE = "//div[contains(text(), 'Cannot create post! Please try again later.')]"

    @allure.step("Add text to post editor")
    def add_post_text(self, text):
        post_body_input = self.driver.find_element(*self._POST_BODY)
        post_body_input.send_keys(text)

    @allure.step("Click post button")
    def click_post_button(self):
        post_button = self.driver.find_element(*self._POST_BUTTON)
        post_button.click()

    def _wait_for_post_to_appear(self, text):
        locator = (By.XPATH, self._PUBLISHED_POST_TEXT[1].format(value=text))
        return WebDriverWait(self.driver, timeout=10).until(ec.presence_of_element_located(locator))

    @allure.step("Check that post is published")
    def is_post_published(self, text):
        published_text = self._wait_for_post_to_appear(text)
        return published_text.text == text

    @allure.step("Check for error message after empty post creation attempt")
    def is_empty_post_error_shown(self):
        error_message = WebDriverWait(self.driver, timeout=10).until(ec.presence_of_element_located(self._ERROR_MESSAGE))
        return error_message.is_displayed()


