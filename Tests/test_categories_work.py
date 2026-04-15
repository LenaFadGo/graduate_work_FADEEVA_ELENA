import selenium
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_open_podrygka(driver_init):
    driver_init.get("https://www.podrygka.ru/")
    wait = WebDriverWait(driver_init, 10)

    accept_button = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a.button.button--default.button--default-round")))
    accept_button.click()

    sleep(10)
    catalog_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.header-menu-catalog')))
    catalog_button.click()

    carusel = driver_init.find_element(By.XPATH, "//ul[@class = 'w-max flex gap-2.5 md:gap-1.5 xl:gap-2']")
    category_for_men = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'a.relative.t3_s.flex-1.h-21.flex.justify-end.cursor-pointer')))
    category_for_men.click()
    pass