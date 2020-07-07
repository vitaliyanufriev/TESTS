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


class DashboardLocators():
    SANDBOX = (By.CSS_SELECTOR, ".lab.icon.module-icon")
    GENERATE_BUTTON = (By.CSS_SELECTOR, ".ui.primary.button")
    PAY = (By.CSS_SELECTOR, ".TnxHub-submit-button")
    # IFFRAME = (By.XPATH, "/html/body/iframe")
    IFRAME = (By.TAG_NAME, "iframe")
    CARD_JS_CVV = (By.CSS_SELECTOR, ".TnxHub__input[name='cvcInput']")
    CARD_JS_PAY = (By.CSS_SELECTOR, ".TnxHub__submit-button")
    GO_TO_TRANSMITTER = (By.CSS_SELECTOR, ".actions .button")
    SEND_REQUEST = (By.CSS_SELECTOR, ".sandbox-form .Input .button")
    RESPONSE_TRANSACTION_CODE = (By.CSS_SELECTOR, "div.sandbox-preview-container > div:nth-child(2) > span > div > "
                                                  "span.preview-number")
    RESPONSE_TRANSACTION_ID = (By.CSS_SELECTOR, "div.sandbox-preview-container > div:nth-child(15) > span > "
                                                "div > a > span.preview-value")
    TRANSACTIONS = (By.CSS_SELECTOR, ".list.icon.module-icon")
    TRANSACTION_ID = (By.CSS_SELECTOR, "table > tbody > tr:nth-child(1) > "
                                       "td.left.aligned.table-cell.transaction-id-cell > div > div > a")