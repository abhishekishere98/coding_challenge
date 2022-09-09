import allure
import pytest

from page_objects.zoopla_landing_screen import zoopla_landing_methods
from utils.common_methods import common_methods


class TestZoopla():
    # def __init__(self, driver):
    #     super().__init__(driver)
    comm =common_methods
    @allure.title("Search flight test")
    @allure.description("This is test of searching flight")
    @pytest.mark.code_challenge
    def test_zoopla_save_search_daily_subscription(self, setup):
        landing = zoopla_landing_methods(setup, TestZoopla.comm)
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        landing.validate_landing_screen_elements()
        landing.click_to_rent_nav_link()


