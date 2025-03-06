from pages.base_page import BasePage


class RegistrationPage(BasePage):

    PAGE_URL = "https://demo.opensource-socialnetwork.org/"

    FIRST_NAME_INPUT = ("xpath", "//input[@name='firstname']")
    LAST_NAME_INPUT = ("xpath", "//input[@name='lastname']")
    EMAIL_INPUT = ("xpath", "//input[@name='email']")
    RE_ENTER_EMAIL_INPUT = ("xpath", "//input[@name='email_re']")
    USERNAME_INPUT = ("xpath", "//input[@name='username']")
    PASSWORD_INPUT = ("xpath", "//input[@name='password']")
    BIRTHDATE_INPUT = ("xpath", "//input[@name='birthdate']")

    GENDER_MALE_RBUTTON = ("xpath", "//input[@name='gender' and @value='male']")
    GENDER_FEMALE_RBUTTON = ("xpath", "//input[@name='gender' and @value='female']")

    TERMS_AND_CONDITIONS_CHECKBOX = ("xpath", "//input[@name='gdpr_agree']")
    CREATE_ACCOUNT = ("xpath", "//input[@type='submit']")

    SUCCESSFUL_REGISTRATION_LABEL = ("xpath", "//div[contains(text(), 'has been registered!')]")

    def enter_firstname(self):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys("John")

    def enter_lastname(self):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys("Doe")

    def enter_email(self):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys("example@mail.ru")

    def re_enter_email(self):
        self.driver.find_element(*self.RE_ENTER_EMAIL_INPUT).send_keys("example@mail.ru")

    def enter_username(self):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys("username127")

    def enter_password(self):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys("123123123")

    def enter_birthdate(self):
        self.driver.find_element(*self.BIRTHDATE_INPUT).send_keys("04/03/2025")

    def choose_male_gender(self):
        self.driver.find_element(*self.GENDER_MALE_RBUTTON).click()

    def choose_female_gender(self):
        self.driver.find_element(*self.GENDER_FEMALE_RBUTTON).click()

    def agree_to_terms_and_conditions(self):
        self.driver.find_element(*self.TERMS_AND_CONDITIONS_CHECKBOX).click()

    def click_submit_button(self):
        self.driver.find_element(*self.CREATE_ACCOUNT).click()

    def is_registration_successful(self):
        return bool(self.driver.find_element(*self.SUCCESSFUL_REGISTRATION_LABEL))
