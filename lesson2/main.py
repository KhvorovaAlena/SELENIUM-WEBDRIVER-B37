import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


def test_admin_authorization(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.NAME, "login").click()

