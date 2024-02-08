from unittest import TestCase

from utils.common_methods import common_methods


class landing_page_locs:
    page_main_heading = '//div[@class="login_logo"]'
    tb_username = '//input[@id="user-name"]'
    tb_password = '//input[@id="password"]'
    btn_submit = '//input[@id="login-button"]'
    txt_user_names = '//div[@id="login_credentials"]'
    txt_password = '//div[@class="login_password"]'
    header_swag_labs = '//div[@class="header_label"]//div[@class="app_logo" and text()="Swag Labs"]'
    text_error_msg = '//div//h3[@data-test="error"]'
    btn_clear_error = '//h3//button[@class="error-button"]'


class sauce_labs_landing_page(common_methods):
    usernames = []
    LockedOutUserErrorMsg = "Epic sadface: Sorry, this user has been locked out."

    def saucelab_landing_page_elements_verification(self):
        """
        Method to verify all landing page elements in sauce labs landing page
        :return: None
        """
        self.test.assertTrue(self.wait_till_element_is_visible(landing_page_locs.page_main_heading).is_displayed(),
                             "Page Logo is visible")
        self.test.assertTrue(self.wait_till_element_is_visible(landing_page_locs.tb_username).is_displayed(),
                             "Username textbox is displayed")
        self.test.assertTrue(self.wait_till_element_is_visible(landing_page_locs.tb_password).is_displayed(),
                             "Password textbox is displayed")
        self.test.assertTrue(self.wait_till_element_is_visible(landing_page_locs.btn_submit).is_displayed(),
                             "Submit button is displayed")
        self.test.assertTrue(self.wait_for_elements(landing_page_locs.txt_user_names).__len__() != 0,
                             "List of usernames is displayed")
        self.test.assertTrue(self.wait_till_element_is_visible(landing_page_locs.txt_password).is_displayed(),
                             "password text is displayed")

    def fetch_login_credentials(self):
        """
        Method to fetch login credentials and store them in dictionary
        :return: Dictionary with usernames
        """
        self.usernames = self.wait_for_element(landing_page_locs.txt_user_names).text.split("\n")
        self.password = self.wait_for_element(landing_page_locs.txt_password).text.split("\n")

    def saucelab_login_success(self):
        """
        Method to enter credentials and login to saucelab website successfully
        :return: None
        """
        # Wait for page to load
        self.wait_till_element_clickable(landing_page_locs.tb_username)
        # Enter Username
        self.wait_for_element(landing_page_locs.tb_username).send_keys(self.usernames[1])
        # Enter Password
        self.wait_for_element(landing_page_locs.tb_password).send_keys(self.password[1])
        # Click on Login Button
        self.wait_for_element(landing_page_locs.btn_submit).click()
        # Check login is Successful
        self.test.assertTrue(self.wait_for_element(landing_page_locs.header_swag_labs).is_displayed(),
                             "User is successfully logged in and Swag Labs header is displayed")

    def saucelab_login_Locked_out_user(self):
        """
        Method to check if a locked out user is prevented from logging in with appropriate error message
        :return: None
        """
        # Wait for page to load
        self.wait_till_element_clickable(landing_page_locs.tb_username)
        # Enter Username
        self.wait_for_element(landing_page_locs.tb_username).send_keys(self.usernames[2])
        # Enter Password
        self.wait_for_element(landing_page_locs.tb_password).send_keys(self.password[1])
        # Click on Login Button
        self.wait_for_element(landing_page_locs.btn_submit).click()
        # Check login not Successful
        self.test.assertTrue(self.wait_till_element_is_visible(landing_page_locs.text_error_msg).is_displayed(),
                             "User is not logged in and appropriate error message is displayed")
        # Check correct error text is displayed
        self.test.assertTrue(self.wait_till_element_is_visible(landing_page_locs.text_error_msg).text ==
                             sauce_labs_landing_page.LockedOutUserErrorMsg,
                             "Correct error message is displayed when user is locked out")

    def saucelab_login_success_problem(self):
        """
        Method to enter credentials and login to saucelab website successfully
        :return: None
        """
        # Wait for page to load
        self.wait_till_element_clickable(landing_page_locs.tb_username)
        # Enter Username
        self.wait_for_element(landing_page_locs.tb_username).send_keys(self.usernames[3])
        # Enter Password
        self.wait_for_element(landing_page_locs.tb_password).send_keys(self.password[1])
        # Click on Login Button
        self.wait_for_element(landing_page_locs.btn_submit).click()
        # Check login is Successful with problem user
        self.test.assertTrue(self.wait_for_element(landing_page_locs.header_swag_labs).is_displayed(),
                             "User is successfully logged in and Swag Labs header is displayed")

    def saucelab_login_success_slow_user(self):
        """
        Method to enter credentials and login to saucelab website successfully
        :return: None
        """
        # Wait for page to load
        self.wait_till_element_clickable(landing_page_locs.tb_username)
        # Enter Username
        self.wait_for_element(landing_page_locs.tb_username).send_keys(self.usernames[4])
        # Enter Password
        self.wait_for_element(landing_page_locs.tb_password).send_keys(self.password[1])
        # Click on Login Button
        self.wait_for_element(landing_page_locs.btn_submit).click()
        # Check login is Successful with problem user
        self.test.assertTrue(self.wait_for_element(landing_page_locs.header_swag_labs).is_displayed(),
                             "User is successfully logged in and Swag Labs header is displayed")
