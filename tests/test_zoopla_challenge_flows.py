import allure
import pytest

from page_objects.to_rent_search_screen import to_rent_search_screen_methods
from page_objects.zoopla_landing_screen import zoopla_landing_methods
from utils.common_methods import common_methods


class TestZoopla:
    # def __init__(self, driver):
    #     super().__init__(driver)
    @allure.title("Search flight test")
    @allure.description("This is test of searching flight")
    @pytest.mark.code_challenge
    def test_zoopla_save_search_daily_subscription(self, setup):
        landing = zoopla_landing_methods(setup)
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        landing.validate_landing_screen_elements()
        driver = landing.click_to_rent_nav_link()
        to_rent = to_rent_search_screen_methods(driver)
        to_rent.check_current_page_is_search_result()
        to_rent.enter_search_criteria_hit_search("London", 1, 1000)


