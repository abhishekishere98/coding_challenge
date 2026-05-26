from __future__ import annotations

import os
from pathlib import Path
from unittest import TestCase

import pytest
import allure
from playwright.sync_api import sync_playwright
from selenium import webdriver
from dotenv import load_dotenv

from utils.driver_factory import DriverFactory


ARTIFACTS_DIR = Path("Results")
SCREENSHOTS_DIR = ARTIFACTS_DIR / "screenshots"
load_dotenv()


@pytest.fixture()
def setup(request) -> tuple[webdriver, TestCase]:
    browser_name = request.config.getoption("--selectbrowser")
    headless = request.config.getoption("--headless")
    driver = DriverFactory.get_driver(browser_name, headless=headless)
    request.node._selenium_driver = driver
    print("Browser value passed from command line: " + browser_name)
    test = TestCase()
    yield driver, test
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--selectbrowser", action="store", default="chrome")
    parser.addoption("--headless", action="store_true", help="Run browser tests in headless mode")
    parser.addoption("--pw-slowmo", action="store", default=0, type=int, help="Playwright slow motion in milliseconds")


@pytest.fixture(scope="function")
def set_up(request):
    headless = request.config.getoption("--headless")
    slow_mo = request.config.getoption("--pw-slowmo")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless, slow_mo=slow_mo)
        page = browser.new_page()
        request.node._pw_page = page
        yield page
        page.close()
        browser.close()


@pytest.fixture(scope="function")
def page(request):
    headless = request.config.getoption("--headless")
    slow_mo = request.config.getoption("--pw-slowmo")
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless, slow_mo=slow_mo)
        context = browser.new_context(record_video_dir=str(ARTIFACTS_DIR / "videos"))
        page = context.new_page()
        request.node._pw_page = page
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope="session")
def zoopla_credentials():
    username = os.getenv("ZOOPLA_USERNAME")
    password = os.getenv("ZOOPLA_PASSWORD")
    if not username or not password:
        pytest.skip("Set ZOOPLA_USERNAME and ZOOPLA_PASSWORD to run authenticated Zoopla tests")
    return username, password


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return

    ARTIFACTS_DIR.mkdir(exist_ok=True)
    SCREENSHOTS_DIR.mkdir(exist_ok=True)
    screenshot_name = f"{item.name}.png"

    driver = getattr(item, "_selenium_driver", None)
    if driver is not None:
        screenshot_path = SCREENSHOTS_DIR / f"selenium_{screenshot_name}"
        driver.save_screenshot(str(screenshot_path))
        allure.attach.file(
            str(screenshot_path),
            name=f"selenium_{item.name}",
            attachment_type=allure.attachment_type.PNG,
        )

    pw_page = getattr(item, "_pw_page", None)
    if pw_page is not None:
        screenshot_path = SCREENSHOTS_DIR / f"playwright_{screenshot_name}"
        pw_page.screenshot(path=str(screenshot_path), full_page=True)
        allure.attach.file(
            str(screenshot_path),
            name=f"playwright_{item.name}",
            attachment_type=allure.attachment_type.PNG,
        )
