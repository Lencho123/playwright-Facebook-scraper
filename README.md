# playwright-Facebook-scraper
A structured Playwright-based browser automation project for collecting public Facebook page posts and saving them to CSV.

Playwright Facebook Scraper

A structured Playwright-based browser automation project for collecting public Facebook page posts and saving them to CSV.

⚠️ This project is for educational and research purposes only. Use responsibly and respect platform terms and applicable laws.

📌 Features

Automated browser control using Playwright

Secure login with saved session (state.json)

Configurable target page

Controlled scrolling logic

Post extraction

CSV export

Logging system

Clean production-style structure

📁 Project Structure
playwright_facebook/
│
├── main.py              # Entry point
├── login.py             # One-time login session creator
├── scraper.py           # Core scraping logic
├── config.py            # Environment config loader
├── utils.py             # Logging + CSV utilities
├── .env                 # Environment variables
├── state.json           # Saved login session (auto-generated)
├── logs.txt             # Log file
└── data/
     └── posts.csv       # Scraped data output

⚙️ Requirements

Python 3.8+

Playwright

python-dotenv

🔧 Installation

Clone or create the project folder.

Install dependencies:

pip install playwright python-dotenv


Install Playwright browsers:

playwright install

🔐 Environment Configuration

Create a .env file in the root folder:

FB_EMAIL=your_email
FB_PASSWORD=your_password
TARGET_PAGE=https://www.facebook.com/somepublicpage
SCROLL_LIMIT=5

Variables Explained

FB_EMAIL – Your Facebook login email

FB_PASSWORD – Your Facebook login password

TARGET_PAGE – Public page to scrape

SCROLL_LIMIT – Number of scroll iterations

🚀 Usage
Step 1 — Login and Save Session (First Time Only)
python login.py


This will:

Open browser

Log in

Save session to state.json

Step 2 — Run Scraper
python main.py


This will:

Load saved session

Open target page

Scroll

Extract posts

Save to data/posts.csv

Log activity in logs.txt

📊 Output
CSV File

Saved at:

data/posts.csv


Contains:

Post Text

Logs

Saved at:

logs.txt


Includes:

Start time

Scroll actions

Number of extracted posts

Errors (if any)

🛡 Responsible Usage Guidelines

Scrape only publicly available data

Avoid aggressive automation

Do not overload servers

Respect privacy and platform policies

Use for research and learning purposes

🧠 Possible Improvements

Extract post timestamps

Extract likes and comments count

Deduplicate posts

Store in database (PostgreSQL / MongoDB)

Convert to async_playwright for performance

Add scheduler (cron / task scheduler)

Containerize with Docker

📌 Tech Stack

Python

Playwright (Chromium)

CSV for storage

dotenv for configuration

⚠️ Disclaimer

This project does not bypass security systems or attempt to evade platform protections.
Users are responsible for ensuring compliance with applicable terms of service and local laws.

👨‍💻 Author

Lencho Lachisa Nagasa
Playwright Automation Project