from selenium import webdriver
import pytest
import os


@pytest.fixture(autouse=True)
def driver(request):
    browser = os.environ["BROWSER"]

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    request.cls.driver = driver

    yield

    driver.quit()
