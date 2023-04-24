import random
from unittest import TestCase

from utils.common_methods import common_methods


class all_products_page_locs:
    txt_header = '//div[@class="header_label"]//div[@class="app_logo" and text()="Swag Labs"]'
    txt_title = '//span[@class="title" and text()="Products"]'
    dd_filter_sort = '//span[@class="select_container"]//select'
    icon_cart = '//div[@id="shopping_cart_container"]'
    cart_products_no = '//span[@class="shopping_cart_badge"]'
    item_product = '//div[@class="inventory_item"]'
    item_product_names = '//div[@class="inventory_item_name"]'
    list_items_names = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",
                        "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    item_product_desc = '//div[@class="inventory_item_desc"]'
    list_items_desc = [
        "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
        "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
        "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.",
        "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
        "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
        "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton."]
    btn_add_to_cart = '//button[contains(@id, "add-to-cart")]'


class all_products_page_methods(common_methods, TestCase):
    product_no_cart = 0
    product_nos_cart = []
    product_details = []


    def validate_products_all_products_page(self):
        """
        This method validates that all items displayed in all products page are as per specification
        :return: None
        """
        # Validate Swag Labs header is displayed correctly
        self.assertTrue(self.wait_till_element_is_visible(all_products_page_locs.txt_header).is_displayed(),
                        "Swag Labs Header is displayed")
        self.assertTrue(self.get_text_from_element(self.find_element("xpath", all_products_page_locs.txt_header))
                        == "Swag Labs", "Swag Labs header is displayed with correct text")
        # Validate Products heading is displayed correctly
        self.assertTrue(self.wait_till_element_is_visible(all_products_page_locs.txt_title).is_displayed(),
                        "Products Tile is displayed")
        self.assertTrue(self.get_text_from_element(self.find_element("xpath", all_products_page_locs.txt_title))
                        == "Products", "Products title is displayed with correct text")
        # Validate the Products displayed in All Products page
        # Validate Product Names
        name_ele = self.wait_for_elements(all_products_page_locs.item_product_names)
        item_names = []
        for i in name_ele:
            item_names.append(i.text)
        self.assertListEqual(item_names, all_products_page_locs.list_items_names, "All Product Names are displayed")
        # Validate Product Descriptions
        name_desc = self.wait_for_elements(all_products_page_locs.item_product_desc)
        item_descs = []
        for i in name_desc:
            item_descs.append(i.text)
        self.assertListEqual(item_descs, all_products_page_locs.list_items_desc, "All Product Descriptions are displayed")
        # Validate Add To card button displayed for all products
        butns_add_to_cart = self.wait_for_elements(all_products_page_locs.item_product_names)
        self.assertTrue(butns_add_to_cart.__len__() == 6, "All Add To Cart buttons displayed")

    def validate_random_product_added_to_cart(self):
        """
        This method validates that any one of the products in landing page is added to cart
        :return: None
        """
        total_products = self.wait_for_elements(all_products_page_locs.item_product_names)
        self.product_no_cart = random.randint(1, total_products.__len__())
        # Check that button state before clicking
        self.assertTrue(
            self.find_element("XPATH", '(' + all_products_page_locs.item_product + ')[' + str(self.product_no_cart) + ']//button').text == "Add to cart",
            "Add Cart button not present before adding product to cart")
        # Click on add to cart
        self.find_element("XPATH", '(' + all_products_page_locs.item_product + ')[' + str(self.product_no_cart) + ']//button').click()
        # Check that button is changed to remove
        self.assertTrue(
            self.find_element("XPATH", '(' + all_products_page_locs.item_product + ')[' + str(self.product_no_cart) + ']//button').text == "Remove",
            "After adding product to cart, remove button is not displayed")
        self.product_nos_cart.append(self.product_no_cart)


    def validate_no_of_products_in_cart(self):
        """
        This method will check the no of products added to cart and validate it against the no displayed on cart icon
        :return: None
        """
        self.assertTrue(self.product_nos_cart.__len__() == int(self.find_element("XPATH", all_products_page_locs.cart_products_no).text),
                        "No of cart items shown in cart icon is incorrect")

    def capture_product_details(self) -> list:
        """
        This method will capture the details of all products added to cart
        :return: product details of all products added to cart
        """
        for i in self.product_nos_cart:
            product_name = self.find_element("XPATH", '(' + all_products_page_locs.item_product + ')[' + str(i) +']//a//div['
                                                                                                    '@class="inventory_item_name"]').text
            product_desc = self.find_element("XPATH", '(' + all_products_page_locs.item_product + ')[' + str(i) +']//div['
                                                                                                    '@class="inventory_item_desc"]').text
            product_price = self.find_element("XPATH", '(' + all_products_page_locs.item_product + ')[' + str(i) +']//div['
                                                                                                    '@class="inventory_item_price"]').text
            self.product_details.append([product_name, product_desc, product_price])
        return self.product_details

    def click_on_cart_icon(self):
        """
        This method will click on the cart icon to navigate to your cart page
        :return: None
        """
        self.find_element("XPATH", all_products_page_locs.icon_cart).click()
