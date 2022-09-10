import allure
import pytest

from page_objects.to_rent_search_screen import to_rent_search_screen_methods
from page_objects.zoopla_landing_screen import zoopla_landing_methods


class TestZoopla:

    @pytest.mark.code_challenge
    def test_zoopla_save_search_daily_subscription(self, setup):
        landing = zoopla_landing_methods(setup)
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        landing.validate_landing_screen_elements()
        driver = landing.click_to_rent_nav_link()
        to_rent = to_rent_search_screen_methods(driver)
        to_rent.validate_to_rent_search_screen_elements()
        to_rent.enter_search_criteria_hit_search("London", 1, 1000)
        to_rent.validate_to_rent_search_results_screen_elements("London", 1, 1000)
        to_rent.enter_min_price_range(800)
        to_rent.click_on_create_email_alert()



