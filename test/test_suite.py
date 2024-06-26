import unittest
import allure
from testcases.test_login import LoginTestSuite
from testcases.test_product_listing import ProductListingTestSuite
from testcases.test_product_details import ProductDetailsTestSuite


# Write all of the test suite that wan to be executed
def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        LoginTestSuite))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProductListingTestSuite))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProductDetailsTestSuite))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    with allure.step('Running all tests'):
        runner.run(suite())
