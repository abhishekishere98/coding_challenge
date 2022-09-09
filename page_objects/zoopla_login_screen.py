import time
from unittest import TestCase

from selenium.webdriver.common.by import By

from base.page_initial import PageInit
from utils.common_methods import common_methods


class zoopla_sign_in_locs:
    zoopla_logo = '//a[@data-testid = "sign-in-page-logo-link"]'


class zoopla_landing_methods(PageInit, TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def validate_login_page_elements(self):
        """

        :return:
        """
