import pytest
from homework8july.Pages.main_page import MainPage
from homework8july.Pages.cart_page import CartPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import scenarios, given, when, then

scenarios('../homework8july/test_homework_bdd.feature')


@pytest.fixture()
def open_browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@given('We open the site')
def test_open_site(open_browser):
    link = 'http://automationpractice.com/index.php'
    global main_page
    main_page = MainPage(open_browser, link)
    main_page.open()


@when('We verify the cart link and open it')
def test_verify_cart_link_and_open_it():
    main_page.verify_cart_link()
    main_page.open_cart_page()


@then('We verify user is on the cart page')
def test_verify_user_is_on_the_cart_page():
    cart_page = CartPage(open_browser, open_browser.current_url)
    cart_page.verify_title_is_present()
