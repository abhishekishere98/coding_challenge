import logging
import time

import allure
from unittest import TestCase
from selenium.webdriver.common.by import By

from base.page_initial import PageInit


class zoopla_landing_locs:
    zoopla_logo = (By.XPATH, '//a[@data-testid="zoopla-logo"]')
    zoopla_naviagtion_links = (By.XPATH, '//nav[@data-testid="header"]//li//a')
    zoopla_slogan = (By.XPATH, '//main[@id="main-content"]//h1//preceding-sibling::p[contains(text(), "We know")]')
    zoopla_info_text = (By.XPATH, '//main[@id="main-content"]//h1[contains(text(),"Find homes")].')
    zoopla_search_tabs = (By.XPATH, '//div[@role="tablist"]//button')
    zoopla_search_text_box = (By.XPATH, '//form[@role="search"]//input')
    icon_search_search_button = (By.XPATH, '(//button[@data-testid="search-btn"]//child::div[@aria-hidden="true"]//attribute::*)[4]')
    text_search_button = (By.XPATH, '//button[@data-testid="search-btn"]//div[contains(text(),"Search")]')
    button_search = (By.XPATH,'//button[@data-testid="search-btn"]')


class zoopla_landing_methods(PageInit, TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Expanding account menu")
    def goto_zoopla_home_page(self, url):
        """
        This method will navigate the browser to user specified url
        :param url: User specified url
        :return: None
        """
        self.driver.get(url)

    @allure.step("Expanding account menu")
    def validate_landing_screen_elements(self):
        """
        This method will validate ui elements of Zoopl landing page
        :return: None
        """

        self.assertTrue(self.driver.find_element(zoopla_landing_locs.zoopla_logo).is_displayed(),
                        "Company Logo not displayed")
        self.assertTrue(self.driver.find_element(zoopla_landing_locs.zoopla_slogan).is_displayed(),
                        "Company slogan is not displayed")
        self.assertTrue(self.driver.find_element(zoopla_landing_locs.zoopla_info_text).is_displayed(),
                        "Info text is not displayed")
        nav_list = self.driver.find_elements(zoopla_landing_locs.zoopla_naviagtion_links)
        name_nav = []
        for ele in nav_list:
            if ele.is_displayed():
                name_nav.append(ele.text)
            else:
                pass
        expected_nav = ["For sale", "To rent", "House prices", "Agent valuation", "instant valuation", "My Home",
                        "Saved", "Sign in"]
        self.assertListEqual(nav_list, expected_nav, f"Displayed Nav menu has incorrect text : {nav_list}")
        tab_list = self.driver.find_elements(zoopla_landing_locs.zoopla_search_tabs)
        name_tab = []
        for ele in tab_list:
            if ele.is_displayed():
                name_tab.append(ele.text)
            else:
                pass
        expected_tab = ["For sale", "To rent", "House prices"]
        self.assertListEqual(nav_list, expected_nav, f"Displayed Nav menu has incorrect text : {name_tab}")
        self.assertTrue(self.driver.find_element(zoopla_landing_locs.icon_search_search_button).is_displayed(),
                        "Search icon is not displayed in search box")
        self.assertTrue(self.driver.find_element(zoopla_landing_locs.text_search_button).is_displayed(),
                        "Search button text is not displayed")
        self.assertTrue(self.driver.find_element(zoopla_landing_locs.button_search).is_displayed(),
                        "Search button is not displayed")
        self.assertTrue(self.driver.find_element(zoopla_landing_locs.button_search).is_enabled(),
                        "Search button is not enabled")
        self.assertTrue(self.driver.find_element(zoopla_landing_locs.zoopla_search_text_box).is_displayed(),
                        "Search textbox is not displayed")
        self.assertTrue(self.driver.find_element(zoopla_landing_locs.zoopla_search_text_box).is_enabled(),
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
