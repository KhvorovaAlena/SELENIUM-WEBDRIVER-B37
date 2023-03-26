import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


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


def zone_sorting(driver, row):
    zones = list()
    (driver.find_element(By.XPATH, "//*[@id='content']/form/table/tbody/tr[{}]/td[3]/a".format(row + 2))).click()
    zones_table = driver.find_element(By.XPATH, "//*[@id='table-zones']")
    all_zones = len(zones_table.find_elements(By.CSS_SELECTOR, "tr"))
    for row in range(all_zones - 2):
        zone = (driver.find_element(By.XPATH,
                                    "//*[@id='table-zones']/tbody/tr[{}]/td[3]/select/option[@selected = 'selected']".format(
                                        row + 2))).get_attribute(
            "text")
        zones.append(zone)

    sorted_zones_list = sorted(zones)
    if zones == sorted_zones_list:
        print("\nZones list sorting is correct")
    else:
        print("\nThe zones list is not sorted")
    print(zones)


def test_countries_sorting_checking(driver):
    authorization(driver)

    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    geo_zones_table = driver.find_element(By.CSS_SELECTOR, ".dataTable")
    all_geo_zones = len(geo_zones_table.find_elements(By.CSS_SELECTOR, "tr.row"))

    for row in range(all_geo_zones):
        zone_sorting(driver, row)
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
