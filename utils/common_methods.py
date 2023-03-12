import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from base.page_initial import PageInit


class common_methods:
    def __init__(self, driver: webdriver):
        """
        Constructor for common methods class to initialise driver
        :param driver:
        """
        self.driver = driver

    def wait_for_element(self, element) -> WebElement:
        element_found = WebDriverWait(self.driver.driver, 5000, 500) \
            .until(EC.presence_of_element_located((By.XPATH, element)))
        return element_found

    def wait_till_element_is_visible(self, element) -> WebElement:
        element_found = WebDriverWait(self.driver.driver, 5000, 500) \
            .until(EC.visibility_of_element_located((By.XPATH, element)))
        return element_found

    def wait_till_element_clickable(self, element) -> WebElement:
        element_found = WebDriverWait(self.driver.driver, 5000, 500) \
            .until(EC.element_to_be_clickable((By.XPATH, element)))
        return element_found

    def wait_for_elements(self, element) -> list[WebElement]:
        elements_found = WebDriverWait(self.driver.driver, 5000, 500) \
            .until(EC.presence_of_all_elements_located((By.XPATH, element)))
        return elements_found

    def find_element(self, identifier: string, element: string) -> WebElement:
        """

        :param identifier: Mention the identifier type to be used, Valid Values : XPATH, NAME, ID, CSS, CLASS, LINK TEXT,
        PARTIAL LINK TEXT, TAG
        :param element: Valid identifier value like a xpath or element name
        :return: Returns the web element if found
        """
        # Identify element based on identifier type and identifier provided
        match identifier.upper():
            # Find element by XPATH
            case "XPATH":
                elements_found = WebDriverWait(self.driver.driver, 5000, 500) \
                    .until(EC.presence_of_element_located((By.XPATH, element)))
                return elements_found
            # Find element by Name
            case "NAME":
                elements_found = WebDriverWait(self.driver.driver, 5000, 500) \
                    .until(EC.presence_of_element_located((By.NAME, element)))
                return elements_found
            # Find element by ID
            case "ID":
                elements_found = WebDriverWait(self.driver.driver, 5000, 500) \
                    .until(EC.presence_of_element_located((By.ID, element)))
                return elements_found
            # Find element by CSS
            case "CSS":
                elements_found = WebDriverWait(self.driver.driver, 5000, 500) \
                    .until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
                return elements_found
            # Find element by Class
            case "CLASS":
                elements_found = WebDriverWait(self.driver.driver, 5000, 500) \
                    .until(EC.presence_of_element_located((By.CLASS_NAME, element)))
                return elements_found
            # Find element by Link Text
            case "LINK TEXT":
                elements_found = WebDriverWait(self.driver.driver, 5000, 500) \
                    .until(EC.presence_of_element_located((By.LINK_TEXT, element)))
                return elements_found
            # Find element by Partial Link Test
            case "PARTIAL LINK TEXT":
                elements_found = WebDriverWait(self.driver.driver, 5000, 500) \
                    .until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element)))
                return elements_found
            # Find element by TAG
            case "TAG":
                elements_found = WebDriverWait(self.driver.driver, 5000, 500) \
                    .until(EC.presence_of_element_located((By.TAG_NAME, element)))
                return elements_found

    def get_text_from_element(self, element: WebElement) -> string:
        """
        Methods returns text from a web element
        :param element: The web element from which text is needed
        :return: Text value from web element
        """
        if element.text is not None or element.text != "":
            return element.text
        elif self.get_text_from_element(element) is not None or self.get_text_from_element(element) != "":
            return self.get_text_from_element(element)



    def goto_url(self, goto_url: string):
        """
        This method will navigate the browser to user specified url
        :param goto_url: User specified url
        :return: None
        """
        self.driver.get(goto_url)

    def yield_driver(self) -> WebDriver:
        """
        This method will return the driver
        :return: None
        """
        return self.driver
