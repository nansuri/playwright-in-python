import unittest
import allure
from util.common_util import CommonUtils
from pages.page_login import LoginPage
from setup_test import SetupTest
from test_data.login_test_data import LoginTestData


class LoginTestSuite(SetupTest):

    # These are the testcases
    @allure.feature('Login')
    @allure.story('Verify Login using Valid Credentials')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_NM_H_login_using_valid_credential_001(self):
        """
        Test login with valid credentials.
        """
        # initiate LoginPage instance
        self.page_login = LoginPage(self.page)
        self.page_login.goto_login_page()
        self.page_login.login(LoginTestData.Credentials.VALID_USERNAME,
                              LoginTestData.Credentials.VALID_PASSWORD)
        # capture and attach
        CommonUtils.capture_and_attach_screenshot(self, "login")
        self.assertTrue(self.page_login.is_login_success())

    @allure.feature('Login')
    @allure.story('Verify Login using Invalid Credentials')
    @allure.severity(allure.severity_level.NORMAL)
    def test_NE_H_login_using_invalid_credential_001(self):
        """
        Test login with invalid credentials.
        """
        self.page_login = LoginPage(self.page)
        self.page_login.goto_login_page()
        self.page_login.login(LoginTestData.Credentials.INVALID_USERNAME,
                              LoginTestData.Credentials.INVALID_PASSWORD)
        # capture and attach
        CommonUtils.capture_and_attach_screenshot(self, "login")
        self.assertTrue(self.page_login.is_login_failed())


if __name__ == "__main__":
    unittest.main()
