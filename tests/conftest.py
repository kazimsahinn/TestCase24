from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setUp(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()