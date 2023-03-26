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


def zone_sorting(driver, countries_with_zones):
    for zone in range(len(countries_with_zones)):
        link = countries_with_zones[zone]
        driver.get(link)

        table = driver.find_element(By.XPATH, "//*[@id='table-zones']/tbody")
        all_zones = len(table.find_elements(By.CSS_SELECTOR, "tr"))
        zones = list()

        for row in range(all_zones-2):
            zone_name = (driver.find_element(By.XPATH, "//*[@id='table-zones']/tbody/tr[{}]/td[3]/input".format(row + 2))).get_attribute("value")
            zones.append(zone_name)

        sorted_zones_list = sorted(zones)
        if zones == sorted_zones_list:
            print("\nZones list sorting is correct", link)
        else:
            print("\nThe zones list is not sorted", link)


def test_countries_sorting_checking(driver):
    authorization(driver)

    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    table = driver.find_element(By.CSS_SELECTOR, "[name = countries_form]")
    all_countries = len(table.find_elements(By.CSS_SELECTOR, "tr.row"))
    countries = list()
    countries_with_zones = list()

    for row in range(all_countries):
        country_name = (driver.find_element(By.XPATH, "//*[@id='content']/form/table/tbody/tr[{}]/td[5]/a".format(row+2))).get_attribute("text")
        countries.append(country_name)
        zone = (driver.find_element(By.XPATH, "//*[@id='content']/form/table/tbody/tr[{}]/td[6]".format(row+2))).get_attribute("textContent")
        if int(zone) > 0:
            country_with_zone = (driver.find_element(By.XPATH, "//*[@id='content']/form/table/tbody/tr[{}]/td[5]/a".format(row+2))).get_attribute("href")
            countries_with_zones.append(country_with_zone)

    sorted_countries_list = sorted(countries)
    if countries == sorted_countries_list:
        print("\nCountries list sorting is correct")
    else:
        print("\nThe countries list is not sorted")

    zone_sorting(driver, countries_with_zones)
