from selenium import webdriver


class PageInit:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def open(self):
        self.driver.open()

    def yield_driver(self):
        """
        This method will return the driver
        :return: driver
        """
        return self.driver
