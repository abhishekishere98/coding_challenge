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
    button_sign_in = '//ul//li//a[text()="Sign in"]'
    button_saved = '//a[normalize-space()="Saved"]'
    button_account = '//a[normalize-space()="Account"]'
    link_saved_searches = '//a[normalize-space()="Searches and alerts"]'



class zoopla_landing_methods(PageInit, TestCase):
    def __init__(self, driver):
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
        common_methods.wait_for_element(self.driver, zoopla_landing_locs.zoopla_logo)
        time.sleep(3)
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_landing_locs.zoopla_logo).is_displayed(),
                        "Company Logo not displayed")
        nav_list = self.driver.find_elements(By.XPATH, zoopla_landing_locs.zoopla_naviagtion_links)
        name_nav = []
        for ele in nav_list:
            if ele.is_displayed():
                name_nav.append(ele.text)
            else:
                pass
        expected_nav = ["For sale", "To rent", "House prices", "Agent valuation", "Instant valuation", "My Home", "Saved", "Sign in"]
        self.assertListEqual(name_nav, expected_nav, f"Displayed Navigation menu has incorrect text : {name_nav}")
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

    def click_to_rent_nav_link(self):
        """
        This method will click on To rent navigation link
        :return: None
        """
        common_methods.wait_for_elements(self.driver, zoopla_landing_locs.zoopla_naviagtion_links)
        self.driver.find_elements(By.XPATH, zoopla_landing_locs.zoopla_naviagtion_links)[1].click()
        time.sleep(3)

    def click_house_prices_nav_link(self):
        """
        This method will click on To rent navigation link
        :return: None
        """
        common_methods.wait_for_elements(self.driver, zoopla_landing_locs.zoopla_naviagtion_links)
        self.driver.find_elements(By.XPATH, zoopla_landing_locs.zoopla_naviagtion_links)[2].click()
        time.sleep(3)

    def click_for_sale_nav_link(self):
        """
        This method will click on To rent navigation link
        :return: None
        """
        common_methods.wait_for_elements(self.driver, zoopla_landing_locs.zoopla_naviagtion_links)
        self.driver.find_elements(By.XPATH, zoopla_landing_locs.zoopla_naviagtion_links)[0].click()
        time.sleep(3)

    def click_sign_in_nav_link(self):
        """
        This method will click on To rent navigation link
        :return: None
        """
        common_methods.wait_for_element(self.driver, zoopla_landing_locs.button_sign_in)
        self.driver.find_element(By.XPATH, zoopla_landing_locs.button_sign_in).click()
        time.sleep(3)

    def click_account_nav_link(self):
        """
        This method will click on To rent navigation link
        :return: None
        """
        common_methods.wait_for_element(self.driver, zoopla_landing_locs.button_account)
        self.driver.find_element(By.XPATH, zoopla_landing_locs.button_account).click()
        time.sleep(3)

    def navigate_to_saved_searches(self):
        """
        This method will navigate user from landing page till saved searches page
        :return: None
        """
        common_methods.wait_till_element_clickable(self.driver, zoopla_landing_locs.link_saved_searches)
        self.driver.find_element(By.XPATH, zoopla_landing_locs.link_saved_searches).click()

    def yield_driver(self):
        """
        This method will return the driver
        :return: None
        """
        return self.driver
