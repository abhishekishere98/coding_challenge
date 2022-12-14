import pytest

from utils.driver_factory import DriverFactory


@pytest.fixture(autouse=True)
def setup(request):
    browser_name = request.config.getoption("--selectbrowser")
    driver = DriverFactory.get_driver(browser_name)

    yield driver
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--selectbrowser", action="store", default="chrome")
