import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

def are_elements_present(driver, *args):
    check = len(driver.find_elements(*args)) > 0
    if check:
        print("H1 tag was found")
    return check

def test_admin_cabinet(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.NAME, "login").click()

    count_links_in_menu = len(driver.find_elements(By.CSS_SELECTOR, "#box-apps-menu li"))

    for url in range(count_links_in_menu):
        link = (driver.find_element(By.CSS_SELECTOR, "#box-apps-menu li#app-:nth-child({})".format(url+1)))
        link.click()
        are_elements_present(driver, By.TAG_NAME, "h1")
        count_sub_link_in_menu = len(driver.find_elements(By.CSS_SELECTOR, ".docs li"))
        for sub_url in range(count_sub_link_in_menu):
                sub_link = (driver.find_element(By.CSS_SELECTOR, ".docs li:nth-child({})".format(sub_url + 1)))
                sub_link.click()
                are_elements_present(driver, By.TAG_NAME, "h1")
