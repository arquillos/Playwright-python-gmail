"""Login into the Google account to store and reuse the credentials information"""
import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


# Get the configuration from the env variables
load_dotenv()
USER=os.getenv("USER")
PASSWORD=os.getenv("PASSWORD")
print(f"User: {USER}, password: {PASSWORD}")

# Save the Google credentials session
with sync_playwright() as playwright:
    # Use Firefox to get rid of Chrome security problems when loggin into Google
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://accounts.google.com")

    # Enter email
    email_input = page.get_by_label("Email or phone")
    email_input.fill(USER)
    page.get_by_role("button", name="Next").click()

    # Enter password
    password_input = page.get_by_label("Enter your password")
    password_input.fill(PASSWORD)
    page.get_by_role("button", name="Next").click()

    # Stop Playwright
    page.pause()
    # Now you take control of the browser window and finish the Google login process (if needed):
    # Two-factor auth
    # Close the browser when the login process has finished

    # Save the browser context
    context.storage_state(path="playwright/.auth/storage_state.json")

    context.close()
