from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    AUTHORIZATION_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main>h1")
    NAME_PRODUCT_IN_BASKET_SUCCESS = (By.CSS_SELECTOR, "#messages > :nth-child(1) .alertinner")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main>.price_color")
    PRICE_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs")

