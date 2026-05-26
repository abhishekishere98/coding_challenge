import pytest
from playwright.sync_api import expect

from page_objects.sauce_labs.playwright_pages.landing_loginPage_pw import LoginPage


@pytest.mark.playwright
@pytest.mark.sauce_labs
@pytest.mark.e2e
def test_place_order(set_up) -> None:
    """
    Verify that user is able to place an order successfully
    """
    page = set_up
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)

    product_name = "Sauce Labs Fleece Jacket"
    checkout_p = products_p.click_add_to_cart_or_remove(product_name)\
        .click_cart_icon()\
        .click_checkout_button()\
        .enter_checkout_details("Fn12", "Ln12", "0011")\
        .click_continue()\
        .click_finish_button()

    expect(checkout_p.get_confirm_message()).to_have_text("THANK YOU FOR YOUR ORDER")
