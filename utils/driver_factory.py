from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from extentions.webdrivers_extnd import WebDriverExtended
from utils.webdriver_listeners import WebDriverListener


class DriverFactory:
    @staticmethod
    def get_driver(config) -> WebDriverExtended:
        if config["browser"].lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            if config["headless_mode"] is True:
                options.add_argument("--headless")
            driver = WebDriverExtended(
                webdriver.Chrome(ChromeDriverManager().install(), options=options),
                WebDriverListener(), config
            )
            return driver
        elif config["browser"].lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if config["headless_mode"] is True:
                options.headless = True
            driver = WebDriverExtended(
                webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options),
                WebDriverListener(), config
            )
            return driver
        else:
            if config["browser"].lower() == "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument("start-maximized")
                if config["headless_mode"] is True:
                    options.add_argument("--headless")
                driver = WebDriverExtended(
                    webdriver.Chrome(ChromeDriverManager().install(), options=options),
                    WebDriverListener(), config
                )
                return driver
        raise Exception("Please provide a valid \"driver\" name")
