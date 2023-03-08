from unittest import TestCase

from utils.common_methods import common_methods
from PIL import Image

class landing_page_locs:
    page_main_heading = '//div[@class="login_logo"]'
    tb_username = '//input[@id="user-name"]'
    tb_password = '//input[@id="password"]'
    btn_submit = '//input[@id="login-button"]'
    txt_user_names = '//div[@id="login_credentials"]'
    txt_password = '//div[@class="login_password"]'


class sauce_labs_landing_page(common_methods, TestCase):
    usernames = []
    def saucelab_landing_page_elements_verification(self):
        """
        Method to verify all landing page elements in sauce labs landing page
        :return: None
        """
        self.assertTrue(self.wait_till_element_is_visible(landing_page_locs.page_main_heading).is_displayed(),
                        "Page Logo is visible")
        self.assertTrue(self.wait_till_element_is_visible(landing_page_locs.tb_username).is_displayed(),
                        "Username textbox is displayed")
        self.assertTrue(self.wait_till_element_is_visible(landing_page_locs.tb_password).is_displayed(),
                        "Password textbox is displayed")
        self.assertTrue(self.wait_till_element_is_visible(landing_page_locs.btn_submit).is_displayed(),
                        "Submit button is displayed")
        self.assertTrue(self.wait_for_elements(landing_page_locs.txt_user_names).__len__() != 0,
                        "List of usernames is displayed")
        self.assertTrue(self.wait_till_element_is_visible(landing_page_locs.txt_password).is_displayed(),
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
        self.wait_till_element_clickable(landing_page_locs.tb_username)
        self.wait_for_element(landing_page_locs.tb_username).send_keys(self.usernames[1])
        self.wait_for_element(landing_page_locs.tb_password).send_keys(self.password[1])
        self.wait_for_element(landing_page_locs.btn_submit).click()
        self.driver.driver.save_screenshot('//Results//ss.png')
        # screenshot = Image.open('/Results/ss.png')
        # screenshot.show()

