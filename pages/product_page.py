from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_product_name_success(self):
        product_main_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        print(product_main_name.text)
        product_basket_name = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET_SUCCESS)
        print(product_basket_name.text)
        assert product_main_name.text in product_basket_name.text, f"NOK {product_main_name.text} NOT IN " \
                                                                   f"{product_basket_name.text}"

    def should_be_product_price_success(self):
        price_main_value = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        print(price_main_value.text)
        price_prod_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_IN_BASKET)
        print(price_prod_in_basket.text)
        assert price_main_value.text in price_prod_in_basket.text, f"NOK {price_main_value} " \
                                                         f"NOT IN {price_prod_in_basket}"


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")



