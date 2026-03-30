from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_open_podrygka(driver_init):
    driver_init.get("https://www.podrygka.ru/")
    wait = WebDriverWait(driver_init, 15)

    accept_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.button.button--default.button--default-round")))
    accept_button.click()

    sleep(2)
    search = wait.until(EC.element_to_be_clickable((By.ID, "search")))
    search.click()
    search.send_keys("essence")
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.digi-ac-find__button')))
    button.click()