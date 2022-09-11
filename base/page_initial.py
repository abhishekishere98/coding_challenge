from extentions.webdrivers_extnd import WebDriverExtended


class PageInit:
    def __init__(self, driver: WebDriverExtended):
        self.driver = driver

    def open(self):
        self.driver.open()
