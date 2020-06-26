from .base_page import BasePage
from .locators import LoginPageLocators


class RegistrationPage(BasePage):
    def fill_register_form(self, log, pas):
        sign_up = self.browser.find_element(*LoginPageLocators.SIGN_UP)
        sign_up.click()
        email = self.browser.find_element(*LoginPageLocators.EMAIL)
        email.send_keys(log)
        password = self.browser.find_element(*LoginPageLocators.PWD)
        password.send_keys(pas)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PWD)
        confirm_password.send_keys(pas)
        terms = self.browser.find_element(*LoginPageLocators.TERMS)
        terms.click()
        sign_up = self.browser.find_element(*LoginPageLocators.SIGN_IN)
        sign_up.click()
