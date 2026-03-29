from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

def test_open_podrygka():
    driver.get("https://www.podrygka.ru/")
    accept_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Подарочные карты']")))
    accept_button.click()