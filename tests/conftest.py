import pytest

from utils.driver_factory import DriverFactory


@pytest.fixture(autouse=True)
def setup(request):
    browser_name = request.config.getoption("browser")
    driver = DriverFactory.get_driver(browser_name)

    yield driver
    driver.close()
