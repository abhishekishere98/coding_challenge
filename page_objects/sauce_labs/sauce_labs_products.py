from unittest import TestCase

from utils.common_methods import common_methods
from PIL import Image

class landing_page_locs:
    txt_header = '//h3//button[@class="error-button"]'
    txt_title = '//span[@class="title" and text()="Products"]'
    dd_filter_sort = '//span[@class="select_container"]//select'
    icon_cart = '//div[@id="shopping_cart_container"]'
    item_product = '//div[@class="inventory_item"]'
    item_product_names = '//div[@class="inventory_item_name"]'
    list_items_names = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt",
                        "Sauce Labs Fleece Jacket", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
    list_product_desc = '//div[@class="inventory_item_desc"]'
    list_items_desc = ["carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.",
                       "A red light isn't the desired state in testing but it sure helps when riding your bike at night. Water-resistant with 3 lighting modes, 1 AAA battery included.",
                       "Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.",
                       "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office.",
                       "Rib snap infant onesie for the junior automation engineer in development. Reinforced 3-snap bottom closure, two-needle hemmed sleeved and bottom won't unravel.",
                       "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to automate a few tests. Super-soft and comfy ringspun combed cotton."]
    btn_add_to_cart = '//button[contains(@id, "add-to-cart")]'

