import allure
import os
from pages.page_login import LoginPage
from test_data.login_test_data import LoginTestData
from datetime import datetime


class CommonUtils:

    @staticmethod
    def login_using_valid_cred(page):
        """
        Perform login using valid credentials.
 
        Args:
            page: The Playwright page object.
        """
        page_login = LoginPage(page)
        page_login.goto_login_page()
        page_login.login(LoginTestData.Credentials.VALID_USERNAME, 
                         LoginTestData.Credentials.VALID_PASSWORD)
        assert page_login.is_login_success()
        
    @staticmethod
    def capture_and_attach_screenshot(self, description):
        """
        Capture a screenshot and attach it to the Allure report.
        """
        # Define the folder to store screenshots
        base_dir = os.path.dirname(os.path.dirname(__file__))
        screenshots_folder = os.path.join(base_dir, "screenshots")

        # Create the folder if it doesn't exist
        if not os.path.exists(screenshots_folder):
            os.makedirs(screenshots_folder)

        # Generate screenshot name with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = os.path.join(screenshots_folder,
                                       f"{description}_{timestamp}.png")

        # Capture screenshot
        self.page.screenshot(path=screenshot_name)

        # Attach screenshot to Allure report
        with open(screenshot_name, "rb") as file:
            allure.attach(file.read(), name="Screenshot",
                          attachment_type=allure.attachment_type.PNG)
