import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from base.page_initial import PageInit


class common_methods:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def wait_for_element(self, element):
        element_found = WebDriverWait(self.driver.driver, 5000, 500)\
            .until(EC.presence_of_element_located((By.XPATH, element)))
        return element_found

    def wait_till_element_is_visible(self, element):
        element_found = WebDriverWait(self.driver.driver, 5000, 500)\
            .until(EC.visibility_of_element_located((By.XPATH, element)))
        return element_found

    def wait_till_element_clickable(self, element):
        element_found = WebDriverWait(self.driver.driver, 5000, 500)\
            .until(EC.element_to_be_clickable((By.XPATH, element)))
        return element_found

    def wait_for_elements(self, element):
        elements_found = WebDriverWait(self.driver.driver, 5000, 500)\
            .until(EC.presence_of_all_elements_located((By.XPATH, element)))
        return elements_found

    def goto_url(self, goto_url: string):
        """
        This method will navigate the browser to user specified url
        :param goto_url: User specified url
        :return: None
        """
        self.driver.get(goto_url)

    def yield_driver(self):
        """
        This method will return the driver
        :return: None
        """
        return self.driver
