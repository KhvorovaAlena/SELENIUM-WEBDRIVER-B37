import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver

def are_elements_present(driver, *args):
    check = len(driver.find_elements(*args))
    if check == 1:
        print("Test is passed. The element has only one sticker")
    else:
        print("Test is not passed. The element does not have only one sticker")
    return check

def test_stickers_present(driver):
    driver.get("http://localhost/litecart/en/")

    count_most_popular_ducks = len(driver.find_elements(By.CSS_SELECTOR, "#box-most-popular .product"))
    print("\nThe most popular ducks count: ", count_most_popular_ducks)
    for item in range(count_most_popular_ducks):
        duck = driver.find_element(By.CSS_SELECTOR, ".product:nth-child({})".format((item + 1)))
        are_elements_present(duck, By.CSS_SELECTOR, ".sticker")

    count_campaigns_ducks = len(driver.find_elements(By.CSS_SELECTOR, "#box-campaigns .product"))
    print("\nCampaigns ducks count: ", count_campaigns_ducks)
    for item in range(count_campaigns_ducks):
        duck = driver.find_element(By.CSS_SELECTOR, ".product:nth-child({})".format((item + 1)))
        are_elements_present(duck, By.CSS_SELECTOR, ".sticker")

    count_latest_ducks = len(driver.find_elements(By.CSS_SELECTOR, "#box-latest-products .product"))
    print("\nThe latest ducks count: ", count_latest_ducks)
    for item in range(count_latest_ducks):
        duck = driver.find_element(By.CSS_SELECTOR, ".product:nth-child({})".format((item + 1)))
        are_elements_present(duck, By.CSS_SELECTOR, ".sticker")