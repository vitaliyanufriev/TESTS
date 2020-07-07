from .pages.login_page import LoginPage

LOG = 'vitandtnx@gmail.com'
PASS = 'qwerty1A'
LINK = 'ddd'


def test_create_sandbox_transaction(browser):
    link = LINK + "/signin"
    page = LoginPage(browser, link)
    page.open()
    page.fill_login_form(LOG, PASS)
    dashboard = page.dashboard_page_link()
    dashboard.create_sandbox_transaction()
