import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture
def driver(request):
    capability = DesiredCapabilities.CHROME
    capability['goog:loggingPrefs'] = {'browser': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities=capability)
    request.addfinalizer(driver.quit)
    return driver


def authorization(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element(By.CSS_SELECTOR, "[name = username]").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "[name = password]").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "[name = login]").click()


def check_page_logs(driver, all_rows_count):
    for row in range(all_rows_count - 3):
        logs = []
        table = driver.find_element(By.CSS_SELECTOR, ".dataTable")
        duck = table.find_element(By.XPATH, "//*[@id='content']/form/table/tbody/tr[{}]/td[3]/a".format(row + 5))
        duck.click()
        for entry in driver.get_log('browser'):
            print("\n", entry)
            logs.append(entry)
        if len(logs) > 0:
            url = driver.current_url
            print("\nThe page", url, "has logs")
        logs.clear()
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")


def test_check_logs(driver):
    authorization(driver)
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    table = driver.find_element(By.CSS_SELECTOR, ".dataTable")
    all_rows = table.find_elements(By.CSS_SELECTOR, "tr.row")
    all_rows_count = len(all_rows)

    check_page_logs(driver, all_rows_count)
