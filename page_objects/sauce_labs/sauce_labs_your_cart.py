import random
from unittest import TestCase

from utils.common_methods import common_methods

class your_cart_locs:
    txt_header = '//div[@class="header_label"]//div[@class="app_logo" and text()="Swag Labs"]'
    txt_title = '//span[@class="title" and text()="Your Cart"]'
    cart_list_heading_1 = '//div[@class="cart_quantity_label"]'
    cart_list_heading_2 = '//div[@class="header_secondary_container"]'
    cart_items = '//div[@class="cart_item_label"]'
    btn_continue_shopping = 'continue-shopping'
    btn_checkout = 'Checkout'


class your_cart_methods(common_methods, TestCase):

    def validate_current_page_your_cart(self):
        """
        Method to validate current page is your cart and all its elements are present
        :return: None
        """
        self.assertTrue()

    def validate_all_cart_products(self):
        """
        Method to validate all products added to cart are present in your cart page
        :return: None
        """

    def click_checkout(self):
        """
        Method to modify quantity for a product
        :return: None
        """

