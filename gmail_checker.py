"""
    Check the Gmail inbox
    - Login into the Google account
    - Check the emails
"""
import os

from typing import Final

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, expect

GOOGLE_ACCOUNTS_URL: Final = "https://accounts.google.com"
GOOGLE_MAIL_URL: Final = "https://mail.google.com"


# Get the configuration from the env variables
load_dotenv()
USER=os.getenv("USER")
PASSWORD=os.getenv("PASSWORD")
# print(f"User: {USER}, password: {PASSWORD}")

# Save the Google credentials session
with sync_playwright() as playwright:
    # Use Firefox to get rid of Chrome security problems when loggin into Google
    browser = playwright.firefox.launch(args=["--kiosk"], headless=False)
    context = browser.new_context(viewport={ 'width': 1920, 'height': 1080 })

    page = context.new_page()
    page.goto(GOOGLE_ACCOUNTS_URL)

    # Enter email
    email_input = page.get_by_label("Email or phone")
    email_input.fill(USER)
    page.get_by_role("button", name="Next").click()

    # Enter password
    password_input = page.get_by_label("Enter your password")
    password_input.fill(PASSWORD)
    welcome_locator = page.get_by_role("heading", name="Welcome").locator("span")
    page.get_by_role("button", name="Next").click()

    # Wait for the page to load. Wait for the Gmail "Inicio" element
    expect(welcome_locator).to_be_hidden()

    # Browse to Google mail
    page.goto(GOOGLE_MAIL_URL)
    
    # The Email table in GMAIL page has no user-visible locators :(
    emails = page.locator("div.UI tbody tr")
    print(f"Number of emails: {emails.count()}")

    for email in emails.all():
        # There are two elements, one visible and an invisible one
        print(f"Email subject: {email.locator("td span[data-thread-id]:visible").inner_text()}")

    context.close()
