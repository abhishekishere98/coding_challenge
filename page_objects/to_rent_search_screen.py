import time
from unittest import TestCase

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.page_initial import PageInit
from utils.common_methods import common_methods


class to_rent_search_screen_locs:
    header_to_rent_page = '//div[@id="main-content"]//h1[contains(text(),"Properties to rent")]'
    sub_header_to_rent_page = '//div[@id="main-content"]//p[contains(text(),"Search houses")]'
    label_search_area = '//label[text()="Search area"]'
    combobox_search_area = '//input[@placeholder="e.g. Oxford or NW3"]'
    label_bedrooms = '//label[text()="Bedrooms"]'
    dropdown_bedrooms = '//div[text()="Any beds"]//parent::button'
    label_max_price = '//label[text()="Max price"]'
    dropdown_max_price = '//div[text()="No max"]//parent::button'
    label_property_type = '//label[text()="Property type"]'
    radio_button_show_all = '//div[@role="radiogroup"]//button[@role="radio" and @value="show all"]'
    radio_button_houses = '//div[@role="radiogroup"]//button[@role="radio" and @value="houses"]'
    radio_button_flats = '//div[@role="radiogroup"]//button[@role="radio" and @value="flats"]'
    labels_radio_buttons = '//button[@role="radio"]//following-sibling::div//label'
    button_search = '//button[@data-testid="search-btn"]'
    # Search result section
    search_result_header = '//div[@data-testid="search-desktop-subheader"]'
    dropdown_search_radius_search_filter = '//div[@data-testid="search-desktop-subheader"]//select[@id="desktop_radius-filter"]'
    dropdown_bedrooms_search_filter = '//div[@data-testid="search-desktop-subheader"]//button[@label="Bedrooms"]'
    dropdown_price_range_search_filter = '//div[@data-testid="search-desktop-subheader"]//button[@label="Price range"]'
    dropdown_property_type_search_filter = '//div[@data-testid="search-desktop-subheader"]//button[@label="Property type"]'
    button_search_filter = '//button[@data-testid="search-button"]'
    button_create_email_alert = '//button//div[contains(text(), "Create email alert")]'
    dropdown_price_range_min = '//select[@data-testid="min_price"]'
    link_travel_time_search = '//aside[@data-testid="search-sidebar"]//a[contains(text(),"Travel time search")]'
    button_save_search = '//button[text()="Save your search and alert"]'
    dropdown_alert_frequency = '//select[@id="alert_frequency"]'
    msg_success_search_saved = '//h2[contains(text(),"Success! Your search")]'
    link_manage_my_saved_searches = '//a[text()="Manage my saved searches"]//parent::div'


