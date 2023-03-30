import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


def authorization(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element(By.CSS_SELECTOR, "[name = username]").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "[name = password]").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "[name = login]").click()


def get_file_path():
    absolute_path = os.path.dirname(__file__)
    relative_path = "duck.jpg"
    full_path = os.path.join(absolute_path, relative_path)
    return full_path


def general_tab_filling(driver, test_duck_name):
    driver.find_element(By.CSS_SELECTOR, "[value='1']").click()
    driver.find_element(By.CSS_SELECTOR, "[name='name[en]']").send_keys(test_duck_name)
    driver.find_element(By.CSS_SELECTOR, "[name='code']").send_keys("1222")
    root_checkbox = driver.find_element(By.CSS_SELECTOR, "[type='checkbox'][data-name='Root']")
    if root_checkbox.is_selected():
        root_checkbox.click()
    driver.find_element(By.CSS_SELECTOR, "[type='checkbox'][data-name='Rubber Ducks']").click()
    driver.find_element(By.CSS_SELECTOR, "[name='default_category_id']").click()
    driver.find_element(By.CSS_SELECTOR, "option[value='1']").click()
    driver.find_element(By.CSS_SELECTOR, "[type='checkbox'][value='1-2']").click()
    quantity_field = driver.find_element(By.CSS_SELECTOR, "[name='quantity']")
    quantity_field.clear()
    quantity_field.send_keys("10")
    driver.find_element(By.CSS_SELECTOR, "[name='new_images[]']").send_keys(get_file_path())
    driver.find_element(By.CSS_SELECTOR, "[name='date_valid_from']").send_keys("10102022")
    driver.find_element(By.CSS_SELECTOR, "[name='date_valid_to']").send_keys("10102024")


def information_tab_filling(driver):
    driver.find_element(By.CSS_SELECTOR, "[href='#tab-information']").click()
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, "[name='manufacturer_id']").click()
    driver.find_element(By.XPATH, "//*[@id='tab-information']/table/tbody/tr[1]/td/select/option[2]").click()
    driver.find_element(By.CSS_SELECTOR, "[name='keywords']").send_keys("Duck, Spider")
    driver.find_element(By.CSS_SELECTOR, "[name='short_description[en]']").send_keys("Test duck")
    driver.find_element(By.CSS_SELECTOR, ".trumbowyg-editor").send_keys("Test duck full description")
    driver.find_element(By.CSS_SELECTOR, "[name='head_title[en]']").send_keys("Test duck head title")
    driver.find_element(By.CSS_SELECTOR, "[name='meta_description[en]']").send_keys("Test duck meta description")


def prices_tab_filling(driver):
    driver.find_element(By.CSS_SELECTOR, "[href='#tab-prices']").click()
    driver.implicitly_wait(10)
    price_field = driver.find_element(By.CSS_SELECTOR, "[name='purchase_price']")
    price_field.clear()
    price_field.send_keys("100")
    driver.find_element(By.CSS_SELECTOR, "[name='purchase_price_currency_code']").click()
    driver.find_element(By.CSS_SELECTOR, "[value='USD']").click()
    driver.find_element(By.CSS_SELECTOR, "[name='prices[USD]']").send_keys("150")
    driver.find_element(By.CSS_SELECTOR, "[name='prices[EUR]']").send_keys("160")


def created_duck_checking(driver, test_duck_name):
    ducks_table = driver.find_element(By.CSS_SELECTOR, ".dataTable")
    rows = len(ducks_table.find_elements(By.CSS_SELECTOR, "tr"))
    for row in range(rows-5):
        duck_name = ducks_table.find_element(By.XPATH, "//*[@id='content']/form/table/tbody/tr[{}]/td[3]/a".format(row+5)).get_attribute("textContent")
        print(duck_name)
        if duck_name == test_duck_name:
            print("Created duck", test_duck_name, "is present")


def test_duck_creation(driver):
    test_duck_name = "Spider duck"
    authorization(driver)
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    driver.find_element(By.XPATH, "//*[@id='content']/div[1]/a[2]").click()
    general_tab_filling(driver, test_duck_name)
    information_tab_filling(driver)
    prices_tab_filling(driver)
    driver.find_element(By.CSS_SELECTOR, "[name='save']").click()
    created_duck_checking(driver, test_duck_name)
