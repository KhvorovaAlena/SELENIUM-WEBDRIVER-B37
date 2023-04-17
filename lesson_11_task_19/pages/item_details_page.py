#На странице деталей нужно добавить элемент в корзину и проверить, что счетчик корзины увеличился
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ItemsDetailsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def is_element_present(self, locator):
        return len(self.driver.find_elements(By.CSS_SELECTOR, locator)) > 0

    def add_item_in_cart(self):
        if self.is_element_present("[name='options[Size]']"):
            self.driver.find_element(By.CSS_SELECTOR, "[name='options[Size]']").click()
            self.driver.find_element(By.CSS_SELECTOR, "[value='Small']").click()

        row_counter = self.driver.find_element(By.CSS_SELECTOR, ".quantity").get_attribute("textContent")
        counter = int(row_counter)
        row_quantity = self.driver.find_element(By.CSS_SELECTOR, "[name='quantity']").get_attribute("value")
        quantity = int(row_quantity)
        expected_items_count = str(counter + quantity)

        self.driver.find_element(By.CSS_SELECTOR, "[name='add_cart_product']").click()
        self.wait.until(EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, ".quantity"), "textContent",
                                                              expected_items_count))


