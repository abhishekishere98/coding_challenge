import pytest
import allure

from page_objects.zoopla_landing_screen import zoopla_landing_methods
from base.page_initial import PageInit


class TestZoopla(PageInit):
    def __int__(self, driver):
        super().__init__(driver)

    @allure.title("Search flight test")
    @allure.description("This is test of searching flight")
    @pytest.mark.code_challenge
    def test_zoopla_save_search_daily_subscription(self):
        landing = zoopla_landing_methods(self.driver)
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        landing.validate_landing_screen_elements()


