from tests.base_test import BaseTest
import allure
import pytest


@allure.epic("Users")
@allure.feature("Trial accounts")
@allure.story("New accounts")
class TestPostPage(BaseTest):
    @allure.title("Login and create post")
    @pytest.mark.parametrize("post_content", ["Hi mum", "Hello, colleagues"])
    def test_login_and_post_page(self, post_content):
        self.login_page.open()
        self.login_page.wait_for_page_to_load()
        self.login_page.click_login_button()

        self.home_page.add_post_text(post_content)
        self.home_page.click_post_button()

        assert self.home_page.is_post_published(post_content)

    @allure.title("Login and create empty post")
    def test_empty_post_error(self):
        self.login_page.open()
        self.login_page.wait_for_page_to_load()
        self.login_page.click_login_button()

        self.home_page.click_post_button()

        assert self.home_page.is_empty_post_error_shown()

        screenshot = self.home_page.driver.get_screenshot_as_png()
        allure.attach(screenshot, name="Chrome Screenshot", attachment_type=allure.attachment_type.PNG)
