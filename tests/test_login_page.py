from tests.base_test import BaseTest


class TestLoginPage(BaseTest):
    def test_login(self):
        self.login_page.open()
        self.login_page.wait_for_page_to_load()
        self.login_page.enter_login("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_submit_button()

        self.dashboard_page.wait_for_page_to_load()
        self.dashboard_page.click_help()

