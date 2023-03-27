import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


def duck_detailed_page_checking(driver, duck_name_value, duck_price_value, duck_sale_price_value):
    detailed_name_value = driver.find_element(By.CSS_SELECTOR, "h1.title").get_attribute("textContent")
    detailed_price_value = driver.find_element(By.CSS_SELECTOR, ".regular-price").get_attribute("textContent")
    detailed_sale_price_value = driver.find_element(By.CSS_SELECTOR, ".campaign-price").get_attribute("textContent")

    if duck_name_value == detailed_name_value:
        print("Names are the same")
    else:
        print("Names are not the same")

    if duck_price_value == detailed_price_value and duck_sale_price_value == detailed_sale_price_value:
        print("Regular and sale prices are the same")
    else:
        print("Regular and sale prices are not the same")

    print("\nNames:", duck_name_value, "and", detailed_name_value, "\nRegular prices:", duck_price_value, "and",
          detailed_price_value, "\nSale prices:", duck_sale_price_value, "and", detailed_sale_price_value)

    duck_price_text_style = driver.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("text-decoration")
    if str(duck_price_text_style) == "line-through solid rgb(102, 102, 102)":
        print("Text is crossed and grey")
    else:
        print("Style is not correct")

    duck_sale_price_font_weight = driver.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("font-weight")
    duck_sale_price_font_color = Color.from_string(driver.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("color"))
    default_sale_price_color = Color.from_string('rgba(204, 0, 0, 1)')
    if (str(duck_sale_price_font_weight) == "700") and (duck_sale_price_font_color == default_sale_price_color):
        print("Text is bold and red")
    else:
        print("Style is not bold and red")

    duck_price_font_size = driver.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("font-size")
    duck_sale_price_font_size = driver.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("font-size")
    if duck_price_font_size < duck_sale_price_font_size:
        print("Sale price font size is bigger than regular price")
    else:
        print("Regular price font size is bigger than sale price")


def test_duck_attributes(driver):
    driver.get("http://localhost/litecart/en/")
    campaign_duck = driver.find_element(By.CSS_SELECTOR, "#box-campaigns .product")

    duck_name_value = campaign_duck.find_element(By.CSS_SELECTOR, ".name").get_attribute("textContent")
    duck_price_value = campaign_duck.find_element(By.CSS_SELECTOR, ".regular-price").get_attribute("textContent")
    duck_sale_price_value = campaign_duck.find_element(By.CSS_SELECTOR, ".campaign-price").get_attribute("textContent")

    duck_price_text_style = campaign_duck.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("text-decoration")
    if str(duck_price_text_style) == "line-through solid rgb(119, 119, 119)":
        print("\nText is crossed and grey")
    else:
        print("\nStyle is not correct")

    duck_sale_price_font_weight = campaign_duck.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("font-weight")
    duck_sale_price_font_color = Color.from_string(campaign_duck.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("color"))
    default_sale_price_color = Color.from_string('rgba(204, 0, 0, 1)')
    if (str(duck_sale_price_font_weight) == "700") and (duck_sale_price_font_color == default_sale_price_color):
        print("\nText is bold and red")
    else:
        print("\nStyle is not bold and red")

    duck_price_font_size = campaign_duck.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("font-size")
    duck_sale_price_font_size = campaign_duck.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("font-size")
    if duck_price_font_size < duck_sale_price_font_size:
        print("\nSale price font size is bigger than regular price")
    else:
        print("\nRegular price font size is bigger than sale price")

    campaign_duck.click()
    duck_detailed_page_checking(driver, duck_name_value, duck_price_value, duck_sale_price_value)






