from time import sleep
from pages.main_page import MainPage
import pytest
from pages.locators import MainPageLocators, BasePageLocators
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
import pytest
from pages.product_page import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from pages.login_page import LoginPage
# from .locators import LoginPageLocators
import time
from pages.base_page import BasePage
from pages.product_page import ProductPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
         #              marks=pytest.mark.xfail),
         # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
         ]


#
#
# @pytest.mark.parametrize('link', links)
# def test_guest_can_add_product_to_basket(browser, link):
#     # Открываем страницу товара
#     product_page = ProductPage(browser, link)
#     product_page.open()
#
#     # Добавляем товар в корзину
#     product_page.add_to_basket()
#
#     product_page.should_be_success_message()
#     product_page.should_be_correct_product_name()
#
#     # Проверяем сообщение со стоимостью корзины
#     product_page.should_be_basket_total()
#     product_page.should_be_correct_basket_total()
#
#
#
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     # Открываем страницу товара
#     product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
#     product_page.open()
#
#     # Добавляем товар в корзину
#     product_page.add_to_basket()
#
#     # Проверяем, что сообщение об успешном добавлении товара не появляется
#     product_page.guest_cant_see_success_message_after_adding_product_to_basket()
#
#
#
#
#
#
#
# def test_guest_cant_see_success_message(browser):
#     product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
#     product_page.open()
#     product_page.guest_cant_see_success_message()
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
#     product_page.open()
#     product_page.add_to_basket()
#     product_page.message_disappeared_after_adding_product_to_basket()
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
# #
#
# def  test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page
#
#
#
#
#
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = MainPageLocators.MAIN_PAGE_LINK
#     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page = MainPage(browser, link)
#     # открываем нужную страницу
#     page.open()
#     page.go_to_basket_page()
#     basket_page = BasketPage(browser, browser.current_url)
#     # проверка, что корзина пустая
#     basket_page.basket_should_be_empty()
#
#
#

#
class TestUserAddToBasketFromProductPage(object):
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Открываем страницу товара
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        product_page.open()

    def test_user_can_register(self, browser):
        # Arrange
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        login_page.open()

        # Act
        email = str(time.time()) + "@fakemail.org"
        password = "password123"
        login_page.register_new_user(email, password)
        base_page = BasePage(browser, browser.current_url)
        base_page.should_be_authorized_user()

        assert login_page.is_element_present(
            *BasePageLocators.REGISTRATION_SUCCESS_MESSAGE), "Registration success message is not presented"

    def test_user_can_add_product_to_basket(self, browser):
        # Открываем страницу товара
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        product_page.open()
#
