import time
from random import randint
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from base.page_initial import PageInit
from utils.common_methods import common_methods


class for_sale_search_screen_locs:
    """
    This Class will store all locators pertaining to For sale search and results screens
    """
    header_for_sale_page = '//div[@id="main-content"]//h1[contains(text(),"Properties for sale")]'
    sub_header_for_sale_page = '//div[@id="main-content"]//p[contains(text(),"for sale in the UK")]'
    label_search_area = '//label[text()="Search area"]'
    combobox_search_area = '//input[@placeholder="e.g. Oxford or NW3"]'
    label_bedrooms = '//label[text()="Bedrooms"]'
    dropdown_bedrooms = '//div[text()="Any beds"]//parent::button'
    label_max_price = '//label[text()="Max price"]'
    dropdown_max_price = '//div[text()="No max"]//parent::button'
    label_property_type = '//label[text()="Property type"]'
    radio_button_show_all = '//div[@role="radiogroup"]//button[@role="radio" and @value="show all"]'
    radio_button_houses = '//div[@role="radiogroup"]//button[@role="radio" and @value="houses"]'
    radio_button_flats = '//div[@role="radiogroup"]//button[@role="radio" and @value="flats"]'
    labels_radio_buttons = '//button[@role="radio"]//following-sibling::div//label'
    button_search = '//button[@data-testid="search-btn"]'
    # Search result section
    search_result_header = '//div[@data-testid="search-desktop-subheader"]'
    textbox_search_area = "//input[@id='header-location']"
    dropdown_search_radius_search_filter = '//div[@data-testid="search-desktop-subheader"]//select[@id="desktop_radius-filter"]'
    dropdown_bedrooms_search_filter = '//div[@data-testid="search-desktop-subheader"]//button[@label="Bedrooms"]'
    dropdown_price_range_search_filter = '//div[@data-testid="search-desktop-subheader"]//button[@label="Price range"]'
    dropdown_price_max = "//select[@id='price_max']"
    dropdown_property_type_search_filter = '//div[@data-testid="search-desktop-subheader"]//button[@label="Property type"]'
    button_search_filter = '//button[@data-testid="search-button"]'
    button_create_email_alert = '//button//div[contains(text(), "Create email alert")]'
    dropdown_price_range_min = '//select[@data-testid="min_price"]'
    link_travel_time_search = '//aside[@data-testid="search-sidebar"]//a[contains(text(),"Travel time search")]'
    button_filter = '//button[@data-testid="search-results-header_filters-button"]'
    header_filter_your_results = '//h2[contains(text(),"Filter your results")]'
    textbox_keywords_filter = '//input[@id="keywords"]'
    button_update_results = '//div[text()="Update Results"]//parent::button'
    header_feature_description = '//section[@data-testid]//h2[@id="listing-features-heading"]'
    text_feature_description_garage = '//*[contains(text(),"garage") or contains(text(),"Garage")]'
    list_search_results = '//a[@data-testid="listing-details-link"]'
    button_save_search_for_sale_result = '//div[text()="Save this search"]//parent::div//parent::button'
    button_save_search = '//div[text()="Save your search and alert"]//parent::button'
    dropdown_alert_frequency = '//select[@id="alert_frequency"]'
    msg_success_search_saved = '//h2[contains(text(),"Success! Your search")]'
    link_manage_my_saved_searches = '//a[text()="Manage my saved searches"]//parent::div'
    button_return_to_search_results = '//button[normalize-space()="Return to search results"]'


