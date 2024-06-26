from playwright.sync_api import Page


class ProductListingPage:
    def __init__(self, page: Page):
        self.page = page

    def is_listing_page_open(self):
        return self.page.is_visible('h1:text("Products")')

    def click_view_cart_button(self):
        self.page.click('a[href="/view_cart"]')

    def is_view_cart_available(self):
        return self.page.is_visible('a[href="/view_cart"]')

    def click_add_to_cart(self, whichEntry):
        self.page.wait_for_selector('/html/body/ul/li['+whichEntry+']/a[1]', state='visible')
        self.page.click('/html/body/ul/li['+whichEntry+']/a[2]')

    def click_product_details(self, whichEntry):
        self.page.wait_for_selector('text="'+whichEntry+'"', state='visible')
        self.page.click('text="'+whichEntry+'"')
