from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
def test_check_essence_on_page():
    try:
        driver.get("https://www.podrygka.ru/")
        try:
            close_button = driver.find_element(By.CSS_SELECTOR, ".modal-close, .popup-close, button.close")
            if close_button.is_displayed():
                close_button.click()
        except():
            pass
        try:
            search_locator = (By.CSS_SELECTOR, "input[name='q'], input.placeholder-search, input.search-input")
            search_input = wait.until(EC.visibility_of_element_located(search_locator))
            search_input.send_keys("essence")
        except NoSuchElementException:
            print("Поиск отсутствует")

        search_button = driver.find_element(
            By.XPATH,"//button[.//svg] | //button[contains(@class, 'search')] | //input[@name='q']/following-sibling::button")
        search_button.click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'product')]")))
        print("Успешно")

    finally:
        driver.quit()