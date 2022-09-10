import time
from unittest import TestCase

from selenium.webdriver.common.by import By

from base.page_initial import PageInit
from utils.common_methods import common_methods


class for_sale_search_screen_locs:
    header_for_sale_page = '//div[@id="main-content"]//h1[contains(text(),"Properties for sale")]'
    sub_header_for_sale_page = '//div[@id="main-content"]//p[contains(text(),"Search houses")]'
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
    dropdown_search_radius_search_filter = '//div[@data-testid="search-desktop-subheader"]//select[@id="desktop_radius-filter"]'
    dropdown_bedrooms_search_filter = '//div[@data-testid="search-desktop-subheader"]//button[@label="Bedrooms"]'
    dropdown_price_range_search_filter = '//div[@data-testid="search-desktop-subheader"]//button[@label="Price range"]'
    dropdown_property_type_search_filter = '//div[@data-testid="search-desktop-subheader"]//button[@label="Property type"]'
    button_search_filter = '//button[@data-testid="search-button"]'
    button_create_email_alert = '//button//div[contains(text(), "Create email alert")]'
    dropdown_price_range_min = '//select[@data-testid="min_price"]'
    link_travel_time_search = '//aside[@data-testid="search-sidebar"]//a[contains(text(),"Travel time search")]'


class for_sale_search_screen_methods(PageInit, TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def validate_for_sale_search_screen_elements(self):
        """
        This method will click on check if current page is search results
        :return:None
        """
        common_methods.wait_for_element(self.driver, for_sale_search_screen_locs.header_for_sale_page)
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.header_for_sale_page).is_displayed(),
            "For sale search page header is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.sub_header_for_sale_page).is_displayed(),
            "For sale search page header is not displayed")
        sub_header = self.driver.find_element(By.XPATH, for_sale_search_screen_locs.sub_header_for_sale_page).text
        exp_sub_header = "Search houses and flats for sale across the UK"
        self.assertTrue(exp_sub_header == sub_header, "Incorrect sub-header displayed in For sale search page")
        self.assertTrue(self.driver.find_element(By.XPATH, for_sale_search_screen_locs.label_search_area).is_displayed(),
                        "'Search area' label is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.combobox_search_area).is_displayed(),
            "'Search area' text input field is not displayed ")
        self.assertTrue(self.driver.find_element(By.XPATH, for_sale_search_screen_locs.label_bedrooms).is_displayed(),
                        "'Bedrooms' label is not displayed ")
        self.assertTrue(self.driver.find_element(By.XPATH, for_sale_search_screen_locs.dropdown_bedrooms).is_displayed(),
                        "'Bedrooms' dropdown is not displayed ")
        self.assertTrue(self.driver.find_element(By.XPATH, for_sale_search_screen_locs.label_max_price).is_displayed(),
                        "'Max price' label is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, for_sale_search_screen_locs.dropdown_max_price).is_displayed(),
            "'Max price' dropdown is not displayed ")
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