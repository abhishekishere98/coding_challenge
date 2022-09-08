import allure
from selenium.webdriver.common.by import By

from base.page_initial import PageInit


class zoopla_landing_locs:
    lang_menu = (By.XPATH, "//a[@id='dropdownLangauge']")


class zoopla_landing_methods(PageInit):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Expanding account menu")
    def goto_zoopla_home_page(self, url):
        self.driver.get(url)

    @allure.step("Expanding account menu")
    def validate_landing_screen_elements(self):
        abc = ""
