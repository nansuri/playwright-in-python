from playwright.sync_api import Page


class ProductDetailsPage:
    def __init__(self, page: Page):
        self.page = page

    def is_view_product_details(self):
        return self.page.is_visible('text="This is product 1."')

    def click_add_to_cart(self):
        self.page.wait_for_selector('a[href="/add_to_cart/1"]', state='visible')
        self.page.click('a[href="/add_to_cart/1"]')
