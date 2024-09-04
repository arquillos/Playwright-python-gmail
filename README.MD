# Checking the GMAIL inbox with Playwright and Python example

The goal of this repository is to check the Gmail inbox for new mails using Python and Playwright.


## Installation
    $ python -m venv venv
    $ .\venv\Scripts\activate
    $ pip install -r requirements.txt
    $ mkdir -p playwright/.auth
    $ mv .env_template .env
    $ playwright install firefox

Edit the ".env" file and set up your Google account user and password

## Scripts execution
### Login into Google account
Objetive: Store the credentials for reuse
    $ .\venv\Scripts\activate
    $ python get_google_creds.py 

### Check the GMail inbox
    $ .\venv\Scripts\activate
    $ python gmail_checker.py
