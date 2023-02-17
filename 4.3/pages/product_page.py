



from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert product_name == success_message, "Product name is not correct in the success message"


    def should_be_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MESSAGE), "Basket total message is not presented"

    def should_be_correct_basket_total(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total_message = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_MESSAGE).text
        assert product_price == basket_total_message, "Basket total is not equal to the product price"


