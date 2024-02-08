from selenium import webdriver
from selenium.webdriver.firefox.service import Service as GekoService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    @staticmethod
    def get_driver(config) -> webdriver:
        if config.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            return driver
        if config.lower() == "chromium":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options)
            return driver
        elif config.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(service=GekoService(GeckoDriverManager().install()), options=options)
            return driver
        raise Exception("Please provide a valid \"driver\" name")
