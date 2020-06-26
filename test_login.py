from .pages.login_page import LoginPage
import time

LOG = 'vitandtnx+2@gmail.com'
PASS = 'qwerty1A'
LINK =

def test_sign_in(browser):
    link = LINK + "/signin"
    page = LoginPage(browser, link)
    page.open()
    page.fill_login_form(LOG, PASS)
