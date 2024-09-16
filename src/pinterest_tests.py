# src/pinterest_tests.py
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException


class PinterestAutomation:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def open_pinterest(self):
        self.driver.get("https://www.pinterest.com/")
        time.sleep(3)

    def check_visibility(self, by_method, locator, element_name):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((by_method, locator)))
            print(f"{element_name} is visible.")
        except Exception as e:
            print(f"{element_name} is NOT visible. Error: {str(e)}")

    def login(self, email, password):
        try:
            # Locate and click the login button
            self.check_visibility(By.XPATH, '//div[text()="Log in"]', "Log In button")
            login_button = self.driver.find_element(By.XPATH, '//div[text()="Log in"]')
            login_button.click()

            # Enter email and password
            email_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'id')))
            password_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'password')))

            email_field.send_keys(email)
            password_field.send_keys(password)

            # Submit login form
            submit_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
            )
            submit_button.click()

            # Wait for a few seconds for the page to load
            time.sleep(5)

            # Check if the profile element is present after login
            profile_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@data-test-id="header-profile"]'))
            )
            if profile_element:
                print("Login successful.")
                return True

        except Exception as e:
            print(f"Login failed. Error: {str(e)}")
            return False

    def perform_search(self, search_term):
        try:
            search_box = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@data-test-id="search-box-input"]'))
            )
            search_box.send_keys(search_term)
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)
            print("Search performed.")
        except Exception as e:
            print(f"Search failed. Error: {str(e)}")

    def logout(self):
        try:
            accounts_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@data-test-id="header-accounts-options-button"]'))
            )
            accounts_button.click()

            logout_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//span[text()="Log out"]'))
            )
            logout_button.click()
            print("Logged out successfully.")
        except Exception as e:
            print(f"Logout failed. Error: {str(e)}")

    def check_link_visibility(self, link_name, link_text):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, link_text))
            )
            print(f"{link_name} link is visible.")
        except Exception as e:
            print(f"{link_name} link is NOT visible. Error: {str(e)}")

    def check_new_sms(self):
        try:
            notifications_button = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@data-test-id="notifications-button"]'))
            )
            unread_notifications_count_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, './/div[@class="Jea KS5 Lfz MIw mQ8 yBD zI7 iyn Hsu"]'))
            )
            unread_notifications_count_text = unread_notifications_count_element.text

            if unread_notifications_count_text != "0":
                print("New SMS notifications available.")
                self.driver.save_screenshot('new_sms_notifications.png')
            else:
                print("No new SMS notifications.")

        except Exception as e:
            print("No new SMS notifications.")

    def click_svg_and_read_last_sms(self):
        try:
            svg_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Messages"]'))
            )
            svg_button.click()

            conversations_container = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@data-test-id="conversation-list-container"]'))
            )
            time.sleep(5)

            conversations_container.screenshot('conversations.png')

            conversation_items = conversations_container.find_elements(By.XPATH, './/div[@data-test-id="conversation-list-item"]')

            if conversation_items:
                last_conversation = conversation_items[-1]
                last_message = last_conversation.find_element(By.XPATH, './/div[contains(@class, "JlN")]').text
                print(f"Last message: {last_message}")
                home_button = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Home"]'))
                )
                home_button.click()
            else:
                print("No conversations found.")

        except Exception as e:
            print(f"Failed to check and screenshot conversations. Error: {str(e)}")

    def send_sms(self):
        try:
            messages_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Messages']"))
            )
            messages_button.click()

            compose_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@data-test-id='compose-new-message-button']"))
            )
            compose_button.click()

            search_box = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Search field']"))
            )
            search_box.send_keys("hasibshanto260@gmail.com")

            suggestion = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and .//div[@title='Hasibur shanto']]"))
            )
            suggestion.click()

            next_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Next']"))
            )
            next_button.click()

            message_box = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//textarea[@id='messageDraft']"))
            )
            message_box.send_keys("Hello, this is a test message!")

            send_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send message to conversation']"))
            )
            send_button.click()

            print("Message sent successfully.")
            #self.driver.save_screenshot('image.png')
            home_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//a[@aria-label="Home"]'))
            )
            home_button.click()

        except Exception as e:
            print(f"Failed to perform actions. Error: {str(e)}")

    def quit(self):
        self.driver.quit()