class for_sale_search_screen_methods(PageInit, TestCase):
    """
    This class is to bind the methods and locators of For sale search and results page together, by implementing execution
    steps related to this page within this file. It implements PageInit and Testcase classes to support webdriver and
    Junit assertions
    """

    def __init__(self, driver: webdriver):
        """
        This is constructor for page object which will initialise the driver
        :param driver: webdriver instance to perform required actions
        """
        super().__init__(driver)

    def validate_for_sale_search_screen_elements(self):
        """
        This method will click on check if current page is search results
        :return:None
        """
        # Check for heading, text check is skipped and xpath compares for exact text match
        common_methods.wait_for_element(self.driver, for_sale_search_screen_locs.header_for_sale_page)
        time.sleep(2)
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.header_for_sale_page).is_displayed(),
            "For sale search page header is not displayed")
        # Check for sub heading
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.sub_header_for_sale_page).is_displayed(),
            "For sale search page header is not displayed")
        sub_header = self.driver.find_element(By.XPATH, for_sale_search_screen_locs.sub_header_for_sale_page).text
        exp_sub_header = "Search flats and houses for sale in the UK"
        self.assertTrue(exp_sub_header == sub_header, "Incorrect sub-header displayed in For sale search page")
        # Search area validation
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.label_search_area).is_displayed(),
            "'Search area' label is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.combobox_search_area).is_displayed(),
            "'Search area' text input field is not displayed ")
        # Bedrooms validation
        self.assertTrue(self.driver.find_element(By.XPATH, for_sale_search_screen_locs.label_bedrooms).is_displayed(),
                        "'Bedrooms' label is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.dropdown_bedrooms).is_displayed(),
            "'Bedrooms' dropdown is not displayed ")
        # Max Price validation
        self.assertTrue(self.driver.find_element(By.XPATH, for_sale_search_screen_locs.label_max_price).is_displayed(),
                        "'Max price' label is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.dropdown_max_price).is_displayed(),
            "'Max price' dropdown is not displayed ")
        # Validations for radio buttons
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.label_property_type).is_displayed(),
            "'Property type' label is not displayed ")
        radio_labels = self.driver.find_elements(By.XPATH, for_sale_search_screen_locs.labels_radio_buttons)
        radio_label_names = []
        exp_label_names = ["Show all", "Houses", "Flats"]
        for i in radio_labels:
            radio_label_names.append(i.text)
        self.assertListEqual(radio_label_names, exp_label_names,
                             f"All radio labels are displayed as expected{radio_label_names}")
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.radio_button_show_all).is_displayed(),
            "'Show all' radio button is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.radio_button_houses).is_displayed(),
            "'Houses' radio button is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.radio_button_flats).is_displayed(),
            "'Flats' radio button is not displayed ")
        self.assertTrue(self.driver.find_element(By.XPATH, for_sale_search_screen_locs.button_search).is_displayed(),
                        "'Search' button is not displayed")

    def enter_search_criteria_hit_search(self, area: str):
        """
        This method will enter area where property for sale will be listed and hit search
        :param area: The area where property sale should be listed
        :return: None
        """
        # Enter search area text and trigger search
        common_methods.wait_till_element_clickable(self.driver, for_sale_search_screen_locs.combobox_search_area)
        self.driver.find_element(By.XPATH, for_sale_search_screen_locs.combobox_search_area).click()
        self.driver.find_element(By.XPATH, for_sale_search_screen_locs.combobox_search_area).send_keys(
            area + Keys.ENTER)
        time.sleep(2)

    def enter_search_criteria_hit_search_criteria(self, area: str, bedrooms: int, max_price: int):
        """
        This method will search for a property for sale with area bedrooms and max price as per user input
        :param area: Area in which search has to performed
        :param bedrooms: No of bedrooms required in search results
        :param max_price: Maximum price for property
        :return: None
        """
        # wait till elements load
        common_methods.wait_till_element_clickable(self.driver, for_sale_search_screen_locs.combobox_search_area)
        self.driver.find_element(By.XPATH, for_sale_search_screen_locs.dropdown_bedrooms).click()
        time.sleep(2)
        # Enter bedrooms
        self.driver.find_element(By.XPATH,
                                 f'//ul[@role="listbox"]//li[@role="option"]//div[contains(text(),"{bedrooms}+")]').click()
        time.sleep(2)
        # Enter max price
        self.driver.find_element(By.XPATH, for_sale_search_screen_locs.dropdown_max_price).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 f'//ul[@role="listbox"]//li[@role="option"]//div[contains(text(),"{"{:,}".format(max_price)}")]').click()
        time.sleep(2)
        # Enter Search area
        self.driver.find_element(By.XPATH, for_sale_search_screen_locs.combobox_search_area).click()
        self.driver.find_element(By.XPATH, for_sale_search_screen_locs.combobox_search_area).send_keys(
            area + Keys.ENTER)
        common_methods.wait_for_elements(self.driver, for_sale_search_screen_locs.list_search_results)
        time.sleep(2)

    def validate_for_sale_search_results_screen_elements(self, search_area: str):
        """
        This method will validate search result screen UI elements
        :return: None
        """
        # Wait till page loads
        common_methods.wait_till_element_is_visible(self.driver, for_sale_search_screen_locs.search_result_header)
        # Validation for search area
        self.assertTrue(self.driver.find_element(By.XPATH, f'//div[@data-testid="search-desktop-subheader"]//input['
                                                           f'@value="{search_area}"]').is_displayed())
        area = self.driver.find_element(By.XPATH, f'//div[@data-testid="search-desktop-subheader"]//input['
                                                  f'@value="{search_area}"]').get_attribute("value")
        self.assertTrue(area == search_area, "Search area is not same as user input")
        # Validation for header
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.search_result_header).is_displayed(),
            "'Search Result' header is not displayed")
        # Filter elements
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 for_sale_search_screen_locs.dropdown_search_radius_search_filter).is_displayed(),
                        "'Search radius' filter is not displayed")
        # Bedrooms
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 for_sale_search_screen_locs.dropdown_bedrooms_search_filter).is_displayed(),
                        "'Bedrooms' filter is not displayed")
        # Property type
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 for_sale_search_screen_locs.dropdown_property_type_search_filter).is_displayed(),
                        "'Property type' radius filter is not displayed")
        # price range
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 for_sale_search_screen_locs.dropdown_price_range_search_filter).is_displayed(),
                        "'Price range' filter is not displayed")
        # Search button
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.button_search_filter).is_displayed(),
            "'Search' button is not displayed")
        # Create email alert button
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.button_create_email_alert).is_displayed(),
            "'Create email alert' button is not displayed")
        # Save search button
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.button_save_search_for_sale_result).is_displayed(),
            "'Save search' button is not displayed")

    def enter_search_keyword(self, keyword: str):
        """
        This method will enter keyword for filtering search results and update search results
        :param keyword: The keyword required to filter search results
        :return: None
        """
        # Click on filter button
        self.driver.find_element(By.XPATH, for_sale_search_screen_locs.button_filter).click()
        common_methods.wait_till_element_is_visible(self.driver, for_sale_search_screen_locs.header_filter_your_results)
        time.sleep(1)
        # Header check
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.header_filter_your_results).is_displayed(),
            "'Filter your results' header is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.textbox_keywords_filter).is_displayed(),
            "'Filter your results' header is not displayed")
        # Enter search keyword
        self.driver.find_element(By.XPATH, for_sale_search_screen_locs.textbox_keywords_filter).send_keys(keyword)
        # Click on search
        self.driver.find_element(By.XPATH, for_sale_search_screen_locs.button_update_results).click()
        time.sleep(4)

    def validate_keyword_search_successful(self, keyword: str):
        """
        This method will validate if keyword related search is successful by randomly selecting a result
        and clicking on it to check if features and description section has garage keyword
        :param keyword: The keyword searched
        :return:None
        """
        # Wait till search results appear
        common_methods.wait_till_element_is_visible(self.driver, for_sale_search_screen_locs.button_save_search_for_sale_result)
        time.sleep(3)
        # Click on a result randomly if results are displayed
        elements = self.driver.find_elements(By.XPATH, for_sale_search_screen_locs.list_search_results)
        if elements is not None or elements.__len__() != 0:
            random = randint(0, elements.__len__() - 1)
            elements[random].click()
            # Wait for page load
            common_methods.wait_for_element(self.driver, for_sale_search_screen_locs.header_feature_description)
            time.sleep(3)
            # Look for specified keyword
            self.assertTrue(
                self.driver.find_elements(By.XPATH, f'//*[contains(text(),"{keyword.lower()}") or contains(text(),"{keyword.upper()}") or contains(text(),"{keyword.lower().capitalize()}")]'),
                "Garage keyword is missing in search results")

    def click_travel_time_search_link(self):
        """
        This method will click on travel time search link
        :return: None
        """
        time.sleep(2)
        common_methods.wait_for_element(self.driver, for_sale_search_screen_locs.link_travel_time_search)
        self.driver.find_element(By.XPATH, for_sale_search_screen_locs.link_travel_time_search).click()
        time.sleep(2)

    def click_save_results(self):
        """
        This method will save the search results from search
        :return: None
        """
        # Wait for save button to be clickable and click
        common_methods.wait_till_element_clickable(self.driver,
                                                   for_sale_search_screen_locs.button_save_search_for_sale_result)
        self.driver.find_element(By.XPATH,
                                 for_sale_search_screen_locs.button_save_search_for_sale_result).click()
        time.sleep(2)
        # Wait till save button in pop up is clickable
        common_methods.wait_till_element_clickable(self.driver, for_sale_search_screen_locs.button_save_search)
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 for_sale_search_screen_locs.button_save_search).click()
        time.sleep(2)
        # Wait for success message
        common_methods.wait_for_element(self.driver, for_sale_search_screen_locs.msg_success_search_saved)
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 for_sale_search_screen_locs.msg_success_search_saved).is_displayed(),
                        "'Success' message is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 for_sale_search_screen_locs.link_manage_my_saved_searches).is_displayed(),
                        "'Manage my saved searches' Link is not displayed")
        # Click on link using action class
        time.sleep(2)
        a = ActionChains(self.driver)
        a.move_to_element(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.button_return_to_search_results)).perform()
        time.sleep(2)
        a.click(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.button_return_to_search_results)).perform()
        time.sleep(5)

    def validate_retrieved_search(self, area: str, bedrooms: int, max_price: int):
        """
        This method will validate if retrieved search result is as per saved search
        :param area: Area for which search was saved
        :param bedrooms: Bedrooms for which search was saved
        :param max_price: Maximum price for which search was saved
        :return: None
        """
        # wait for page load
        common_methods.wait_till_element_clickable(self.driver,
                                                   for_sale_search_screen_locs.dropdown_price_range_search_filter)
        time.sleep(2)
        # Validate area
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.textbox_search_area).get_attribute(
                "value").find(area) + 1,
            "Incorrect Search area retrieved")
        # Validate bedroom
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 for_sale_search_screen_locs.dropdown_bedrooms_search_filter).get_attribute(
            "title").find(str(bedrooms))+1,
                        "Incorrect Bedrooms retrieved")
        # Validate price range
        self.driver.find_element(By.XPATH, for_sale_search_screen_locs.dropdown_price_range_search_filter).click()
        time.sleep(2)
        obj = Select(self.driver.find_element(By.XPATH, for_sale_search_screen_locs.dropdown_price_max))
        self.assertTrue(obj.first_selected_option.text.find(str("{:,}".format(max_price))) + 1,
                        "Incorrect maximum price retrieved")
