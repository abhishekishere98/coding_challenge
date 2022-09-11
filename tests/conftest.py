import pytest
from webdriver_manager.core import driver

from utils.driver_factory import DriverFactory

driver = None


@pytest.fixture(autouse=True)
def setup(request):
    global driver
    browser_name = request.config.getoption("--selectbrowser")
    driver = DriverFactory.get_driver(browser_name)

    yield driver
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--selectbrowser", action="store")
