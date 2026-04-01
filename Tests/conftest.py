import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver_init():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()