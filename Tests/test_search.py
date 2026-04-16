import allure
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



@allure.epic("E-commerce Tests")
@allure.feature("Search")
@allure.story("Product Search")
@allure.title("Поиск товара 'essence' на podrygka.ru")
def test_open_podrygka(driver_init):
    with allure.step("Шаг 1: Открытие главной страницы сайта"):
        driver_init.get("https://www.podrygka.ru/")
        wait = WebDriverWait(driver_init, 10)

    with allure.step("Шаг 2: Закрытие всплывающего окна (Cookies/Promo)"):
        try:
            btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button.button--default.button--default-round")))
            btn.click()
        except:
            pass

    with allure.step("Шаг 3: Клик по полю поиска"):
        sleep(2) # небольшая пауза для стабильности
        search_field = wait.until(EC.element_to_be_clickable((By.ID, "search")))
        search_field.click()

    with allure.step("Шаг 4: Ввод запроса 'essence'"):
        search_field.send_keys("essence")

    with allure.step("Шаг 5: Нажатие кнопки поиска"):
        btn_find = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.digi-ac-find__button')))
        btn_find.click()


