import allure
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@allure.epic("E-commerce Tests")
@allure.feature("Catalog Navigation")
@allure.story("Korean Cosmetics Category")
@allure.title("Переход в категорию 'Корея' через каталог")
def test_open_podrygka(driver_init):
    with allure.step("Шаг 1: Открытие главной страницы"):
        driver_init.get("https://www.podrygka.ru/")
        wait = WebDriverWait(driver_init, 10)

    with allure.step("Шаг 2: Закрытие всплывающего окна"):
        accept_button = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.button.button--default.button--default-round")))
        accept_button.click()

    with allure.step("Шаг 3: Открытие меню Каталога"):
        sleep(5)
        catalog_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.header-menu-catalog')))
        catalog_button.click()

    with allure.step("Шаг 4: Выбор категории 'Корея'"):
        category_for_Koreya = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a.relative.t3_s.flex-1.h-21.flex.justify-end.cursor-pointer')))
        category_for_Koreya.click()
