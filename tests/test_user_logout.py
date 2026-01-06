"""
Test Case: User Logout Functionality

===========================================
Test Steps
===========================================

1. Open the application in the browser.
2. Navigate to the "My Account" menu and click on "Login".
3. Enter valid user credentials (email and password).
4. Click on the "Login" button.
5. Verify that the "My Account" page is displayed.
6. Click on the "Logout" link or button.
7. Verify that the Logout confirmation page is displayed.
8. Click the "Continue" button to return to the Home page.
9. Verify that the Home page is displayed by checking its title.

Expected Result:
----------------
After logging out, the user should be redirected to the Logout confirmation page.
Clicking "Continue" should navigate back to the Home page successfully.
"""

import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from config import Config


@pytest.mark.regression
def test_user_logout(page):
    """
    Automated Test Case: Verify that a logged-in user can successfully log out of the application.
    """

    # --- Step 1: Create Page Object Instances ---
    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    # --- Step 2: Navigate to Login Page ---
    home_page.click_my_account()
    home_page.click_login()

    # --- Step 3: Enter Valid Credentials and Login ---
    login_page.set_email(Config.email)
    login_page.set_password(Config.password)
    login_page.click_login()

    # --- Step 4: Verify 'My Account' Page is Displayed ---
    expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=3000)

    # --- Step 5: Perform Logout Action ---
    logout_page = my_account_page.click_logout()

    # --- Step 6: Verify Logout Page is Displayed ---
    # Checks whether the 'Continue' button is visible on the Logout page
    expect(logout_page.get_continue_button()).to_be_visible(timeout=3000)

    # --- Step 7: Click 'Continue' to Return to Home Page ---
    logout_page.click_continue()

    # --- Step 8: Verify Navigation to Home Page by Checking Page Title ---
    expect(page).to_have_title("Your Store")
