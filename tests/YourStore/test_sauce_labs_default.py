import pytest

from utils.common_methods import common_methods
from page_objects.sauce_labs.sauce_labs_landing import sauce_labs_landing_page


class TestSauceLab:

    @pytest.mark.default
    def test_launch_sauce_lab_page_validation(self, setup):
        """
        Open your store webpage and validate landing page elements
        :param setup: pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        utils = common_methods(setup)
        # creating driver context to be used across execution for creating page objects
        driver = utils.yield_driver()
        # Navigate to saucedemo url
        utils.goto_url("https://www.saucedemo.com/")
        # Page object landing page created
        landing = sauce_labs_landing_page(utils)
        # Validate all elements of landing page are displayed
        landing.saucelab_landing_page_elements_verification()
        landing.fetch_login_credentials()
        landing.saucelab_login_success()





