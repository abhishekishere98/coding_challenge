import time
from unittest import TestCase

from selenium.webdriver.common.by import By

from base.page_initial import PageInit
from utils.common_methods import common_methods


class zoopla_sign_in_locs:
    """
    This Class will store all locators for Zoopla login screen
    """
    zoopla_logo = "//a[@title='Return to zoopla home page']"
    heading_sign_in = "//h1[normalize-space()='Sign in to save properties and much more']"
    label_email = "//label[normalize-space()='Email address']"
    label_password = "//label[normalize-space()='Password']"
    textbox_email = "//input[@id='email']"
    textbox_password = "//input[@id='password']"
    button_signin = "//button[normalize-space()='Sign in']"


class zoopla_login_methods(PageInit, TestCase):
    """
    This class is to bind the methods and locators of Zoopla Login page together, by implementing execution
    steps related to this page within this file. It implements PageInit and Testcase classes to support webdriver and
    Junit assertions
    """
    def __init__(self, driver):
        """
        This is constructor for page object which will initialise the driver
        :param driver: webdriver instance to perform required actions
        """
        super().__init__(driver)

    def validate_login_page_elements(self):
        """
        This method will validate the login page elements
        :return:None
        """
        # Wait for page load
        common_methods.wait_for_element(self.driver, zoopla_sign_in_locs.zoopla_logo)
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_sign_in_locs.zoopla_logo).is_displayed(),
                        "Zoopla logo is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_sign_in_locs.heading_sign_in).is_displayed(),
                        "Sign in heading is not displayed")
        # Heading
        heading = self.driver.find_element(By.XPATH, zoopla_sign_in_locs.heading_sign_in).text
        expected_heading = "Sign in to save properties and much more"
        self.assertTrue(heading == expected_heading, "Heading text is incorrect")
        # Email
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_sign_in_locs.label_email).is_displayed(),
                        "Email label is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_sign_in_locs.textbox_email).is_displayed(),
                        "Email textbox is not displayed")
        # Password
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_sign_in_locs.label_password).is_displayed(),
                        "Password label is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_sign_in_locs.textbox_password).is_displayed(),
                        "Password textbox is not displayed")
        # Sign In button
        self.assertTrue(self.driver.find_element(By.XPATH, zoopla_sign_in_locs.button_signin).is_displayed(),
                        "Sign in button is not displayed")

    def enter_login_info_click_sign_in(self, username: str, password: str):
        """
        This Method will enter username and password and click on Sign in
        :param username: Username
        :param password: Password
        :return: None
        """
        # Enter username
        self.driver.find_element(By.XPATH, zoopla_sign_in_locs.textbox_email).click()
        self.driver.find_element(By.XPATH, zoopla_sign_in_locs.textbox_email).send_keys(username)
        time.sleep(2)
        # Enter password
        self.driver.find_element(By.XPATH, zoopla_sign_in_locs.textbox_password).click()
        self.driver.find_element(By.XPATH, zoopla_sign_in_locs.textbox_password).send_keys(password)
        time.sleep(2)
        # Click sign in
        self.driver.find_element(By.XPATH, zoopla_sign_in_locs.button_signin).click()
        time.sleep(4)

