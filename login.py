from playwright.sync_api import sync_playwright
from config import EMAIL, PASSWORD

def login_and_save():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.facebook.com")

        page.fill("#email", EMAIL)
        page.fill("#pass", PASSWORD)
        page.keyboard.press("Enter")

        page.wait_for_timeout(10000)

        context.storage_state(path="state.json")

        browser.close()

if __name__ == "__main__":
    login_and_save()
