import string

from playwright.async_api import Page
from unittest import TestCase

from playwright.sync_api import expect, Page, BrowserContext


class common_methods:
    wait_timeout = 30
    def __init__(self, df : tuple[BrowserContext,TestCase]):
        """
        Constructor for common methods class to initialise drive
        :param driver:
        """
        self.page = df[0]
        self.test = df[1]

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
                    elements_found = expect(Page.locator("xpath")).not_to_contain_text(element)
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
