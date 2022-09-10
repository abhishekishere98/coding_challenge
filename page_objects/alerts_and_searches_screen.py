class zoopla_landing_locs:
    header_alerts_searches = "//h1[normalize-space()='Alerts & searches']"
    tab_residential = "(//a[normalize-space()='Residential'])[1]"
    tab_commercial = "//li[@aria-controls='tab-commercial']//a[text()='Commercial']"
    tab_to_rent = "//li[@aria-controls='tab-residential-to-rent']//a[text()='To rent']"
    tab_for_sale = "//li[@aria-controls='tab-residential-to-rent']//a[text()='For sale']"
    column_header_alerts_searches = "//div[@id='tab-residential-to-rent']//div[@class='myaccount-alert-col']//strong"
    dropdown_first_saved_search_frequency = '(//form//div[@class="myaccount-alert-col"]//select)[1]'


