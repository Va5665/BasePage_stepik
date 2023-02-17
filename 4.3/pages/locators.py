from selenium.webdriver.common.by import By

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, '.row h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong')
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")   # в козине цкна
























# from selenium.webdriver.common.by import By
#
#
# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
#
#
#
#
# class  LoginPageLocators():
#     register_form = (By.CSS_SELECTOR, "button[value='Register']")
#     login_form = (By.CSS_SELECTOR, "button[value='Log In']")