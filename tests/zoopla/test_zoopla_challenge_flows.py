import pytest

from page_objects.zoopla.alerts_and_searches_screen import alerts_searches_methods
from page_objects.zoopla.for_sale_search_screen import for_sale_search_screen_methods
from page_objects.zoopla.house_prices_search_screen import house_prices_search_methods
from page_objects.zoopla.to_rent_search_screen import to_rent_search_screen_methods
from page_objects.zoopla.travel_time_search_screen import travel_time_search
from page_objects.zoopla.zoopla_landing_screen import zoopla_landing_methods
from page_objects.zoopla.zoopla_login_screen import zoopla_login_methods


class TestZoopla:

    @pytest.mark.code_challenge
    def test_zoopla_save_search_daily_subscription(self, setup):
        """
        Register for daily email updates on rental property in London for 1 bed properties between £800 and £1000 per month
        :param setup: Pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        landing = zoopla_landing_methods(setup)
        # creating driver context to be used across execution for creating page objects
        driver = landing.yield_driver()
        # Navigate to zoopla url
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        # Landing screen UI elements validation
        landing.validate_landing_screen_elements()
        # Click on sign in button
        landing.click_sign_in_nav_link()
        # Create login page object
        login = zoopla_login_methods(driver)
        # Validate login page ui elements
        login.validate_login_page_elements()
        # Enter login credentials and click on sign in
        login.enter_login_info_click_sign_in("abhishekishere98@gmail.com", "Work4aig!")
        # Click on to rent link
        landing.click_to_rent_nav_link()
        # create to rent page object
        to_rent = to_rent_search_screen_methods(driver)
        # Validate to rent screen elements
        to_rent.validate_to_rent_search_screen_elements()
        # Enter search criteria area, bedrooms, maximum price
        to_rent.enter_search_criteria_hit_search("London", 1, 1000)
        # Validate to rent search results screen UI elements
        to_rent.validate_to_rent_search_results_screen_elements("London")
        # Enter minimum price
        to_rent.enter_min_price_range(800)
        # Select email frequency to daily
        to_rent.click_on_create_email_alert("Daily summary emails")
        # Navigate to user account section
        landing.click_account_nav_link()
        # Navigate to saved searches
        landing.navigate_to_saved_searches()
        # Create alerts page object
        alert_search = alerts_searches_methods(driver)
        # Validate alerts and searches screen elements
        alert_search.validate_alerts_searches_screen()
        # Select tp rent tab in alerts and searches screen
        alert_search.select_tab_for_sale("To rent")
        # Validate search is saved based on date, area, bedrooms, min price, maximum price and frequency of emails
        alert_search.validate_first_saved_record_to_rent("London", 1, 800, 1000, "Daily summary emails")

    @pytest.mark.code_challenge
    def test_change_frequency_save_search(self, setup):
        """
        Change the frequency of an existing email update
        :param setup: Pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        landing = zoopla_landing_methods(setup)
        # creating driver context to be used across execution for creating page objects
        driver = landing.yield_driver()
        # Navigate to zoopla url
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        # Landing screen UI elements validation
        landing.validate_landing_screen_elements()
        # Click on sign in button
        landing.click_sign_in_nav_link()
        # Create login page object
        login = zoopla_login_methods(driver)
        # Validate login page ui elements
        login.validate_login_page_elements()
        # Enter login credentials and click on sign in
        login.enter_login_info_click_sign_in("abhishekishere98@gmail.com", "Work4aig!")
        # Click on to rent link
        landing.click_to_rent_nav_link()
        # create to rent page object
        to_rent = to_rent_search_screen_methods(driver)
        # Validate to rent screen elements
        to_rent.validate_to_rent_search_screen_elements()
        # Enter search criteria area, bedrooms, maximum price
        to_rent.enter_search_criteria_hit_search("London", 1, 1000)
        # Validate to rent search results screen UI elements
        to_rent.validate_to_rent_search_results_screen_elements("London")
        # Enter minimum price
        to_rent.enter_min_price_range(800)
        # Select email frequency to daily
        to_rent.click_on_create_email_alert("Daily summary emails")
        # Navigate to user account section
        landing.click_account_nav_link()
        # Navigate to saved searches
        landing.navigate_to_saved_searches()
        # Create alerts page object
        alert_search = alerts_searches_methods(driver)
        # Validate alerts and searches screen elements
        alert_search.validate_alerts_searches_screen()
        # Select tp rent tab in alerts and searches screen
        alert_search.select_tab_for_sale("To rent")
        # Validate search is saved based on date, area, bedrooms, min price, maximum price and frequency of emails
        alert_search.validate_first_saved_record_to_rent("London", 1, 800, 1000, "Daily summary emails")
        # Enter the new frequency for saved alert
        alert_search.change_frequency_first_saved_search('Weekly summary emails')

    @pytest.mark.code_challenge
    def test_sale_house_prices_search(self, setup):
        """
        Search for a particular property in the house prices search and confirm that it appears as the first result
        :param setup: Pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        landing = zoopla_landing_methods(setup)
        # creating driver context to be used across execution for creating page objects
        driver = landing.yield_driver()
        # Navigate to zoopla url
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        # Landing screen UI elements validation
        landing.validate_landing_screen_elements()
        # Click on House prices link
        landing.click_house_prices_nav_link()
        # Create house prices page object
        house_prices = house_prices_search_methods(driver)
        # Validate house prices search page UI elements
        house_prices.validate_house_prices_search_page_elements()
        # Enter area as search criteria and hit search
        house_prices.enter_area_postcode_and_hit_search("SW16")
        # Validate house prices search result screen UI elements
        house_prices.validate_house_price_search_result_elements()
        # Filter results with more criteria
        house_prices.enter_price_search_criteria("3 months", "Any", "Sold (newest - oldest)")
        # Validate first result is the property expected to be returned
        house_prices.validate_first_result("Flat 16, Radnor House, 1272 London Road, London, SW16 4EA")

    @pytest.mark.code_challenge
    def test_for_sale_house_garage_search(self, setup):
        """
        Search houses for sale including the key word “garage” and check that results have garages
        :param setup: Pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        landing = zoopla_landing_methods(setup)
        # creating driver context to be used across execution for creating page objects
        driver = landing.yield_driver()
        # Navigate to zoopla url
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        # Landing screen UI elements validation
        landing.validate_landing_screen_elements()
        # Click on for sale link
        landing.click_for_sale_nav_link()
        # Create for sale page object
        for_sale = for_sale_search_screen_methods(driver)
        # Validate for sale UI elements
        for_sale.validate_for_sale_search_screen_elements()
        # Enter search criteria For sale search
        for_sale.enter_search_criteria_hit_search("London")
        # Validate UI elements for For sale search result page
        for_sale.validate_for_sale_search_results_screen_elements("London")
        # Implement keyword based search
        for_sale.enter_search_keyword("Garage")
        # Pick a random result and check that the result details page has keyword searched
        for_sale.validate_keyword_search_successful("Garage")

    @pytest.mark.code_challenge
    def test_time_search_in_area(self, setup):
        """
        Save a search for property within 15 minutes drive of SE1 2LH.
        param setup: Pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        landing = zoopla_landing_methods(setup)
        # creating driver context to be used across execution for creating page objects
        driver = landing.yield_driver()
        # Navigate to zoopla url
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        # Landing screen UI elements validation
        landing.validate_landing_screen_elements()
        # Click on sign in link
        landing.click_sign_in_nav_link()
        # Create login page object
        login = zoopla_login_methods(driver)
        # Validate login page ui elements
        login.validate_login_page_elements()
        # Enter login credentials and click on sign in
        login.enter_login_info_click_sign_in("abhishekishere98@gmail.com", "Work4aig!")
        # Click on For sale link
        landing.click_for_sale_nav_link()
        # Create For sale page object
        for_sale = for_sale_search_screen_methods(driver)
        # Validate For sale search page UI elements
        for_sale.validate_for_sale_search_screen_elements()
        # Enter search criteria and hit search
        for_sale.enter_search_criteria_hit_search("SE1 2LH")
        # Validate For sale search results screen UI elements
        for_sale.validate_for_sale_search_results_screen_elements("SE1 2LH")
        # Click on travel time search link
        for_sale.click_travel_time_search_link()
        # Create Travel Time search link
        travel_time = travel_time_search(driver)
        # Validate Travel Time search UI elements
        travel_time.validate_travel_time_search_page_elements()
        # Enter search criteria for Travel Time search
        travel_time.enter_search_criteria_hit_search("SE1 2LH", "15 minutes", "Driving")
        # Click Save results in travel time search page
        for_sale.click_save_results()

    @pytest.mark.code_challenge
    def test_retrieve_saved_searches(self, setup):
        """
        Check that saved searches can be retrieved
        :param setup: Pytest fixture to initiate and yield driver
        :return: None
        """
        # create landing page object through pytest fixture setup
        landing = zoopla_landing_methods(setup)
        # creating driver context to be used across execution for creating page objects
        driver = landing.yield_driver()
        # Navigate to zoopla url
        landing.goto_zoopla_home_page("https://zoopla.co.uk")
        # Landing screen UI elements validation
        landing.validate_landing_screen_elements()
        # Click on sign in button
        landing.click_sign_in_nav_link()
        # Create login page object
        login = zoopla_login_methods(driver)
        # Validate login page ui elements
        login.validate_login_page_elements()
        # Enter login credentials and click on sign in
        login.enter_login_info_click_sign_in("abhishekishere98@gmail.com", "Work4aig!")
        # Click on For sale link
        landing.click_for_sale_nav_link()
        # Create For sale page object
        for_sale = for_sale_search_screen_methods(driver)
        # Validate For sale screen elements
        for_sale.validate_for_sale_search_screen_elements()
        # Enter for sale search criteria area, bedrooms, maximum price
        for_sale.enter_search_criteria_hit_search_criteria("SE1 2LH", 2, 10000)
        # Click on save search results in For sale search results screen
        for_sale.click_save_results()
        # Click on Account link
        landing.click_account_nav_link()
        # Navigate to saved searches
        landing.navigate_to_saved_searches()
        # Create Alerts and Searches page object
        alert_search = alerts_searches_methods(driver)
        # Validate Alerts and searches screen elements
        alert_search.validate_alerts_searches_screen()
        # Retrieve saved searches
        alert_search.retrieve_saved_search()
        # Validate saved search is retrieved correctly
        for_sale.validate_retrieved_search("SE1 2LH", 2, 10000)
