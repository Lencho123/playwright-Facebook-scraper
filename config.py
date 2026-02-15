import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("FB_EMAIL")
PASSWORD = os.getenv("FB_PASSWORD")
TARGET_PAGE = os.getenv("TARGET_PAGE")
SCROLL_LIMIT = int(os.getenv("SCROLL_LIMIT", 5))
