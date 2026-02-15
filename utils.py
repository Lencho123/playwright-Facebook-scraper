import csv
import os
from datetime import datetime

def log_message(message):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {message}\n")

def save_posts_to_csv(posts):
    os.makedirs("data", exist_ok=True)
    file_path = "data/posts.csv"

    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Post Text"])

        for post in posts:
            writer.writerow([post])
