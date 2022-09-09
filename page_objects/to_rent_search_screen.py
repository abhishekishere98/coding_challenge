import time
from unittest import TestCase

from selenium.webdriver.common.by import By

from base.page_initial import PageInit
from utils.common_methods import common_methods


class to_rent_search_screen_locs:
    header_to_rent_page = '//div[@id="main-content"]//h1[contains(text(),"Properties to rent")]'
    sub_header_to_rent_page = '//div[@id="main-content"]//p[contains(text(),"Search houses")]'
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


class to_rent_search_screen_methods(PageInit, TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def check_current_page_is_search_result(self):
        """
        This method will click on check if current page is search results
        :return:
        """
        common_methods.wait_for_element(self.driver, to_rent_search_screen_locs.header_to_rent_page)
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.header_to_rent_page).is_displayed(),
            "To rent search page header is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.sub_header_to_rent_page).is_displayed(),
            "To rent search page header is not displayed")
        sub_header = self.driver.find_element(By.XPATH, to_rent_search_screen_locs.sub_header_to_rent_page).text
        exp_sub_header = "Search houses and flats to rent across the UK"
        self.assertTrue(exp_sub_header == sub_header, "Incorrect sub-header displayed in To rent search page")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.label_search_area).is_displayed(),
                        "'Search area' label is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.combobox_search_area).is_displayed(),
            "'Search area' text input field is not displayed ")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.label_bedrooms).is_displayed(),
                        "'Bedrooms' label is not displayed ")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_bedrooms).is_displayed(),
                        "'Bedrooms' dropdown is not displayed ")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.label_max_price).is_displayed(),
                        "'Max price' label is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_max_price).is_displayed(),
            "'Max price' dropdown is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.label_property_type).is_displayed(),
            "'Property type' label is not displayed ")
        radio_labels = self.driver.find_elements(By.XPATH, to_rent_search_screen_locs.labels_radio_buttons)
        radio_label_names = []
        exp_label_names = ["Show all", "Houses", "Flats"]
        for i in radio_labels:
            radio_label_names.append(i.text)
        self.assertListEqual(radio_label_names, exp_label_names,
                             f"All radio labels are displayed as expected{radio_label_names}")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.radio_button_show_all).is_displayed(),
            "'Show all' radio button is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.radio_button_houses).is_displayed(),
            "'Houses' radio button is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.radio_button_flats).is_displayed(),
            "'Flats' radio button is not displayed ")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.button_search).is_displayed(),
                        "'Search' button is not displayed")

    def enter_search_criteria_hit_search(self, search_area, bedrooms, max_price):
        """
        This method will enter criteria in search fields and click on search button
        :return: None
        """
        self.driver.find_element(By.XPATH, to_rent_search_screen_locs.combobox_search_area).click()
        self.driver.find_element(By.XPATH, to_rent_search_screen_locs.combobox_search_area).send_keys(search_area)
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 f'//ul[@role="listbox"]//li[@role="option"]//span[text()="{search_area}"]').click()
        self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_bedrooms).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 f'//ul[@role="listbox"]//li[@role="option"]//div[contains(text(),"{bedrooms}+")]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_max_price).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 f'//ul[@role="listbox"]//li[@role="option"]//div[contains(text(),"{"{:,}".format(max_price)} pcm")]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, to_rent_search_screen_locs.button_search).click()

    def click_search_button(self):
        """
        This method will click on search button to trigger search
        :return: None
        """
        self.driver.find_element(to_rent_search_screen_locs.button_search).click()
        time.sleep(3)
