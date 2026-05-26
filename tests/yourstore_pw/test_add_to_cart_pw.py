import pytest
from playwright.sync_api import Page, expect

from page_objects.sauce_labs.playwright_pages.landing_loginPage_pw import LoginPage

@pytest.mark.new_pw
@pytest.mark.playwright
@pytest.mark.sauce_labs
@pytest.mark.smoke
def test_add_to_cart(page: Page) -> None:
    """
    Verify that add to cart button is changed to Remove when clicked
    """
    page = page
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)

    product_name = "Sauce Labs Bolt T-Shirt"

    products_p.click_add_to_cart_or_remove(product_name)

    expect(products_p.get_add_remove_cart_locator(product_name)).to_have_text("Remove")


@pytest.mark.playwright
@pytest.mark.sauce_labs
def test_remove_product_from_cart(page) -> None:
    page = page
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)

    product_name = "Sauce Labs Bolt T-Shirt"

    products_p.click_add_to_cart_or_remove(product_name)

    products_p.click_add_to_cart_or_remove(product_name)

    expect(products_p.get_add_remove_cart_locator(product_name)).to_have_text("Add to cart")
