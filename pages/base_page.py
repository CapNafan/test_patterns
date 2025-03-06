from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    ABOUT_LINK = ("xpath", "//a[@class='menu-footer-about']")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        self.driver.get(self.PAGE_URL)
