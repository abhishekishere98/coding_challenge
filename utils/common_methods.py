from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver


class common_methods:

    def wait_for_element(driver: webdriver, element):
        element_found = WebDriverWait(driver, 5000, 500).until(EC.presence_of_element_located((By.XPATH, element)))
        return element_found

    def wait_till_element_is_visible(driver: webdriver, element):
        element_found = WebDriverWait(driver, 5000, 500).until(EC.visibility_of_element_located((By.XPATH, element)))
        return element_found

    def wait_till_element_clickable(driver: webdriver, element):
        element_found = WebDriverWait(driver, 5000, 500).until(EC.element_to_be_clickable((By.XPATH, element)))
        return element_found

    def wait_for_elements(driver: webdriver, element):
        elements_found = WebDriverWait(driver, 5000, 500).until(EC.presence_of_all_elements_located((By.XPATH, element)))
        return elements_found

