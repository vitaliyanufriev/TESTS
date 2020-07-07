from .base_page import BasePage
from .locators import DashboardLocators
import time


class DashboardPage(BasePage):
    def create_sandbox_transaction(self):
        sandbox = self.browser.find_element(*DashboardLocators.SANDBOX)
        sandbox.click()
        generate_button = self.browser.find_element(*DashboardLocators.GENERATE_BUTTON)
        generate_button.click()
        pay_button = self.browser.find_element(*DashboardLocators.PAY)
        pay_button.click()
        # time.sleep(0.5)
        iframeElement = self.browser.find_element(*DashboardLocators.IFRAME)
        self.browser.switch_to.frame(iframeElement)
        # self.browser.switch_to_frame(self.browser.find_element(*DashboardLocators.IFFRAME))
        card_cvv = self.browser.find_element(*DashboardLocators.CARD_JS_CVV)
        card_cvv.send_keys('440')
        card_js_pay_button = self.browser.find_element(*DashboardLocators.CARD_JS_PAY)
        card_js_pay_button.click()
        self.browser.switch_to_default_content()
        go_to_transmitter = self.browser.find_element(*DashboardLocators.GO_TO_TRANSMITTER)
        go_to_transmitter.click()
        send_request = self.browser.find_element(*DashboardLocators.SEND_REQUEST)
        send_request.click()
        response_transaction_id = self.browser.find_element(*DashboardLocators.RESPONSE_TRANSACTION_ID)
        resp_trans_id = response_transaction_id.text
        self.check_sandbox_response_code()
        transaction_page = self.browser.find_element(*DashboardLocators.TRANSACTIONS)
        transaction_page.click()
        transaction_id = self.browser.find_element(*DashboardLocators.TRANSACTION_ID)
        assert transaction_id.text == resp_trans_id, 'Transaction not found'
        print('\nTransaction with ID ' + transaction_id.text + " was created")

    def check_sandbox_response_code(self):
        response_code = self.browser.find_element(*DashboardLocators.RESPONSE_TRANSACTION_CODE)
        assert response_code.text == '0', self.browser.save_screenshot("screenshot.png")
        # "Code isn't 0, code is " + response_code.text

