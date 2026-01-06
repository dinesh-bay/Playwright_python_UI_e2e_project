# shopping_cart_page.py
from playwright.sync_api import Page, expect
from pages.checkout_page import CheckoutPage  # Adjust import path as per your project structure


class ShoppingCartPage:
    """
    Page Object Model for the Shopping Cart Page.
    This class contains web element locators and reusable methods
    to interact with the shopping cart page.
    """

    def __init__(self, page: Page):
        self.page = page

        # ===== Locators =====
        # Locator for the total price in the cart summary section
        self.lbl_total_price = page.locator(
            "//*[@id='content']/div[2]/div/table//strong[text()='Total:']//following::td"
        )

        # Locator for the "Checkout" button
        self.btn_checkout = page.locator("a.btn.btn-primary")

    # ===== Methods =====

    def get_total_price(self):
        """
        Returns the total price element from the shopping cart.

        :return: Locator representing the total price element, or None if not found.
        """
        try:
            return self.lbl_total_price
        except Exception as e:
            print(f"Unable to retrieve total price: {e}")
            return None

    def click_on_checkout(self) -> CheckoutPage:
        """
        Clicks on the "Checkout" button and navigates to the Checkout Page.

        :return: Instance of the CheckoutPage class.
        """
        try:
            self.btn_checkout.click()
            return CheckoutPage(self.page)
        except Exception as e:
            print(f"Error clicking on checkout button: {e}")
            raise e  # Re-raise to fail the test if critical navigation fails

    def is_page_loaded(self) :
        """
        Verifies if the Shopping Cart page is successfully loaded.

        :return: Element if page loaded, otherwise None.
        """
        try:
            return self.btn_checkout
        except Exception as e:
            print(f"Error verifying shopping cart page load: {e}")
            return None
