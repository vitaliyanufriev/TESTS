from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".ui.center.aligned.segment.auth-form-container")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, ".auth-form [name='email']")
    PWD = (By.CSS_SELECTOR, ".auth-form [name='password']")
    CONFIRM_PWD = (By.CSS_SELECTOR, ".auth-form [name='confirmPassword']")
    TERMS = (By.CSS_SELECTOR, ".ui.checkbox > label")
    SIGN_IN = (By.CSS_SELECTOR, ".ui.large.button.auth-submit")
    SIGN_UP = (By.CSS_SELECTOR, ".auth-form-footer [href='/signup']")
