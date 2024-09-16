# tests/test_pinterest.py
import time
import pytest
from selenium.webdriver.common.by import By
from src.pinterest_tests import PinterestAutomation
from config.credentials import EMAIL, PASSWORD


@pytest.fixture(scope="module")
def pinterest():
    pinterest = PinterestAutomation()
    pinterest.open_pinterest()
    yield pinterest
    pinterest.quit()
# Test Case 1: Check Pinterest logo visibility
def test_case_1_check_logo(pinterest):
    pinterest.check_visibility(By.XPATH, '//div[@data-test-id="unauth-header-logo"]', "Pinterest Logo")
# Test Case 2: Check Log In button visibility
def test_case_2_check_login_button(pinterest):
    pinterest.check_visibility(By.XPATH, '//div[text()="Log in"]', "Log In button")

# Test Case 3: Check Sign Up button visibility
def test_case_3_check_signup_button(pinterest):
    pinterest.check_visibility(By.XPATH, '//div[text()="Sign up"]', "Sign Up button")

# Test Case 4: Check specific link visibility
def test_case_4_check_links(pinterest):
    links_to_check = {
        "Explore": 'Explore',
        "Watch": 'Watch',
        "About": 'About',
        "Business": 'Business',
        "Press": 'Press'
    }
    for link_name, link_text in links_to_check.items():
        pinterest.check_link_visibility(link_name, link_text)

# Test Case 5: Perform login with wrong email
def test_case_5_login_wrong_email(pinterest):
    assert pinterest.login("wrongemail202220123@example.com", PASSWORD) == False
    pinterest.driver.refresh()

# Test Case 6: Perform login with wrong password
def test_case_6_login_wrong_password(pinterest):
    assert pinterest.login(EMAIL, "wrongpassword") == False
    pinterest.driver.refresh()

# Test Case 7: Perform login without email
def test_case_7_login_without_email(pinterest):
    assert pinterest.login("", PASSWORD) == False
    pinterest.driver.refresh()

# Test Case 8: Perform login with valid credentials
def test_case_8_login_valid_credentials(pinterest):
    assert pinterest.login(EMAIL, PASSWORD) == True
    pinterest.driver.refresh()

# Test Case 9: Perform search operation
def test_case_9_perform_search(pinterest):
    
    pinterest.login(EMAIL, PASSWORD)
    pinterest.perform_search("demon slayer")


# Test Case 11: Check new SMS notifications
def test_case_11_check_new_sms(pinterest):
    pinterest.login(EMAIL, PASSWORD)
    pinterest.check_new_sms()


# Test Case 12: Read last SMS from messages
def test_case_12_read_last_sms(pinterest):
    pinterest.login(EMAIL, PASSWORD)
    pinterest.click_svg_and_read_last_sms()


# Test Case 13: Send SMS to a user
def test_case_13_send_sms(pinterest):
    pinterest.login(EMAIL, PASSWORD)
    pinterest.send_sms()


# Test Case 10: Perform logout after login
def test_case_10_perform_logout(pinterest):
    pinterest.login(EMAIL, PASSWORD)
    pinterest.logout()
    time.sleep(2)

# Test Case 14: Check Explore link
def test_case_14_check_explore_link(pinterest):
    pinterest.check_link_visibility("Explore", "Explore")


# Test Case 15: Check Watch link
def test_case_15_check_watch_link(pinterest):
    pinterest.check_link_visibility("Watch", "Watch")

# Test Case 16: Check About link
def test_case_16_check_about_link(pinterest):
    pinterest.check_link_visibility("About", "About")

# Test Case 17: Check Business link
def test_case_17_check_business_link(pinterest):
    pinterest.check_link_visibility("Business", "Business")



