import time
from unittest import TestCase

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.page_initial import PageInit
from utils.common_methods import common_methods


class house_prices_search_loc:
    header_house_prices_search = "//h1[normalize-space()='Research sold house prices']"
    sub_header_house_prices_search = "//div[@id='main-content']//div//p[contains(text(),'get started')]"
    label_search_area = "//label[text()='Search area']"
    textbox_search_area = "//div[@role='combobox']//input"
    button_house_prices_search = "//button[@data-testid='search-btn']"
    # Search results section
    header_house_prices_search_results = "//h1[contains(normalize-space(),'House prices in')]"
    text_average_price = "//p[contains(text(),'The average sold price for a property in')]"
    text_info_average_price = "//p[contains(text(),'Different property types in')]"
    label_last_sold_within = "//label[text()='Last sold within']"
    dropdown_last_sold_within = "//label[text()='Last sold within']//following-sibling::button"
    label_property_type = "//label[text()='Property type']"
    dropdown_property_type = "//label[text()='Property type']//following-sibling::button"
    label_sort = "//label[text()='Sort']"
    dropdown_sort = "//label[text()='Sort']//following-sibling::button"
    list_result_list = "//ul[@data-testid='result-list']"
    list_result_names = "//ul[@data-testid='result-list']//li//div[@aria-disabled='false']//h2"


class house_prices_search_methods(PageInit, TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def validate_house_prices_search_page_elements(self):
        """
        This method validates all the elements displayed in House Prices search page
        (Currently limited to fields relevant to challenge)
        :return:
        """
        common_methods.wait_for_element(self.driver, house_prices_search_loc.button_house_prices_search)
        time.sleep(3)
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.header_house_prices_search).is_displayed(),
            "House prices search header is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.sub_header_house_prices_search).is_displayed(),
            "House prices search sub header is not displayed")
        text = self.driver.find_element(By.XPATH, house_prices_search_loc.sub_header_house_prices_search).text
        self.assertTrue("Enter a UK town or street name to get started." == text, "sub header text is in correct")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.label_search_area).is_displayed(),
            "Search area label is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.textbox_search_area).is_displayed(),
            "Street or pincode search textbox is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.button_house_prices_search).is_displayed(),
            "Search button is not displayed")

    def enter_area_postcode_and_hit_search(self, area_postcode):
        """
        This method will enter the area/postcode in house prices search based on test data
        :param area_postcode: Either area or postcode where search needs to be done
        :return: None
        """
        common_methods.wait_till_element_is_visible(self.driver, house_prices_search_loc.textbox_search_area)
        time.sleep(1)
        self.driver.find_element(By.XPATH, house_prices_search_loc.textbox_search_area).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, house_prices_search_loc.textbox_search_area).send_keys(area_postcode)
        time.sleep(2)
        self.driver.find_element(By.XPATH, house_prices_search_loc.textbox_search_area).send_keys(Keys.ENTER)
        time.sleep(2)

    def validate_house_price_search_result_elements(self):
        """
        This method will validate the house price search result screen elements
        :return: None
        """
        common_methods.wait_for_element(self.driver, house_prices_search_loc.list_result_list)
        self.assertTrue(
            self.driver.find_element(By.XPATH,
                                     house_prices_search_loc.header_house_prices_search_results).is_displayed(),
            "House prices results header is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.text_average_price).is_displayed(),
            "Search result page text info about average property prices not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.text_info_average_price).is_displayed(),
            "Search result page text info about different average property prices not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.label_last_sold_within).is_displayed(),
            "'Last sold within' label is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.dropdown_last_sold_within).is_displayed(),
            "'Last sold dropdown' label is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.label_property_type).is_displayed(),
            "'Property type' label is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.dropdown_property_type).is_displayed(),
            "'Property type' dropdown is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.label_sort).is_displayed(),
            "'Sort' label is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.dropdown_sort).is_displayed(),
            "'Sort' dropdown is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, house_prices_search_loc.list_result_list).is_displayed(),
            "Search results list is not displayed")

    def enter_price_search_criteria(self, last_sold_within, property_type, sort):
        """
        This method will enter criteria to search for house prices
        :param last_sold_within: Filter criteria for results
        :param property_type: Filter criteria for results
        :param sort: Filter criteria for results
        :return: None
        """
        time.sleep(2)
        common_methods.wait_till_element_is_visible(self.driver, house_prices_search_loc.dropdown_last_sold_within)
        self.driver.find_element(By.XPATH, house_prices_search_loc.dropdown_last_sold_within).click()
        common_methods.wait_till_element_is_visible(self.driver, f'//ul[@role="listbox"]//li[@role="option"]//div[contains(text(),"{last_sold_within}")]') # 3 months
        self.driver.find_element(By.XPATH, f'//ul[@role="listbox"]//li[@role="option"]//div[contains(text(),"{last_sold_within}")]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, house_prices_search_loc.dropdown_property_type).click()
        common_methods.wait_till_element_is_visible(self.driver, f'//ul[@role="listbox"]//li[@role="option"]//div[contains(text(),"{property_type}")]') # Any
        self.driver.find_element(By.XPATH, f'//ul[@role="listbox"]//li[@role="option"]//div[contains(text(),"{property_type}")]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, house_prices_search_loc.dropdown_sort).click()
        common_methods.wait_till_element_is_visible(self.driver, f'//ul[@role="listbox"]//li[@role="option"]//div[contains(text(),"{sort}")]') # Sold (newest - oldest)
        self.driver.find_element(By.XPATH, f'//ul[@role="listbox"]//li[@role="option"]//div[contains(text(),"{sort}")]').click()
        time.sleep(2)
        common_methods.wait_till_element_is_visible(self.driver, house_prices_search_loc.list_result_list)

    def validate_first_result(self, property_name):
        """
        This method will validate if the first search result matches with the property expected
        :param property_name: Name of the property expected in first search result
        :return: None
        """
        time.sleep(3)
        # property_name = "Flat 16, Radnor House, 1272 London Road, London, SW16 4EA"
        element = self.driver.find_elements(By.XPATH, house_prices_search_loc.list_result_names)[0]
        self.assertTrue(element.text == property_name, "First result doesnt match with expected property")



