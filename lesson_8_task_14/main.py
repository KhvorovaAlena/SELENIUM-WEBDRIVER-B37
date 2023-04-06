import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import re


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


def any_window_other_than(old_windows):
    def expected_condition(driver):
        handles = driver.window_handles
        handles = list(set(handles)-set(old_windows))
        if len(handles) > 0:
            return handles[0]
        else:
            return False
    return expected_condition


def is_url(url):
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    return re.match(url_pattern, url)


def is_element_present(driver, locator):
    return len(driver.find_elements(By.XPATH, locator)) > 0


def test_windows_opening(driver):
    authorization(driver)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element(By.CSS_SELECTOR, ".button").click()
    table = driver.find_element(By.XPATH, "//*[@id='content']/form/table[1]")
    rows_list = table.find_elements(By.CSS_SELECTOR, "tr")
    rows_count = len(rows_list)

    main_window = driver.current_window_handle
    old_windows = driver.window_handles

    for link in range(rows_count):
        links_in_row = driver.find_elements(By.XPATH, "//*[@id='content']/form/table[1]/tbody/tr[{}]/td/a".format(link+1))
        count_links_in_row = len(links_in_row)
        for i in range(count_links_in_row):
            if not(is_element_present(driver, "//*[@id='content']/form/table[1]/tbody/tr[{}]/td/a[{}]".format(link + 1, i + 1))):
                continue

            url = table.find_element(By.XPATH, "//*[@id='content']/form/table[1]/tbody/tr[{}]/td/a[{}]".format(link + 1, i + 1))
            a = url.get_attribute("href")

            if not(is_url(a)):
                continue

            url.click()
            wait = WebDriverWait(driver, 10)
            new_window = wait.until(any_window_other_than(old_windows))
            driver.switch_to.window(new_window)
            driver.close()
            driver.switch_to.window(main_window)







    # main_window = driver.current_window_handle
    # old_windows = driver.window_handles
    # link.click()  # открывает новое окно
    # # ожидание появления нового окна,
    # # идентификатор которого отсутствует в списке oldWindows,
    # # остаётся в качестве самостоятельного упражнения
    # new_window = wait.until(there_is_window_other_than(old_windows))
    # driver.switch_to_window(new_window)
    # # ...
    # driver.close()
    # driver.switch_to_window(main_window)