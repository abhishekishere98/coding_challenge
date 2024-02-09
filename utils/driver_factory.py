from typing import Generator

from playwright.async_api import Playwright
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as GekoService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from webdriver_manager.firefox import GeckoDriverManager

from playwright.sync_api import Page, BrowserContext


class DriverFactory:
    @staticmethod
    def get_driver(config) -> webdriver:
        if config.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()), options=options)
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

    @staticmethod
    def get_page(config, my_page: Playwright) -> [None, None, BrowserContext]:
        if config.lower() == "chrome" or config.lower() == "chromium":
            context = my_page.chromium.launch_persistent_context(
                "",
                headless=False,
                args=[],
            )
            return context
        elif config.lower() == "firefox":
            if config.lower() == "chrome" or config.lower() == "chromium":
                context = my_page.firefox.launch_persistent_context(
                    "",
                    headless=False,
                    args=[],
                )
                return context
        raise Exception("Please provide a valid \"driver\" name")