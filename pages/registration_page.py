from pages.base_page import BasePage


class RegistrationPage(BasePage):

    _PAGE_URL = "https://demo.opensource-socialnetwork.org/"

    _FIRST_NAME_INPUT = ("xpath", "//input[@name='firstname']")
    _LAST_NAME_INPUT = ("xpath", "//input[@name='lastname']")
    _EMAIL_INPUT = ("xpath", "//input[@name='email']")
    _RE_ENTER_EMAIL_INPUT = ("xpath", "//input[@name='email_re']")
    _USERNAME_INPUT = ("xpath", "//input[@name='username']")
    _PASSWORD_INPUT = ("xpath", "//input[@name='password']")
    _BIRTHDATE_INPUT = ("xpath", "//input[@name='birthdate']")

    _GENDER_MALE_RBUTTON = ("xpath", "//input[@name='gender' and @value='male']")
    _GENDER_FEMALE_RBUTTON = ("xpath", "//input[@name='gender' and @value='female']")

    _TERMS_AND_CONDITIONS_CHECKBOX = ("xpath", "//input[@name='gdpr_agree']")
    _CREATE_ACCOUNT = ("xpath", "//input[@type='submit']")

    _SUCCESSFUL_REGISTRATION_LABEL = ("xpath", "//div[contains(text(), 'has been registered!')]")

    def enter_firstname(self):
        self.driver.find_element(*self._FIRST_NAME_INPUT).send_keys("John")

    def enter_lastname(self):
        self.driver.find_element(*self._LAST_NAME_INPUT).send_keys("Doe")

    def enter_email(self):
        self.driver.find_element(*self._EMAIL_INPUT).send_keys("example@mail.ru")

    def re_enter_email(self):
        self.driver.find_element(*self._RE_ENTER_EMAIL_INPUT).send_keys("example@mail.ru")

    def enter_username(self):
        self.driver.find_element(*self._USERNAME_INPUT).send_keys("username127")

    def enter_password(self):
        self.driver.find_element(*self._PASSWORD_INPUT).send_keys("123123123")

    def enter_birthdate(self):
        self.driver.find_element(*self._BIRTHDATE_INPUT).send_keys("04/03/2025")

    def choose_male_gender(self):
        self.driver.find_element(*self._GENDER_MALE_RBUTTON).click()

    def choose_female_gender(self):
        self.driver.find_element(*self._GENDER_FEMALE_RBUTTON).click()

    def agree_to_terms_and_conditions(self):
        self.driver.find_element(*self._TERMS_AND_CONDITIONS_CHECKBOX).click()

    def click_submit_button(self):
        self.driver.find_element(*self._CREATE_ACCOUNT).click()

    def is_registration_successful(self):
        return bool(self.driver.find_element(*self._SUCCESSFUL_REGISTRATION_LABEL))
