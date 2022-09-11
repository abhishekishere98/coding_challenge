from selenium import webdriver


class PageInit:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def open(self):
        self.driver.open()
