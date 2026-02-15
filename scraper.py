from playwright.sync_api import sync_playwright
from config import TARGET_PAGE, SCROLL_LIMIT
from utils import save_posts_to_csv, log_message
import time

def scrape_posts():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="state.json")
        page = context.new_page()

        log_message("Opening target page")
        page.goto(TARGET_PAGE)
        page.wait_for_timeout(5000)

        # Scroll logic
        for i in range(SCROLL_LIMIT):
            log_message(f"Scrolling {i+1}/{SCROLL_LIMIT}")
            page.mouse.wheel(0, 3000)
            time.sleep(3)

        # Extract posts
        log_message("Extracting posts")
        post_elements = page.query_selector_all("div[role='article']")

        posts = []
        for post in post_elements:
            try:
                text = post.inner_text()
                posts.append(text)
            except:
                continue

        log_message(f"Extracted {len(posts)} posts")

        save_posts_to_csv(posts)

        browser.close()

        log_message("Scraping finished successfully")
