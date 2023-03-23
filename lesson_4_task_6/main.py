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

    links_in_menu = driver.find_elements(By.CSS_SELECTOR, "#box-apps-menu a")
    page_urls = [element.get_attribute('href') for element in links_in_menu]

    for url in page_urls:
        driver.get(url)
        are_elements_present(driver, By.TAG_NAME, "h1")
        sub_link_in_menu = driver.find_elements(By.CSS_SELECTOR, ".docs a")
        sub_link_urls = [link.get_attribute('href') for link in sub_link_in_menu]
        for sub_url in sub_link_urls:
            if url != sub_url:
                driver.get(sub_url)
                are_elements_present(driver, By.TAG_NAME, "h1")