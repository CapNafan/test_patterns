from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class DashboardPage(BasePage):

    _PAGE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    _HELP_SIGN = "xpath", "//button[@title='Help']"

    def wait_for_page_to_load(self):
        (WebDriverWait(self.driver, timeout=10)
         .until(ec.presence_of_element_located(self._HELP_SIGN)))

    def click_help(self):
        help_button = self.driver.find_element(*self._HELP_SIGN)
        help_button.click()
