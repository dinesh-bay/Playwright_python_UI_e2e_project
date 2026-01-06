# login_page.py
# =====================
# This class represents the "Login Page" of the application.
# It is designed using the Page Object Model (POM) pattern,
# which helps to keep locators and actions separate from the test logic.

from playwright.sync_api import Page, expect


class LoginPage:
    """Page Object Model class for the Login Page."""

    def __init__(self, page: Page):
        """
        Constructor that initializes the Playwright Page instance
        and defines all locators used on the Login Page.
        """
        self.page = page

        # ===== Locators =====
        # Using CSS selectors to locate elements on the Login page.
        self.txt_email_address = page.locator('#input-email')
        self.txt_password = page.locator('#input-password')
        self.btn_login = page.locator('input[value="Login"]')
        self.txt_error_message = page.locator('.alert.alert-danger.alert-dismissible')

    # ===== Action Methods =====
    # These methods represent user interactions on the Login Page.

    def set_email(self, email: str):
        """Enter the email address in the Email field."""
        try:
            self.txt_email_address.fill(email)
        except Exception as e:
            print(f" Exception while entering email: {e}")
            raise

    def set_password(self, password: str):
        """Enter the password in the Password field."""
        try:
            self.txt_password.fill(password)
        except Exception as e:
            print(f" Exception while entering password: {e}")
            raise

    def click_login(self):
        """Click the Login button."""
        try:
            self.btn_login.click()
        except Exception as e:
            print(f" Exception while clicking Login button: {e}")
            raise

    def login(self, email: str, password: str):
        """
        Perform the complete login operation:
        1. Enter email
        2. Enter password
        3. Click the Login button
        """
        self.set_email(email)
        self.set_password(password)
        self.click_login()

    def get_login_error(self):
        """
        Return the error message element if login fails.
        Example use:
            error_text = login_page.get_login_error().inner_text()
        """
        try:
            return self.txt_error_message
        except Exception as e:
            print(f" Exception while fetching login error message: {e}")
            return None
