import random
from unittest import TestCase

from utils.common_methods import common_methods


class your_cart_locs:
    txt_header = '//div[@class="header_label"]//div[@class="app_logo" and text()="Swag Labs"]'
    txt_title = '//span[@class="title" and text()="Your Cart"]'
    cart_list_heading_1 = '//div[@class="cart_quantity_label"]'
    cart_list_heading_2 = '//div[@class="header_secondary_container"]'
    cart_items = '//div[@class="cart_item"]'
    btn_continue_shopping = 'continue-shopping'
    btn_checkout = 'checkout'


class your_cart_methods(common_methods, TestCase):

    def validate_current_page_your_cart(self):
        """
        Method to validate current page is your cart and all its elements are present
        :return: None
        """
        self.assertTrue(self.wait_till_element_is_visible(your_cart_locs.txt_header),
                        "'Swag Labs' Heading is not displayed'")
        self.assertTrue(self.wait_till_element_is_visible(your_cart_locs.txt_header),
                        "'Your Cart' title is not displayed'")
        self.assertTrue(self.wait_till_element_is_visible(your_cart_locs.cart_list_heading_1),
                        "'QTY' Heading is not displayed'")
        self.assertTrue(self.wait_till_element_is_visible(your_cart_locs.cart_list_heading_2),
                        "'Description' Heading is not displayed'")
        self.assertTrue(self.find_element("ID", your_cart_locs.btn_continue_shopping),
                        "Continue Shopping button not displayed in Your Cart page")
        self.assertTrue(self.find_element("ID", your_cart_locs.btn_checkout),
                        "Checkout button not displayed in Your Cart page")

    def validate_all_cart_products(self, cart_products):
        """
        Method to validate all products added to cart are present in your cart page
        :param cart_products: Details of all products added to cart(returned by capture_product_details method in products page)
        :return: None
        """
        products_in_cart = []
        products_ele = self.wait_for_elements(your_cart_locs.cart_items)
        for i in range(1, products_ele.__len__()+1):
            product_name = self.find_element("XPATH",
                                             '(' + your_cart_locs.cart_items + ')[' + str(i) + ']//div['
                                                                                                         '@class="inventory_item_name"]').text
            product_desc = self.find_element("XPATH",
                                             '(' + your_cart_locs.cart_items + ')[' + str(i) + ']//div['
                                                                                                         '@class="inventory_item_desc"]').text
            product_price = self.find_element("XPATH",
                                              '(' + your_cart_locs.cart_items + ')[' + str(i) + ']//div['
                                                                                                          '@class="inventory_item_price"]').text
            products_in_cart.append([product_name, product_desc, product_price])
        self.assertCountEqual(cart_products, products_in_cart, "All Product details dont match")

    def click_checkout(self):
        """
        Method to click on checkout button
        :return: None
        """
        self.find_element("ID", your_cart_locs.btn_checkout).click()

    def click_continue_shopping(self):
        """
        Method to click on continue shopping button
        :return: None
        """
        self.find_element("ID", your_cart_locs.btn_checkout).click()
