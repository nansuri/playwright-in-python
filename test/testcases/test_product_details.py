import unittest
import allure
from setup_test import SetupTest
from util.common_util import CommonUtils
from pages.page_product_listing import ProductListingPage
from pages.page_product_details import ProductDetailsPage
from test_data.product_details_data import ProductDetailsData


class ProductDetailsTestSuite(SetupTest):

    # Testcases
    @allure.feature('Product Details')
    @allure.story('Verify user will be able to redirected to product details')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_NM_H_verify_product_details_001(self):
        """
        Verify user will be able to redirected to product details
        """
        # Perform login
        CommonUtils.login_using_valid_cred(self.page)

        # do small assertion make sure product is listed
        self.page_product_listing = ProductListingPage(self.page)
        self.assertTrue(self.page_product_listing.is_view_cart_available())

        self.page_product_listing.click_product_details(ProductDetailsData.
                                                        Product.PRODUCT_NAME)
        self.page_product_details = ProductDetailsPage(self.page)
        CommonUtils.capture_and_attach_screenshot(self, "product_details")
        self.assertTrue(self.page_product_details.is_view_product_details())
        
    @allure.feature('Product Details')
    @allure.story('Verify user will be able to add product to cart')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_NM_H_verify_add_to_cart_product_002(self):
        """
        Verify user will be able to add product to cart
        """
        # Perform login
        CommonUtils.login_using_valid_cred(self.page)

        # do small assertion make sure product is listed
        self.page_product_listing = ProductListingPage(self.page)
        self.page_product_listing.click_product_details(ProductDetailsData.
                                                        Product.PRODUCT_NAME)
        self.page_product_details = ProductDetailsPage(self.page)
        self.page_product_details.click_add_to_cart()
        CommonUtils.capture_and_attach_screenshot(self, "product_details")
        self.assertTrue(self.page_product_listing.is_listing_page_open())


if __name__ == "__main__":
    unittest.main()
