import unittest
from playwright.sync_api import sync_playwright
from configs.general_config import Configs


class SetupTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.playwright = sync_playwright().start()
        # Choose browser based on configuration
        if Configs.General.BROWSER == 'chromium':
            cls.browser = cls.playwright.chromium.launch(headless=Configs
                                                         .General.HEADLESS)
        elif Configs.General.BROWSER == 'firefox':
            cls.browser = cls.playwright.firefox.launch(headless=Configs
                                                        .General.HEADLESS)
        elif Configs.General.BROWSER == 'webkit':
            cls.browser = cls.playwright.webkit.launch(headless=Configs
                                                       .General.HEADLESS)
        else:
            raise ValueError(f"Unsupported browser: {Configs.General.BROWSER}")

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()

    def setUp(self):
        self.page = self.browser.new_page()

    def tearDown(self):
        self.page.close()
