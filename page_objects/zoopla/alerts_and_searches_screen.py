import datetime
import time
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.page_initial import PageInit
from utils.common_methods import common_methods


class alerts_searches_locs:
    """
    This Class will store all locators for Alerts and Searches screen
    """
    header_alerts_searches = "//h1[normalize-space()='Alerts & searches']"
    tab_residential = "(//a[normalize-space()='Residential'])[1]"
    tab_commercial = "//li[@aria-controls='tab-commercial']//a[text()='Commercial']"
    tab_to_rent = "//li[@aria-controls='tab-residential-to-rent']//a[text()='To rent']"
    tab_for_sale = "//li[@aria-controls='tab-residential-for-sale']//a[text()='For sale']"
    column_header_alerts_searches = "//div[@id='tab-residential-to-rent']//div[@class='myaccount-alert-col']//strong"
    text_saved_date_first_result = "(//div[@id='tab-residential-to-rent']//div[@class='clearfix top myaccount-alert-item type-alert'])[1]//p"
    text_saved_date_first_result_sale = "(//div[@id='tab-residential-for-sale']//div[@class='clearfix top myaccount-alert-item type-alert'])[1]//p"
    header_location_first_result = "( //div[@id='tab-residential-to-rent']//div[@class='clearfix top myaccount-alert-item type-alert'])[1]//h4"
    header_location_first_result_sale = "( //div[@id='tab-residential-for-sale']//div[@class='clearfix top myaccount-alert-item type-alert'])[1]//h4"
    text_location_first_result = "(( //div[@id='tab-residential-to-rent']//div[@class='clearfix top myaccount-alert-item type-alert'])[1]//li)[1]"
    text_location_first_result_sale = "(( //div[@id='tab-residential-for-sale']//div[@class='clearfix top myaccount-alert-item type-alert'])[1]//li)[1]"
    text_bedrooms_first_result = "(( //div[@id='tab-residential-to-rent']//div[@class='clearfix top myaccount-alert-item type-alert'])[1]//li)[2]"
    text_price_range_first_result = "(( //div[@id='tab-residential-to-rent']//div[@class='clearfix top myaccount-alert-item type-alert'])[1]//li)[3]"
    dropdown_first_saved_search_frequency = "(( //div[@id='tab-residential-to-rent']//div[@class='clearfix top myaccount-alert-item type-alert'])//div[@class='myaccount-alert-col']//select)[1]"
    link_view_first_result = "( //div[@id='tab-residential-to-rent']//div[@class='clearfix top myaccount-alert-item type-alert'])[1]//div[@class='myaccount-alert-col']//a[text()='View']"
    link_view_first_result_sale = "( //div[@id='tab-residential-for-sale']//div[@class='clearfix top myaccount-alert-item type-alert'])[1]//div[@class='myaccount-alert-col']//a[text()='View']"
    link_delete_first_result = "( //div[@id='tab-residential-to-rent']//div[@class='clearfix top myaccount-alert-item type-alert'])[1]//div[@class='myaccount-alert-col']//a[text()='Delete']"
    results_saved_searches_to_rent = '//div[@id="tab-residential-to-rent"]'
    results_saved_searches_for_sale = '//div[@id="tab-residential-for-sale"]'
    links_left_navigation_menu = '//ul[@class="myaccount-main-nav"]//li//a'


