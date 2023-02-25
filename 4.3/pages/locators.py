from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, '.row h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner>strong')

    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")   # в козине цкна




class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON_EN_GB = (By.LINK_TEXT, "View basket")
    BASKET_BUTTON_RU = (By.LINK_TEXT, "Посмотреть корзину")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class MainPageLocators():
    MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/"
    LOGIN_LINK = (By.ID, "login_link")

class BasketPageLocators():
    BASKET_EMPTY = (By.ID, "content_inner")
    BASKET_NOT_EMPTY = (By.CLASS_NAME, "basket-title")
    SUBSTRING_BASKET_EN_GB = "Your basket is empty" #"Ваша корзина пуста"
    SUBSTRING_BASKET_RU = "Ваша корзина пуста"


