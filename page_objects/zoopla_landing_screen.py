import time
from unittest import TestCase

from selenium.webdriver.common.by import By

from base.page_initial import PageInit
from utils.common_methods import common_methods


class zoopla_landing_locs:
    zoopla_logo = '//a[@data-testid="zoopla-logo"]'
    zoopla_naviagtion_links = '//nav[@data-testid="header"]//li//a'
    zoopla_slogan = '//main[@id="main-content"]//h1//preceding-sibling::p[contains(text(), "We know")]'
    zoopla_info_text = '//main[@id="main-content"]//h1[contains(text(),"Find homes")]'
    zoopla_search_tabs = '//div[@role="tablist"]//button'
    zoopla_search_text_box = '//form[@role="search"]//input'
    button_search = '//button[@data-testid="search-btn"]'


class zoopla_landing_methods(PageInit):
    def __init__(self, driver, comm):
        super().__init__(driver)

    def goto_zoopla_home_page(self, url):
        """
        This method will navigate the browser to user specified url
        :param url: User specified url
        :return: None
        """
        self.driver.get(url)
        expected_url = "https://www.zoopla.co.uk/"
        # self.driver.

    def validate_landing_screen_elements(self):
        """
        This method will validate ui elements of Zoopl landing page
        :return: None
        """
        comm
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_landing_locs.zoopla_logo).is_displayed(),
                        "Company Logo not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_landing_locs.zoopla_slogan).is_displayed(),
                        "Company slogan is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_landing_locs.zoopla_info_text).is_displayed(),
                        "Info text is not displayed")
        nav_list = self.driver.find_elements(By.XPATH, zoopla_landing_locs.zoopla_naviagtion_links)
        name_nav = []
        for ele in nav_list:
            if ele.is_displayed():
                name_nav.append(ele.text)
            else:
                pass
        expected_nav = ["For sale", "To rent", "House prices", "Agent valuation", "Instant valuation", "My Home",
                        "Saved", "Sign in"]
        self.assertListEqual(name_nav, expected_nav, f"Displayed Nav menu has incorrect text : {nav_list}")
        tab_list = self.driver.find_elements(By.XPATH, zoopla_landing_locs.zoopla_search_tabs)
        name_tab = []
        for ele in tab_list:
            if ele.is_displayed():
                name_tab.append(ele.text)
            else:
                pass
        expected_tab = ["For sale", "To rent", "House prices"]
        self.assertListEqual(name_tab, expected_tab, f"Displayed Nav menu has incorrect text : {name_tab}")
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_landing_locs.button_search).is_displayed(),
                        "Search button is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_landing_locs.button_search).is_enabled(),
                        "Search button is not enabled")
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_landing_locs.zoopla_search_text_box).is_displayed(),
                        "Search textbox is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_landing_locs.zoopla_search_text_box).is_enabled(),
                        "Search textbox is not enabled")

    def enter_text_zoopla_landing_search_textbox(self, search_string):
        """
        This method will enter required string into search box
        :param search_string: User entered string to be searched
        :return: None
        """
        time.sleep(1)
        self.driver.find_element(zoopla_landing_locs.zoopla_search_text_box).send_keys(search_string)
        time.sleep(1)

    def click_search_button(self):
        """
        This method will click on search button to trigger search
        :return: None
        """
        self.driver.find_element(zoopla_landing_locs.button_search).click()
        time.sleep(3)

    def check_current_page_is_search_result(self):
        """
        This method will click on check if current page is search results
        :return:
        """

    def click_to_rent_nav_link(self):
        """
        This method will click on To rent nav link
        :return: None
        """
        self.driver.find_elements(zoopla_landing_locs.zoopla_naviagtion_links)[1].click()
        time.sleep(3)
        return self.driver




