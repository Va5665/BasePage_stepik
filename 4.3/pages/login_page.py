from .base_page import BasePage
from .locators import LoginPageLocators





class LoginPage(BasePage):
    def should_be_login_page(self):
         self.should_be_login_url()
         self.should_be_login_form()
         self.should_be_register_form()
    #


    def should_be_login_url(self):
        url = self.browser.url
        url.contains('login')
        assert self.browser.current_url.endswith("/login/")
        assert True



    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        email_input.send_keys(email)

        password_input1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT1)
        password_input1.send_keys(password)

        password_input2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT2)
        password_input2.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        register_button.click()

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_EMAIL_INPUT), "Registration email input is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD_INPUT1), "Registration password input1 is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD_INPUT2), "Registration password input2 is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), "Registration submit button is not presented"