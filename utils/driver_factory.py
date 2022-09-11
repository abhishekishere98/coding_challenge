from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as Services
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    @staticmethod
    def get_driver(config) -> webdriver:
        if config.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            return driver
        elif config.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
            return driver
        raise Exception("Please provide a valid \"driver\" name")


