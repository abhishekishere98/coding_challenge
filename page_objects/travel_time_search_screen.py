import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

from base.page_initial import PageInit
from unittest import TestCase

from utils.common_methods import common_methods


class time_search_loc:
    """
    This Class will store all locators for Travel time search screen
    """
    header_time_search = '//form[@name = "search-form"]//h1'
    sub_header_time_search = '//form[@name = "search-form"]//p'
    radio_for_sale = '//div[@id="search-section-wrapper"]//input[@value="for-sale"]'
    radio_to_rent = '//div[@id="search-section-wrapper"]//input[@value="to-rent"]'
    label_radio_for_sale = '//label[normalize-space()="For sale"]'
    label_radio_to_rent = '//label[normalize-space()="To rent"]'
    textbox_area = '//input[@id="search-input-location"]'
    labels_search_criteria_for_sale = '//div[contains(@class,"search-attributes-col") and not(contains(@class,"to-rent"))]//label[not(contains(@for,"week"))]'
    dropdown_max_travel_time_for_sale = '//select[@id="duration"]'
    dropdown_method_of_transfer_for_sale = '//select[@id="transport_type"]'
    dropdown_min_price_for_sale = '//select[@id="forsale_price_min"]'
    dropdown_max_price_for_sale = '//select[@id="forsale_price_max"]'
    dropdown_property_type_for_sale = '//select[@id="property_type"]'
    dropdown_bedrooms_for_sale = '//select[@id="beds_min"]'
    button_search = '//button[@id="search-submit"]'
    link_advanced_search = '//div[@class="search-bottom-left"]//span'


class travel_time_search(PageInit, TestCase):
    """
    This class is to bind the methods and locators of Time Travel search page together, by implementing execution
    steps related to this page within this file. It implements PageInit and Testcase classes to support webdriver and
    Junit assertions
    """

    def __init__(self, driver):
        """
        This is constructor for page object which will initialise the driver
        :param driver: webdriver instance to perform required actions
        """
        super().__init__(driver)

    def validate_travel_time_search_page_elements(self):
        """
        This method will validate travel time search page elements
        :return: None
        """
        # Wait for page load
        common_methods.wait_for_element(self.driver, time_search_loc.header_time_search)
        time.sleep(3)
        # Heading
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.header_time_search).is_displayed(),
            "Travel Time search page header is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.header_time_search).text.strip() == "Travel time search",
            "Travel Time Search heading is displayed with incorrect text")
        # sub heading
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.sub_header_time_search).is_displayed(),
            "Travel Time search page sub heading is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, time_search_loc.sub_header_time_search).text ==
                        "Enter target destination that you will be travelling to",
                        "Travel Time Search sub heading is displayed with incorrect text")
        # Radio buttons
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.label_radio_for_sale).is_displayed(),
            "Radio 'For sale' label is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.label_radio_to_rent).is_displayed(),
            "Radio 'To rent' label is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.radio_to_rent),
            "Radio button 'To rent' is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.radio_for_sale),
            "Radio button 'To rent' is not displayed")
        # Area
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.textbox_area).is_displayed(),
            "Textbox 'PostCode,School or Station' label is not displayed")
        # Labels
        elements = self.driver.find_elements(By.XPATH, time_search_loc.labels_search_criteria_for_sale)
        labels = []
        for i in elements:
            labels.append(i.text)
        expected_labels = ["Max travel time", "Method of transport", "Min price", "Max price", "Property type",
                           "Bedrooms"]
        self.assertListEqual(labels, expected_labels, f"All labels are not displayed with correct text : {labels}")
        # Maximum Travel Time
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.dropdown_max_travel_time_for_sale).is_displayed(),
            "Dropdown 'Max travel time' is not displayed")
        # Mode of transport
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.dropdown_method_of_transfer_for_sale).is_displayed(),
            "Dropdown 'Method of transport' is not displayed")
        # Minimum price
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.dropdown_min_price_for_sale).is_displayed(),
            "Dropdown 'Min price' is not displayed")
        # Maximum price
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.dropdown_max_travel_time_for_sale).is_displayed(),
            "Dropdown 'Max price' is not displayed")
        # Property
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.dropdown_property_type_for_sale).is_displayed(),
            "Dropdown 'Property type' is not displayed")
        # Bedrooms
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.dropdown_bedrooms_for_sale).is_displayed(),
            "Dropdown 'Bedrooms' is not displayed")
        # Search button
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.button_search).is_displayed(),
            "Button 'Search' is not displayed")
        # Advanced search link
        self.assertTrue(
            self.driver.find_element(By.XPATH, time_search_loc.link_advanced_search).is_displayed(),
            "Link 'Advanced search options' is not displayed")

    def enter_search_criteria_hit_search(self, postcode: str, max_travel_time: str, method_of_transport: str):
        """
        This method will enter all relevant data for Travel Time Search and hit search button
        :param postcode: Postcode where search needs to be performed
        :param max_travel_time: Maximum travel time expected
        :param method_of_transport: Mode of transportation
        :return: None
        """
        # Select class selecting Max travel time
        obj = Select(self.driver.find_element(By.XPATH, time_search_loc.dropdown_max_travel_time_for_sale))
        obj.select_by_visible_text(max_travel_time)
        time.sleep(2)
        # Select class selecting Method of transfer
        obj = Select(self.driver.find_element(By.XPATH, time_search_loc.dropdown_method_of_transfer_for_sale))
        obj.select_by_visible_text(method_of_transport)
        time.sleep(2)
        # Area
        self.driver.find_element(By.XPATH, time_search_loc.textbox_area).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, time_search_loc.textbox_area).send_keys(postcode + Keys.ENTER)
        time.sleep(5)
