"""
Test Case: User Registration Functionality

===========================================
Test Steps
===========================================

1. Open the application in the browser.
2. Navigate to the "My Account" menu and click on "Register".
3. Enter user details:
   - First Name
   - Last Name
   - Email
   - Telephone Number
   - Password and Confirm Password
4. Accept the Privacy Policy checkbox.
5. Click on the "Continue" button.
6. Verify that the account creation confirmation message is displayed.

Expected Result:
----------------
After submitting valid details, the system should display the message:
"Your Account Has Been Created!"
"""
import pytest

from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utilities.random_data_util import RandomDataUtil
from playwright.sync_api import expect


@pytest.mark.sanity
@pytest.mark.regression
def test_user_registration(page):
    home_page=HomePage(page)
    registration_page=RegistrationPage(page)

    home_page.click_my_account()
    home_page.click_register()

    random_data=RandomDataUtil()

    first_name=random_data.get_first_name()
    last_name = random_data.get_last_name()
    email = random_data.get_email()
    phone = random_data.get_phone_number()
    password = random_data.get_password()

    registration_page.set_first_name(first_name)
    registration_page.set_last_name(last_name)
    registration_page.set_email(email)
    registration_page.set_telephone(phone)
    registration_page.set_password(password)
    registration_page.set_confirm_password(password)

    registration_page.set_privacy_policy()
    registration_page.click_continue()

    confirmation_msg=registration_page.get_confirmation_msg()
    expect(confirmation_msg).to_have_text("Your Account Has Been Created!")