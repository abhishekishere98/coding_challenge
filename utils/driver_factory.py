from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    @staticmethod
    def get_driver(config) -> webdriver:
        if config.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
            return driver
        elif config.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
            return driver
        elif config.lower() == "chromium":
            chrome_options = webdriver.ChromeOptions()
            options = [
                "--headless",
                "--disable-gpu",
                "--window-size=1920,1200",
                "--ignore-certificate-errors",
                "--disable-extensions",
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
            for option in options:
                chrome_options.add_argument(option)
            driver = webdriver.Chrome(executable_path=ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=chrome_options)
            return driver
        raise Exception("Please provide a valid \"driver\" name")
