from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def fill_login_form(self, log, pas):
        email = self.browser.find_element(*LoginPageLocators.EMAIL)
        email.send_keys(log)
        password = self.browser.find_element(*LoginPageLocators.PWD)
        password.send_keys(pas)
        sign_in = self.browser.find_element(*LoginPageLocators.SIGN_IN)
        sign_in.click()
        self.should_be_dash_url()

    def should_be_dash_url(self):
        assert "dashboard" in str(self.browser.current_url), "/dashboard missed in URL"