from playwright.sync_api import Page
from configs.general_config import Configs


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto_login_page(self):
        self.page.goto(Configs.General.LOGIN_URL)
        self.page.wait_for_selector('input[name="username"]')

    def enter_username(self, username):
        self.page.fill('input[name="username"]', username)

    def enter_password(self, password):
        self.page.fill('input[name="password"]', password)

    def click_login_button(self):
        self.page.click('button[type="submit"]')

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def is_login_success(self):
        return self.page.is_visible('h1:text("Products")')

    def is_login_failed(self):
        return self.page.is_visible('text="Invalid credentials. Please try again."')
