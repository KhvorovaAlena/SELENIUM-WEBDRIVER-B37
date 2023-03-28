import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)
    return driver


def to_float(string):
    digits = list(filter(lambda x: x.isdigit() or x == "." or x == ",", string))
    return float(''.join(digits))


def color_checker(color):
    if color.red == color.green == color.blue:
        print("The color is grey", color.red, color.green, color.blue)
    elif color.green == color.blue == 0:
        print("The color id red", color.red, color.green, color.blue)
    else:
        print("The color is incorrect", color.red, color.green, color.blue)


def check_regular_price_style(driver):
    print("\nChecking regular price style:")
    duck_price_text_style = driver.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("text-decoration")
    duck_price_font_color = Color.from_string(
        driver.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("color"))

    color_checker(duck_price_font_color)
    if duck_price_text_style.__contains__('line-through'):
        print("Text is crossed")
    else:
        print("Text is not crossed")


def check_campaign_price_style(driver):
    print("\nChecking campaign price style:")
    duck_sale_price_font_weight = driver.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("font-weight")
    duck_sale_price_font_color = Color.from_string(driver.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("color"))

    color_checker(duck_sale_price_font_color)
    if 700 <= (int(duck_sale_price_font_weight)) <= 900:
        print("Text is bold")
    else:
        print("Style is not bold")


def check_fonts_sizes(driver):
    print("\nChecking prices font sizes:")
    duck_price_font_size = to_float(driver.find_element(By.CSS_SELECTOR, ".regular-price").value_of_css_property("font-size"))
    duck_sale_price_font_size = to_float(driver.find_element(By.CSS_SELECTOR, ".campaign-price").value_of_css_property("font-size"))
    if duck_price_font_size < duck_sale_price_font_size:
        print("Sale price font size is bigger than regular price")
    else:
        print("Regular price font size is bigger than sale price")


def duck_detailed_page_checking(driver, duck_name_value, duck_price_value, duck_sale_price_value):
    print("\nChecking for detailed page:")
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

    print("Names:", duck_name_value, "and", detailed_name_value, "\nRegular prices:", duck_price_value, "and",
          detailed_price_value, "\nSale prices:", duck_sale_price_value, "and", detailed_sale_price_value)

    check_regular_price_style(driver)
    check_campaign_price_style(driver)
    check_fonts_sizes(driver)


def test_duck_attributes(driver):
    driver.get("http://localhost/litecart/en/")

    print("\nChecking for main page:")
    campaign_duck = driver.find_element(By.CSS_SELECTOR, "#box-campaigns .product")
    duck_name_value = campaign_duck.find_element(By.CSS_SELECTOR, ".name").get_attribute("textContent")
    duck_price_value = campaign_duck.find_element(By.CSS_SELECTOR, ".regular-price").get_attribute("textContent")
    duck_sale_price_value = campaign_duck.find_element(By.CSS_SELECTOR, ".campaign-price").get_attribute("textContent")

    check_regular_price_style(campaign_duck)
    check_campaign_price_style(campaign_duck)
    check_fonts_sizes(campaign_duck)

    campaign_duck.click()
    duck_detailed_page_checking(driver, duck_name_value, duck_price_value, duck_sale_price_value)