class to_rent_search_screen_methods(PageInit, TestCase):
    def __init__(self, driver):
        super().__init__(driver)

    def validate_to_rent_search_screen_elements(self):
        """
        This method will click on check if current page is search results
        :return: None
        """
        common_methods.wait_for_element(self.driver, to_rent_search_screen_locs.header_to_rent_page)
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.header_to_rent_page).is_displayed(),
            "To rent search page header is not displayed")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.sub_header_to_rent_page).is_displayed(),
            "To rent search page header is not displayed")
        sub_header = self.driver.find_element(By.XPATH, to_rent_search_screen_locs.sub_header_to_rent_page).text
        exp_sub_header = "Search houses and flats to rent across the UK"
        self.assertTrue(exp_sub_header == sub_header, "Incorrect sub-header displayed in To rent search page")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.label_search_area).is_displayed(),
                        "'Search area' label is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.combobox_search_area).is_displayed(),
            "'Search area' text input field is not displayed ")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.label_bedrooms).is_displayed(),
                        "'Bedrooms' label is not displayed ")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_bedrooms).is_displayed(),
                        "'Bedrooms' dropdown is not displayed ")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.label_max_price).is_displayed(),
                        "'Max price' label is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_max_price).is_displayed(),
            "'Max price' dropdown is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.label_property_type).is_displayed(),
            "'Property type' label is not displayed ")
        radio_labels = self.driver.find_elements(By.XPATH, to_rent_search_screen_locs.labels_radio_buttons)
        radio_label_names = []
        exp_label_names = ["Show all", "Houses", "Flats"]
        for i in radio_labels:
            radio_label_names.append(i.text)
        self.assertListEqual(radio_label_names, exp_label_names,
                             f"All radio labels are displayed as expected{radio_label_names}")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.radio_button_show_all).is_displayed(),
            "'Show all' radio button is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.radio_button_houses).is_displayed(),
            "'Houses' radio button is not displayed ")
        self.assertTrue(
            self.driver.find_element(By.XPATH, to_rent_search_screen_locs.radio_button_flats).is_displayed(),
            "'Flats' radio button is not displayed ")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.button_search).is_displayed(),
                        "'Search' button is not displayed")

    def enter_search_criteria_hit_search(self, search_area, bedrooms, max_price):
        """
        This method will enter criteria in search fields and click on search button
        :return: None
        """
        self.driver.find_element(By.XPATH, to_rent_search_screen_locs.combobox_search_area).click()
        self.driver.find_element(By.XPATH, to_rent_search_screen_locs.combobox_search_area).send_keys(search_area)
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 f'//ul[@role="listbox"]//li[@role="option"]//span[text()="{search_area}"]').click()
        self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_bedrooms).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 f'//ul[@role="listbox"]//li[@role="option"]//div[contains(text(),"{bedrooms}+")]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_max_price).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 f'//ul[@role="listbox"]//li[@role="option"]//div[contains(text(),"{"{:,}".format(max_price)} pcm")]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, to_rent_search_screen_locs.button_search).click()

    def validate_to_rent_search_results_screen_elements(self, search_area):
        """
        This method will validate search result screen elements
        :return: None
        """
        common_methods.wait_till_element_is_visible(self.driver, to_rent_search_screen_locs.search_result_header)
        self.assertTrue(self.driver.find_element(By.XPATH, f'//div[@data-testid="search-desktop-subheader"]//input['
                                                           f'@value="{search_area}"]').is_displayed())
        area = self.driver.find_element(By.XPATH, f'//div[@data-testid="search-desktop-subheader"]//input['
                                                  f'@value="{search_area}"]').get_attribute("value")
        self.assertTrue(area == search_area, "Search area is not same as user input")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.search_result_header).is_displayed(), "'Search Result' header is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_search_radius_search_filter).is_displayed(), "'Search radius' filter is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_bedrooms_search_filter).is_displayed(), "'Bedrooms' filter is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_property_type_search_filter).is_displayed(), "'Property type' radius filter is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_price_range_search_filter).is_displayed(), "'Price range' filter is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.button_search_filter).is_displayed(), "'Search' button is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.button_create_email_alert).is_displayed(), "'Create email alert' button is not displayed")

    def enter_min_price_range(self, min_price):
        """
        This method will enter minimum price range for rental search
        :return: None
        """
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 to_rent_search_screen_locs.dropdown_price_range_search_filter).is_displayed(),
                        "'Price range' filter is not displayed")
        self.driver.find_element(By.XPATH,
                                 to_rent_search_screen_locs.dropdown_price_range_search_filter).click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 to_rent_search_screen_locs.dropdown_price_range_min).is_displayed(),
                        "'Price range min' Dropdown is not displayed")
        self.driver.find_element(By.XPATH,
                                 to_rent_search_screen_locs.dropdown_price_range_min).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 f'//select[@data-testid="min_price"]//option[contains(text(),"{"{:,}".format(min_price)} pcm")]').click()
        self.driver.find_element(By.XPATH,
                                 to_rent_search_screen_locs.button_search_filter).click()
        time.sleep(5)

    def click_on_create_email_alert(self, frequency):
        """
        This methos will click on Create email alert button
        :return:None
        """
        self.driver.find_element(By.XPATH, to_rent_search_screen_locs.button_create_email_alert).click()
        time.sleep(2)
        obj = Select(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.dropdown_alert_frequency))
        obj.select_by_visible_text(frequency)
        time.sleep(2)
        common_methods.wait_till_element_clickable(self.driver, to_rent_search_screen_locs.button_save_search)
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 to_rent_search_screen_locs.button_save_search).click()
        time.sleep(2)
        common_methods.wait_for_element(self.driver, to_rent_search_screen_locs.msg_success_search_saved)
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 to_rent_search_screen_locs.msg_success_search_saved).is_displayed(),
                        "'Success' message is not displayed")
        self.assertTrue(self.driver.find_element(By.XPATH,
                                                 to_rent_search_screen_locs.link_manage_my_saved_searches).is_displayed(),
                        "'Manage my saved searches' Link is not displayed")
        time.sleep(2)
        a = ActionChains(self.driver)
        a.move_to_element(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.link_manage_my_saved_searches)).perform()
        time.sleep(2)
        a.click(self.driver.find_element(By.XPATH, to_rent_search_screen_locs.link_manage_my_saved_searches)).perform()
        time.sleep(5)


    def yield_driver(self):
        """
        This method will return the driver
        :return: None
        """
        return self.driver




