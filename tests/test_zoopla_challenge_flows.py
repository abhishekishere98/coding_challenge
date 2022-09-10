import allure
import pytest

from page_objects.for_sale_search_screen import for_sale_search_screen_methods
from page_objects.house_prices_search_screen import house_prices_search_methods
from page_objects.to_rent_search_screen import to_rent_search_screen_methods
from page_objects.travel_time_search_screen import travel_time_search
from page_objects.zoopla_landing_screen import zoopla_landing_methods
from page_objects.zoopla_login_screen import zoopla_login_methods


class TestZoopla:



    def test_zoopla_save_search_daily_subscription(self, setup):
        """
        Register for daily email updates on rental property in London for 1 bed properties between £800 and £1000 per month
        :param setup:
        :return:
        """
        landing = zoopla_landing_methods(setup)
        driver = landing.yield_driver()
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        landing.validate_landing_screen_elements()
        landing.click_sign_in_nav_link()
        login = zoopla_login_methods(driver)
        login.validate_login_page_elements()
        login.enter_login_info_click_sign_in("abhishekishere98@gmail.com", "Work4aig!")
        landing.click_to_rent_nav_link()
        to_rent = to_rent_search_screen_methods(driver)
        to_rent.validate_to_rent_search_screen_elements()
        to_rent.enter_search_criteria_hit_search("London", 1, 1000)
        to_rent.validate_to_rent_search_results_screen_elements("London")
        to_rent.enter_min_price_range(800)
        to_rent.click_on_create_email_alert("Daily summary emails")


    def test_change_frequency_save_search(self, setup):
        """
        Change the frequency of an existing email update
        :param setup:
        :return:
        """
        landing = zoopla_landing_methods(setup)
        driver = landing.yield_driver()
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        landing.validate_landing_screen_elements()
        landing.click_sign_in_nav_link()
        login = zoopla_login_methods(driver)
        login.validate_login_page_elements()
        login.enter_login_info_click_sign_in("abhishekishere98@gmail.com", "Work4aig!")
        landing.click_to_rent_nav_link()
        to_rent = to_rent_search_screen_methods(driver)
        to_rent.validate_to_rent_search_screen_elements()
        to_rent.enter_search_criteria_hit_search("London", 1, 1000)
        to_rent.validate_to_rent_search_results_screen_elements("London")
        to_rent.enter_min_price_range(800)
        to_rent.click_on_create_email_alert("Daily summary emails")



    @pytest.mark.code_challenge
    def test_sale_house_prices_search(self, setup):
        """
        Search for a particular property in the house prices search and confirm that it appears as the first result
        :return:
        """
        landing = zoopla_landing_methods(setup)
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        landing.validate_landing_screen_elements()
        landing.click_house_prices_nav_link()
        driver = landing.yield_driver()
        house_prices = house_prices_search_methods(driver)
        house_prices.validate_house_prices_search_page_elements()
        house_prices.enter_area_postcode_and_hit_search("SW16")
        house_prices.validate_house_price_search_result_elements()
        house_prices.enter_price_search_criteria("3 months", "Any", "Sold (newest - oldest)")
        house_prices.validate_first_result("Flat 16, Radnor House, 1272 London Road, London, SW16 4EA")


    def test_for_sale_house_garage_search(self, setup):
        """
        Search houses for sale including the key word “garage” and check that results have garages
        :param setup:
        :return:
        """
        landing = zoopla_landing_methods(setup)
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        landing.validate_landing_screen_elements()
        landing.click_for_sale_nav_link()
        driver = landing.yield_driver()
        for_sale = for_sale_search_screen_methods(driver)
        for_sale.validate_for_sale_search_screen_elements()
        for_sale.enter_search_criteria_hit_search("London")
        for_sale.validate_for_sale_search_results_screen_elements("London")
        for_sale.enter_search_keyword("Garage")
        for_sale.validate_keyword_search_successful("Garage")


    def test_time_search_in_area(self, setup):
        """
        Save a search for property within 15 minutes drive of SE1 2LH.
        :return:
        """
        landing = zoopla_landing_methods(setup)
        driver = landing.yield_driver()
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        landing.validate_landing_screen_elements()
        landing.click_sign_in_nav_link()
        login = zoopla_login_methods(driver)
        login.validate_login_page_elements()
        login.enter_login_info_click_sign_in("abhishekishere98@gmail.com", "Work4aig!")
        landing.click_for_sale_nav_link()
        for_sale = for_sale_search_screen_methods(driver)
        for_sale.validate_for_sale_search_screen_elements()
        for_sale.enter_search_criteria_hit_search("SE1 2LH")
        for_sale.validate_for_sale_search_results_screen_elements("SE1 2LH")
        for_sale.click_travel_time_search_link()
        travel_time = travel_time_search(driver)
        travel_time.validate_travel_time_search_page_elements()
        travel_time.enter_search_criteria_hit_search("SE1 2LH", "15 minutes", "Driving")
        for_sale.click_save_results()


    def test_retrive_saved_searches(self, setup):
        """
        Check that saved searches can be retrieved
        :return:
        """
