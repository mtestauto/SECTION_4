from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page1 = LoginPage(browser, link)
    page1.open()
    page1.should_be_login_url()

def test_autorization_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page1 = LoginPage(browser, link)
    page1.open()
    page1.should_be_login_form()

def test_registration_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page1 = LoginPage(browser, link)
    page1.open()
    page1.should_be_register_form()



