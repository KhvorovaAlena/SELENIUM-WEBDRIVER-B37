#На странице корзины нужно удалить товар из корзины
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def cart_open(self):
        self.driver.find_element(By.CSS_SELECTOR, ".content").click()
        return self

    def remove_items_from_cart(self):
        ducks = self.driver.find_elements(By.CSS_SELECTOR, ".shortcuts li")
        ducks_count = len(ducks)
        for i in range(ducks_count):
            table = self.driver.find_element(By.CSS_SELECTOR, ".dataTable")
            self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[name='remove_cart_item']")))
            self.driver.find_element(By.CSS_SELECTOR, "[name='remove_cart_item']").click()
            self.wait.until(EC.staleness_of(table))
        return self
