import time

import pytest

from utils.driver_factory import DriverFactory
from selenium import webdriver
from unittest import TestCase


@pytest.fixture(autouse=True)
def setup(request) -> tuple[webdriver,TestCase]:
    browser_name = request.config.getoption("--selectbrowser")
    driver = DriverFactory.get_driver(browser_name)
    print("Browser value passed from command line: " + browser_name)
    test = TestCase()
    yield driver, test
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--selectbrowser", action="store", default="chrome")
