from unittest import TestCase

from utils.common_methods import common_methods


class landing_page_locs:
    txt_header = '//div[@class="header_label"]//div[@class="app_logo" and text()="Swag Labs"]'
    txt_title = '//span[@class="title" and text()="Products"]'
    dd_filter_sort = '//span[@class="select_container"]//select'
    icon_cart = '//div[@id="shopping_cart_container"]'
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


class landing_page_methods(common_methods, TestCase):

    def validate_products_all_products_page(self):
        """
        This method validates that all items displayed in all products page are as per specification
        :return: None
        """
        # Validate Swag Labs header is displayed correctly
        self.assertTrue(self.wait_till_element_is_visible(landing_page_locs.txt_header).is_displayed(),
                        "Swag Labs Header is displayed")
        self.assertTrue(self.get_text_from_element(self.find_element("xpath", landing_page_locs.txt_header))
                        == "Swag Labs", "Swag Labs header is displayed with correct text")
        # Validate Products heading is displayed correctly
        self.assertTrue(self.wait_till_element_is_visible(landing_page_locs.txt_title).is_displayed(),
                        "Products Tile is displayed")
        self.assertTrue(self.get_text_from_element(self.find_element("xpath", landing_page_locs.txt_title))
                        == "Products", "Products title is displayed with correct text")
        # Validate the Products displayed in All Products page
        # Validate Product Names
        name_ele = self.wait_for_elements(landing_page_locs.item_product_names)
        item_names = []
        for i in name_ele:
            item_names.append(i.text)
        self.assertListEqual(item_names, landing_page_locs.list_items_names, "All Product Names are displayed")
        # Validate Product Descriptions
        name_desc = self.wait_for_elements(landing_page_locs.item_product_desc)
        item_descs = []
        for i in name_desc:
            item_descs.append(i.text)
        self.assertListEqual(item_descs, landing_page_locs.list_items_desc, "All Product Descriptions are displayed")
        # Validate Add To card button displayed for all products
        butns_add_to_cart = self.wait_for_elements(landing_page_locs.item_product_names)
        self.assertTrue(butns_add_to_cart.__len__() == 6, "All Add To Cart buttons displayed")

