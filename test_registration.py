from .pages.registration_page import RegistrationPage
from .gmail_test import MailClient
import random

LOG = 'vitandtnx' + str(random.randint(1000,9999)) + '@gmail.com'
PASS = 'qwerty1A'
LINK =


def test_sign_in(browser):
    link = LINK + "/signin"
    page = RegistrationPage(browser, link)
    mail = MailClient()
    page.open()
    page.fill_register_form(LOG, PASS)
    mail.confirmation_link()
