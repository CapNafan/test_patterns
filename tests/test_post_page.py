from tests.base_test import BaseTest
import pytest


class TestPostPage(BaseTest):
    @pytest.mark.parametrize("post_content", ["Hi mum", "Hello, colleagues"])
    def test_login_and_post_page(self, post_content):
        self.login_page.open()
        self.login_page.wait_for_page_to_load()
        self.login_page.click_login_button()

        self.home_page.add_post_text(post_content)
        self.home_page.click_post_button()

        assert self.home_page.is_post_published(post_content)

    def test_empty_post_error(self):
        self.login_page.open()
        self.login_page.wait_for_page_to_load()
        self.login_page.click_login_button()

        self.home_page.click_post_button()

        assert self.home_page.is_empty_post_error_shown()