class alerts_searches_methods(PageInit, TestCase):
    """
    This class is to bind the methods and locators of Alerts and Searches page together, by implementing execution
    steps related to this page within this file. It implements PageInit and Testcase classes to support webdriver and
    Junit assertions
    """
    def __init__(self, driver: webdriver):
        """
        This is constructor for page object which will initialise the driver
        :param driver: webdriver instance to perform required actions
        """
        super().__init__(driver)

    def validate_alerts_searches_screen(self):
        """
        This method will validate the UI elements of alerts and searches screen
        :return:
        """
        # Wait till header appears
        common_methods.wait_for_element(self.driver, alerts_searches_locs.header_alerts_searches)
        time.sleep(3)
        self.assertTrue(self.driver.find_element(By.XPATH, alerts_searches_locs.header_alerts_searches).is_displayed(),
                        "Company Logo not displayed")
        # Validation for navigation link names in left panel
        nav_list = self.driver.find_elements(By.XPATH, alerts_searches_locs.links_left_navigation_menu)
        name_nav = []
        for ele in nav_list:
            name_nav.append(ele.text)
        expected_nav = ["My Zoopla", "My profile", "Alerts & searches", "Email preferences", "Saved properties",
                        "Property notes"]
        self.assertListEqual(name_nav, expected_nav, f"Displayed left navigation menu has incorrect text : {name_nav}")
        # Assertions for available tabs
        self.assertTrue(self.driver.find_element(By.XPATH, alerts_searches_locs.tab_residential).is_displayed(),
                        "Tab residential not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, alerts_searches_locs.tab_commercial).is_displayed(),
                        "Tab commercial not displayed")
        # Validation for column names displayed
        col_list = self.driver.find_elements(By.XPATH, alerts_searches_locs.column_header_alerts_searches)
        name_col = []
        for ele in col_list:
            name_col.append(ele.get_attribute("innerHTML"))
        expected_col = ["Saved searches and alerts", "Frequency", "Actions"]
        self.assertListEqual(name_col, expected_col, f"Displayed column names have incorrect text : {name_col}")

    def select_tab_for_sale(self, tab_name: str):
        """
        This method will select a tab based on user input
        :param tab_name: Name of the tab uses wishes to select
        :return: None
        """
        # Tab selection based on user input
        match tab_name:
            case "Residential":
                self.driver.find_element(By.XPATH, alerts_searches_locs.tab_residential).click()
            case "Commercial":
                self.driver.find_element(By.XPATH, alerts_searches_locs.tab_commercial).click()
            case "To rent":
                self.driver.find_element(By.XPATH, alerts_searches_locs.tab_to_rent).click()
            case "For sale":
                self.driver.find_element(By.XPATH, alerts_searches_locs.tab_for_sale).click()
        time.sleep(3)

    def validate_first_saved_record_to_rent(self, area, bedrooms, min_price, max_price, frequency):
        """
        This method will validate saved search based on user input
        :param area: Expected area saved to search
        :param bedrooms: Expected bedrooms saved to search
        :param min_price: Expected minimum price saved to search
        :param max_price: Expected maximum price saved to search
        :param frequency: Expected frequency of email saved to search
        :return: None
        """
        # Validation for date when record is saved
        today = datetime.date.today()
        day = today.day
        month = today.strftime("%b")
        year = today.strftime("%Y")
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
        exp_date = str(day) + suffix + " " + month + " " + year
        self.assertTrue(
            self.driver.find_element(By.XPATH, alerts_searches_locs.text_saved_date_first_result).text.find(exp_date),
            "The date saved is not today's date")
        # Validation for area
        self.assertTrue(
            self.driver.find_element(By.XPATH, alerts_searches_locs.header_location_first_result).text.find(area)+1,
            "The location displayed in result header doesnt match with saved search")
        self.assertTrue(
            self.driver.find_element(By.XPATH, alerts_searches_locs.text_location_first_result).text.find(area),
            "The location displayed in result text doesnt match with saved search")
        # Validation for bedrooms
        self.assertTrue(
            self.driver.find_element(By.XPATH, alerts_searches_locs.text_bedrooms_first_result).text.find(str(bedrooms)),
            "The bedrooms displayed in result doesnt match with saved search")
        # Validation for minimum price
        self.assertTrue(
            self.driver.find_element(By.XPATH, alerts_searches_locs.text_price_range_first_result).text.find(''"{:,}".format(min_price)+' pcm'),
            "Min price is not displayed in result")
        # Validation for maximum price
        self.assertTrue(
            self.driver.find_element(By.XPATH, alerts_searches_locs.text_price_range_first_result).text.find(''"{:,}".format(max_price)+' pcm'),
            "Max price is not displayed in result")
        # Validation for frequency of emails
        obj = Select(self.driver.find_element(By.XPATH, alerts_searches_locs.dropdown_first_saved_search_frequency))
        frequency_fetched = obj.first_selected_option.text
        self.assertTrue(frequency_fetched == frequency, f"Frequency of search result is not same as user input :{frequency_fetched}")
        # Validation for view link
        self.assertTrue(
            self.driver.find_element(By.XPATH, alerts_searches_locs.link_view_first_result).is_displayed(),
            "View link is not displayed in result")
        # Validation for delete link
        self.assertTrue(
            self.driver.find_element(By.XPATH, alerts_searches_locs.link_delete_first_result).is_displayed(),
            "Delete link is not displayed in result")

    def change_frequency_first_saved_search(self, frequency):
        """
        This method will change the frequency of first saved result to user input
        :param frequency: The new frequency of emails to be selected
        :return:None
        """
        # Using select class for handling dropdown and value selection
        obj = Select(self.driver.find_element(By.XPATH, alerts_searches_locs.dropdown_first_saved_search_frequency))
        obj.select_by_visible_text(frequency)
        time.sleep(2)
        self.driver.get(self.driver.current_url)
        time.sleep(2)
        # refresh page and check if frequency selected is persisted
        self.driver.refresh()
        time.sleep(4)
        obj = Select(self.driver.find_element(By.XPATH, alerts_searches_locs.dropdown_first_saved_search_frequency))
        obj.select_by_visible_text(frequency)
        time.sleep(2)
        current_frequency = obj.first_selected_option.text
        self.assertTrue(current_frequency == frequency, "Frequency of search result is not same as user input")

    def validate_first_saved_record_for_sale(self, area):
        """
        This method will validate saved search based on user input
        :return: None
        """
        # Using select class for handling dropdown and value selection
        today = datetime.date.today()
        day = today.day
        month = today.strftime("%b")
        year = today.strftime("%Y")
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
        exp_date = str(day) + suffix + " " + month + " " + year
        self.assertTrue(
            self.driver.find_element(By.XPATH, alerts_searches_locs.text_saved_date_first_result_sale).text.find(exp_date))
        # Validation for area
        self.assertTrue(
            self.driver.find_element(By.XPATH, alerts_searches_locs.header_location_first_result_sale).text.find(area)+1)
        self.assertTrue(
            self.driver.find_element(By.XPATH, alerts_searches_locs.text_location_first_result_sale).text.find(area))

    def retrieve_saved_search(self):
        """
        This method will click on view button for first saved search result to retrieve search
        :return: None
        """
        # Click on saved search to view search
        time.sleep(2)
        self.driver.find_element(By.XPATH, alerts_searches_locs.link_view_first_result_sale).click()
        time.sleep(5)
