#На главной страницы нужны методы открытия этой страницы и клик по первому элементу
from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("http://localhost/litecart/en/")
        return self

    def open_product_details(self):
        self.driver.find_element(By.CSS_SELECTOR, "#box-most-popular li").click()
        return self
