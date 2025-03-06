import time

from pages.registration_page import RegistrationPage


class TestRegistrationPage:

    def setup_method(self):
        self.registration_page = RegistrationPage(self.driver)

    def test_registration(self):
        self.registration_page.open()
        self.registration_page.enter_firstname()
        self.registration_page.enter_lastname()
        self.registration_page.enter_email()
        self.registration_page.re_enter_email()
        self.registration_page.enter_username()
        self.registration_page.enter_password()
        self.registration_page.enter_birthdate()
        self.registration_page.choose_male_gender()
        self.registration_page.agree_to_terms_and_conditions()
        self.registration_page.click_submit_button()
