import pytest
from playwright.sync_api import Page, expect
from page_objects.sauce_labs.playwright_pages.landing_loginPage_pw import LoginPage


@pytest.mark.playwright
@pytest.mark.sauce_labs
def test_logout(set_up) -> None:

    page = set_up
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.do_logout()
    expect(login_p.login_button).to_be_visible()
