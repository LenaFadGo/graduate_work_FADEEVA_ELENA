import allure
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_open_podrygka(driver_init):
    with allure.step("Шаг 1: Открытие главной страницы сайта"):
        driver_init.get("https://www.podrygka.ru/")
        wait = WebDriverWait(driver_init, 10)

    with allure.step("Шаг 2: Закрытие всплывающего окна (Cookies/Promo)"):
        accept_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.button.button--default.button--default-round")))
        accept_button.click()

    with allure.step("Шаг 3: Клик по полю поиска"):
        sleep(2) # небольшая пауза для стабильности
        search = wait.until(EC.element_to_be_clickable((By.ID, "search")))
        search.click()

    with allure.step("Шаг 4: Ввод запроса 'essence'"):
        search.send_keys("essence")

    with allure.step("Шаг 5: Нажатие кнопки поиска"):
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.digi-ac-find__button')))
        button.click()
    pass

    