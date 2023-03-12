import pytest

from utils.common_methods import common_methods
from page_objects.sauce_labs.sauce_labs_landing import sauce_labs_landing_page
from page_objects.sauce_labs.sauce_labs_products import landing_page_methods


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
        all_products = landing_page_methods(utils)
        all_products.validate_products_all_products_page()



