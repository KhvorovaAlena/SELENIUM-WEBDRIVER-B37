import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


def is_element_present(driver, locator):
    return len(driver.find_elements(By.CSS_SELECTOR, locator)) > 0


def add_duck_to_cart(driver):
    driver.find_element(By.CSS_SELECTOR, "#box-most-popular li").click()

    if is_element_present(driver, "[name='options[Size]']"):
        driver.find_element(By.CSS_SELECTOR, "[name='options[Size]']").click()
        driver.find_element(By.CSS_SELECTOR, "[value='Small']").click()

    row_counter = driver.find_element(By.CSS_SELECTOR, ".quantity").get_attribute("textContent")
    counter = int(row_counter)
    row_quantity = driver.find_element(By.CSS_SELECTOR, "[name='quantity']").get_attribute("value")
    quantity = int(row_quantity)
    expected_items_count = str(counter+quantity)

    driver.find_element(By.CSS_SELECTOR, "[name='add_cart_product']").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, ".quantity"), "textContent", expected_items_count))
    driver.get("http://localhost/litecart/en/")


def remove_duck_from_bucket(driver):
    driver.find_element(By.CSS_SELECTOR, ".content").click()
    ducks = driver.find_elements(By.CSS_SELECTOR, ".shortcuts li")
    ducks_count = len(ducks)
    for i in range(ducks_count):
        table = driver.find_element(By.CSS_SELECTOR, ".dataTable")

        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[name='remove_cart_item']")))
        driver.find_element(By.CSS_SELECTOR, "[name='remove_cart_item']").click()
        wait.until(
            EC.staleness_of(table)
        )


def test_cart_work(driver):
    driver.get("http://localhost/litecart/en/")
    for i in range(3):
        add_duck_to_cart(driver)
    remove_duck_from_bucket(driver)
