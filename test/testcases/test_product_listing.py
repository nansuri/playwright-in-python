import unittest
import re
import allure
from pages.page_product_listing import ProductListingPage
from setup_test import SetupTest
from util.common_util import CommonUtils


class ProductListingTestSuite(SetupTest):

    # These are the testcases
    @allure.feature('Product Listing')
    @allure.story('Verify login then the user can navigate to the product listing page.')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_NM_H_navigate_to_product_listing_after_login_001(self):
        """
        Verify login then the user can navigate to the product listing page.
        """
        CommonUtils.login_using_valid_cred(self.page)
        self.page_product_listing = ProductListingPage(self.page)
        CommonUtils.capture_and_attach_screenshot(self, "product_listing")
        self.assertTrue(self.page_product_listing.is_view_cart_available())

    @allure.feature('Product Listing')
    @allure.story('Verify that user able to see all products')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_NM_H_navigate_to_product_listing_after_login_002(self):
        """
        Verify that user able to see all products
        """
        CommonUtils.login_using_valid_cred(self.page)
        self.page_product_listing = ProductListingPage(self.page)
        self.assertTrue(self.page_product_listing.is_view_cart_available())
        page_content = self.page.content()
        pattern = re.compile(r"Product")
        CommonUtils.capture_and_attach_screenshot(self, "product_listing")
        self.assertRegex(page_content, pattern)


if __name__ == "__main__":
    unittest.main()
