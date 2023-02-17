# from time import sleep
#
# import pytest
#
# from pages.product_page import ProductPage
#
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser):
#     # Открываем страницу товара
#     product_page = ProductPage(browser, link)
#
#     product_page.open()
#
#     # Добавляем товар в корзину
#     product_page.add_to_basket()
#
#     product_page.should_be_success_message()
#
#     product_page.should_be_correct_product_name()
#
#     # Проверяем сообщение со стоимостью корзины
#     product_page.should_be_basket_total()
#     product_page.should_be_correct_basket_total()


from time import sleep

import pytest

from pages.product_page import ProductPage
import pytest
from pages.product_page import ProductPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
         ]

@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    # Открываем страницу товара
    product_page = ProductPage(browser, link)
    product_page.open()

    # Добавляем товар в корзину
    product_page.add_to_basket()

    product_page.should_be_success_message()
    product_page.should_be_correct_product_name()

    # Проверяем сообщение со стоимостью корзины
    product_page.should_be_basket_total()
    product_page.should_be_correct_basket_total()