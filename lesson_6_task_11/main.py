import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
import random
import string


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


def random_char(char_num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(char_num))


def test_registration(driver):
    test_mail = random_char(7) + "@testmail.com"
    password = random_char(7)
    print(test_mail, password)

    driver.get("http://localhost/litecart/en/")
    driver.find_element(By.XPATH, "//*[@id='box-account-login']/div/form/table/tbody/tr[5]/td/a").click()

    driver.find_element(By.CSS_SELECTOR, "[name='tax_id']").send_keys("12443")
    driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("Test company")
    driver.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("Test")
    driver.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("User")
    driver.find_element(By.CSS_SELECTOR, "[name='address1']").send_keys("Test address")
    driver.find_element(By.CSS_SELECTOR, "[name='address2']").send_keys("Test address 2")
    driver.find_element(By.CSS_SELECTOR, "[name='postcode']").send_keys("12456")
    driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("New York")
    driver.find_element(By.XPATH, "//*[@id='create-account']/div/form/table/tbody/tr[5]/td[1]/span[2]").click()
    driver.find_element(By.CSS_SELECTOR, ".select2-search__field").send_keys("United States", Keys.ENTER)
    driver.find_element(By.CSS_SELECTOR, "[name='email']").send_keys(test_mail)
    driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+14845219649")
    driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "[name='confirmed_password']").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "[name='create_account']").click()

    driver.find_element(By.XPATH, "//*[@id='box-account']/div/ul/li[4]/a").click()
    driver.find_element(By.CSS_SELECTOR, "[name='email']").send_keys(test_mail)
    driver.find_element(By.CSS_SELECTOR, "[name='password']").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "[name='login']").click()
    driver.find_element(By.XPATH, "//*[@id='box-account']/div/ul/li[4]/a").click()










