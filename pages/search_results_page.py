# search_results_page.py
from playwright.sync_api import Page
from pages.product_page import ProductPage  # Adjust import path based on your project structure


class SearchResultsPage:
    """
    Page Object Model class for the Search Results Page.
    This class contains locators and methods to interact with and verify
    products displayed after performing a search.
    """

    def __init__(self, page: Page):
        self.page = page

        # ===== Locators =====
        # Header that appears on the search results page
        self.search_page_header = page.locator("#content h1", has_text="Search -")

        # List of all product links shown in the search results
        self.search_products = page.locator("h4 > a")

    # ===== Page Header =====

    def get_search_results_page_header(self):
        """
        Returns the header element of the search results page, if it exists.
        Useful for verifying that the user is on the correct page.
        """
        try:
            return self.search_page_header
        except Exception as e:
            print(f"Error fetching search results page header: {e}")
            return None

    # ===== Product Verification =====

    def is_product_exist(self, product_name: str):
        """
        Checks whether a specific product is displayed on the search results page.

        :param product_name: Name of the product to search for
        :return: Product element if it exists, otherwise None
        """
        try:
            count = self.search_products.count()
            for i in range(count):
                product = self.search_products.nth(i)
                title = product.text_content()
                if title and title.strip() == product_name:
                    return product
        except Exception as e:
            print(f"Error while checking product existence: {e}")
        return None

    # ===== Product Selection =====

    def select_product(self, product_name: str) -> ProductPage | None:
        """
        Selects a product from the search results by its name and navigates to the Product Page.

        :param product_name: Name of the product to select
        :return: Instance of ProductPage if the product is found, otherwise None
        """
        try:
            count = self.search_products.count()
            for i in range(count):
                product = self.search_products.nth(i)
                title = product.text_content()
                if title and title.strip() == product_name:
                    product.click()
                    return ProductPage(self.page)
            print(f"Product not found: {product_name}")
        except Exception as e:
            print(f"Error while selecting product: {e}")
        return None

    # ===== Product Count =====

    def get_product_count(self):
        """
        Returns the products found in the search results.

        :return: All the products found
        """
        try:
            return self.search_products
        except Exception as e:
            print(f"Error while getting product count: {e}")
            return None
