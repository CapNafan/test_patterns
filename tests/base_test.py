from pages.login_page import LoginPage
from pages.home_page import HomePage


class BaseTest:

    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)