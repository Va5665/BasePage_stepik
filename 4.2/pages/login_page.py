# from .base_page import BasePage
# from .locators import LoginPageLocators
#
#
# class LoginPage(BasePage):
#     def should_be_login_page(self):
#          self.should_be_login_url()
#          self.should_be_login_form()
#          self.should_be_register_form()
#     #
#
#
#     def should_be_login_url(self):
#         # url = self.browser.url
#         # url.contains('login')
#         assert self.browser.current_url.endswith("/login/")
#         assert True
#
#     def should_be_login_form(self):
#         assert self.is_element_present(*LoginPageLocators.login_form), "Registration form is not presented"
#         assert True
#
#     def should_be_register_form(self):
#         assert self.is_element_present(*LoginPageLocators.register_form), "Registration form is not presented"
#         assert True
