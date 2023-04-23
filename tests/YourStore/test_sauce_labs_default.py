import pytest

from utils.common_methods import common_methods
from page_objects.sauce_labs.sauce_labs_landing import sauce_labs_landing_page
from page_objects.sauce_labs.sauce_labs_products import all_products_page_methods
from page_objects.sauce_labs.sauce_labs_your_cart import your_cart_methods


class TestSauceLab:

    @pytest.mark.default
    def test_sauce_lab_page_successfully_logged_in(self, setup):
        """
        Open your store webpage and validate landing page elements
        :param setup: pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        utils = common_methods(setup)
        # Navigate to saucedemo url
        utils.goto_url("https://www.saucedemo.com/")
        # Page object landing page created
        landing = sauce_labs_landing_page(utils)
        # Validate all elements of landing page are displayed
        landing.saucelab_landing_page_elements_verification()
        # Capture login credentials from webpage
        landing.fetch_login_credentials()
        # Check user is successfully logged in
        landing.saucelab_login_success()


    @pytest.mark.default
    def test_launch_sauce_lab_page_validation(self, setup):
        """
        Open your store webpage and validate landing page elements
        :param setup: pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        utils = common_methods(setup)
        # Navigate to saucedemo url
        utils.goto_url("https://www.saucedemo.com/")
        # Page object landing page created
        landing = sauce_labs_landing_page(utils)
        # Validate all elements of landing page are displayed
        landing.saucelab_landing_page_elements_verification()
        # Capture login credentials from webpage
        landing.fetch_login_credentials()
        # Check user is successfully logged in
        landing.saucelab_login_Locked_out_user()

    @pytest.mark.default
    def test_sauce_lab_page_successfully_logged_in_problem_user(self, setup):
        """
        Open your store webpage and validate landing page elements
        :param setup: pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        utils = common_methods(setup)
        # Navigate to saucedemo url
        utils.goto_url("https://www.saucedemo.com/")
        # Page object landing page created
        landing = sauce_labs_landing_page(utils)
        # Validate all elements of landing page are displayed
        landing.saucelab_landing_page_elements_verification()
        # Capture login credentials from webpage
        landing.fetch_login_credentials()
        # Check user is successfully logged in
        landing.saucelab_login_success_problem()



    @pytest.mark.default
    def test_sauce_lab_page_successfully_logged_in_slow_user(self, setup):
        """
        Open your store webpage and validate landing page elements
        :param setup: pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        utils = common_methods(setup)
        # Navigate to saucedemo url
        utils.goto_url("https://www.saucedemo.com/")
        # Page object landing page created
        landing = sauce_labs_landing_page(utils)
        # Validate all elements of landing page are displayed
        landing.saucelab_landing_page_elements_verification()
        # Capture login credentials from webpage
        landing.fetch_login_credentials()
        # Check user is successfully logged in
        landing.saucelab_login_success_slow_user()

    @pytest.mark.default
    def test_sauce_lab_all_products_validation(self, setup):
        """
        Open your store webpage and validate landing page elements
        :param setup: pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        utils = common_methods(setup)
        # Navigate to saucedemo url
        utils.goto_url("https://www.saucedemo.com/")
        # Page object landing page created
        landing = sauce_labs_landing_page(utils)
        # Validate all elements of landing page are displayed
        landing.saucelab_landing_page_elements_verification()
        # Capture login credentials from webpage
        landing.fetch_login_credentials()
        # Check user is successfully logged in
        landing.saucelab_login_success()
        all_products = all_products_page_methods(utils)
        all_products.validate_products_all_products_page()

    @pytest.mark.default
    def test_sauce_lab_buy_random_product(self, setup):
        """
        Open your store webpage and validate landing page elements
        :param setup: pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        utils = common_methods(setup)
        # Navigate to saucedemo url
        utils.goto_url("https://www.saucedemo.com/")
        # Page object landing page created
        landing = sauce_labs_landing_page(utils)
        # Validate all elements of landing page are displayed
        landing.saucelab_landing_page_elements_verification()
        # Capture login credentials from webpage
        landing.fetch_login_credentials()
        # Check user is successfully logged in
        landing.saucelab_login_success()
        all_products = all_products_page_methods(utils)
        all_products.validate_products_all_products_page()
        # Add a product to cart and buy it
        all_products.validate_random_product_added_to_cart()
        # Check no of products added to cart
        all_products.validate_no_of_products_in_cart()
        # Get details of all products added to cart
        product_details = all_products.capture_product_details()
        # Click on cart icon and navigate to my cart page
        all_products.click_on_cart_icon()
        # Check user is navigated to My Cart Page
        your_cart = your_cart_methods(utils)






