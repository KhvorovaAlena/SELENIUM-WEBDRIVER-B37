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









    # all_countries_names = (list(map(lambda x: x.text, all_countries)))
    # sorted_countries = sorted(all_countries_names)
    #
    # print("\nOrdinary list: ", all_countries_names)
    # print("\nSorted list: ", sorted_countries)
    #
    # if all_countries_names == sorted_countries:
    #     print("Sorting is correct")
    # else:
    #     print("The list is not sorted")
    #
    # all_zones = table.find_elements(By.CSS_SELECTOR, "td:nth-child(6)")
    # all_zones_count = (list(map(lambda x: x.text, all_zones)))
    # for zone in all_zones_count:
    #     if int(zone) > 0:

















    #
    # count_most_popular_ducks = len(driver.find_elements(By.CSS_SELECTOR, "#box-most-popular .product"))
    # print("\nThe most popular ducks count: ", count_most_popular_ducks)
    # for item in range(count_most_popular_ducks):
    #     duck = driver.find_element(By.CSS_SELECTOR, ".product:nth-child({})".format((item + 1)))
    #     are_elements_present(duck, By.CSS_SELECTOR, ".sticker")
    #
    # count_campaigns_ducks = len(driver.find_elements(By.CSS_SELECTOR, "#box-campaigns .product"))
    # print("\nCampaigns ducks count: ", count_campaigns_ducks)
    # for item in range(count_campaigns_ducks):
    #     duck = driver.find_element(By.CSS_SELECTOR, ".product:nth-child({})".format((item + 1)))
    #     are_elements_present(duck, By.CSS_SELECTOR, ".sticker")
    #
    # count_latest_ducks = len(driver.find_elements(By.CSS_SELECTOR, "#box-latest-products .product"))
    # print("\nThe latest ducks count: ", count_latest_ducks)
    # for item in range(count_latest_ducks):
    #     duck = driver.find_element(By.CSS_SELECTOR, ".product:nth-child({})".format((item + 1)))
    #     are_elements_present(duck, By.CSS_SELECTOR, ".sticker")