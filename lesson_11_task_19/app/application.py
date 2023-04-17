from selenium import webdriver
from pages.main_page import MainPage
from pages.item_details_page import ItemsDetailsPage
from pages.cart_page import CartPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.item_details_page = ItemsDetailsPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def quit(self):
        self.driver.quit()

    def open_main_page(self):
        self.main_page.open()

    def open_items_details_page(self):
        self.main_page.open_product_details()

    def add_items_in_cart(self):
        self.item_details_page.add_item_in_cart()

    def clear_cart(self):
        self.cart_page.cart_open()
        self.cart_page.remove_items_from_cart()

