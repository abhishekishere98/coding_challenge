import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from unittest import TestCase

class common_methods:
    wait_timeout = 30
    def __init__(self, df : tuple[webdriver,TestCase]):
        """
        Constructor for common methods class to initialise drive
        :param driver:
        """
        self.driver = df[0]
        self.test = df [1]

    
    def wd_wait(self) -> WebDriverWait:
        """
        Create webdriver wait object
        :return: WebDriverWait object
        """
        wait = WebDriverWait(self.driver, self.wait_timeout)
        return wait

    def wait_for_element(self, element) -> WebElement:
        try:
            element_found = self.wd_wait().until(EC.presence_of_element_located((By.XPATH, element)))
            return element_found
        except Exception as ex:
            self.test.fail("Element with 'XPATH' -> '"+element+"' not found" + "\n Exception : \n"+str(ex))

    def wait_till_element_is_visible(self, element) -> WebElement:
        try:
            element_found = self.wd_wait().until(EC.visibility_of_element_located((By.XPATH, element)))
            return element_found
        except Exception as ex:
            self.test.fail("Element with 'XPATH' -> '"+element+"' not visible" + "\n Exception : \n"+str(ex))

    def wait_till_element_clickable(self, element) -> WebElement:
        try:
            element_found = self.wd_wait().until(EC.element_to_be_clickable((By.XPATH, element)))
            return element_found
        except Exception as ex:
            self.test.fail("Element with 'XPATH' -> '"+element+"' not clickable" + "\n Exception : \n"+str(ex))

    def wait_for_elements(self, element) -> list[WebElement]:
        try:
            elements_found = self.wd_wait().until(EC.presence_of_all_elements_located((By.XPATH, element)))
            return elements_found
        except Exception as ex:
            self.test.fail("Elements with 'XPATH' -> '"+element+"' not found" + "\n Exception : \n"+str(ex))

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
                try:
                    elements_found = self.wd_wait().until(EC.presence_of_element_located((By.XPATH, element)))
                    return elements_found
                except Exception as ex:
                    self.test.fail("Elements with 'XPATH' -> '" + element + "' not found" + "\n Exception : \n"+str(ex))
            # Find element by Name
            case "NAME":
                try:
                    elements_found = self.wd_wait().until(EC.presence_of_element_located((By.NAME, element)))
                    return elements_found
                except Exception as ex:
                    self.test.fail("Elements with 'Name' -> '" + element + "' not found" + "\n Exception : \n"+str(ex))
            # Find element by ID
            case "ID":
                try:
                    elements_found = self.wd_wait().until(EC.presence_of_element_located((By.ID, element)))
                    return elements_found
                except Exception as ex:
                    self.test.fail("Elements with 'ID' -> '" + element + "' not found" + "\n Exception : \n"+str(ex))
            # Find element by CSS
            case "CSS":
                try:
                    elements_found = self.wd_wait().until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
                    return elements_found
                except Exception as ex:
                    self.test.fail("Elements with 'CSS' -> '" + element + "' not found" + "\n Exception : \n"+str(ex))
            # Find element by Class
            case "CLASS":
                try:
                    elements_found = self.wd_wait().until(EC.presence_of_element_located((By.CLASS_NAME, element)))
                    return elements_found
                except Exception as ex:
                    self.test.fail("Elements with 'Class' -> '" + element + "' not found" + "\n Exception : \n"+str(ex))
            # Find element by Link Text
            case "LINK TEXT":
                try:
                    elements_found = self.wd_wait().until(EC.presence_of_element_located((By.LINK_TEXT, element)))
                    return elements_found
                except Exception as ex:
                    self.test.fail("Elements with 'Link Text' -> '" + element + "' not found" + "\n Exception : \n"+str(ex))
            # Find element by Partial Link Test
            case "PARTIAL LINK TEXT":
                try:
                    elements_found = self.wd_wait().until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element)))
                    return elements_found
                except Exception as ex:
                    self.test.fail("Elements with 'Partial Link Test' -> '" + element + "' not found" + "\n Exception : \n"+str(ex))
            # Find element by TAG
            case "TAG":
                try:
                    elements_found = self.wd_wait().until(EC.presence_of_element_located((By.TAG_NAME, element)))
                    return elements_found
                except Exception as ex:
                    self.test.fail("Elements with 'Tag' -> '" + element + "' not found" + "\n Exception : \n"+str(ex))

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

    def yield_driver(self) -> tuple[WebDriver, TestCase]:
        """
        This method will return the driver
        :return: None
        """
        return self.driver, self.test
