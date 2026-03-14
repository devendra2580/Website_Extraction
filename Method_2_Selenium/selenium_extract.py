import os
import pandas as pd
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# -------------------------------
# Configuration
# -------------------------------
URL = "https://news.ycombinator.com/"
TOP_N = 10
SAVE_FOLDER = "SELENIUM_SAVED_FILES"


# -------------------------------
# Setup WebDriver
# -------------------------------
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


# -------------------------------
# Extract Stories
# -------------------------------
def extract_stories(driver):

    driver.get(URL)

    # wait until stories are loaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "tr.athing"))
    )

    stories = []

    # story rows
    rows = driver.find_elements(By.CSS_SELECTOR, "tr.athing")

    for rank, row in enumerate(rows[:TOP_N], start=1):

        # title + link
        title_element = row.find_element(By.CSS_SELECTOR, ".titleline a")
        title = title_element.text
        url = title_element.get_attribute("href")

        # metadata row (next row after story row)
        metadata = row.find_element(By.XPATH, "following-sibling::tr[1]")

        # author
        try:
            author = metadata.find_element(By.CLASS_NAME, "hnuser").text
        except:
            author = "N/A"

        # score
        try:
            score_text = metadata.find_element(By.CLASS_NAME, "score").text
            score = score_text.split()[0]  # remove "points"
        except:
            score = "0"

        stories.append({
            "Rank": rank,
            "Title": title,
            "Author": author,
            "Score": score,
            "URL": url
        })

    return stories


# -------------------------------
# Save to Excel
# -------------------------------
def save_to_excel(data):

    os.makedirs(SAVE_FOLDER, exist_ok=True)

    df = pd.DataFrame(data, columns=["Rank", "Title", "Author", "Score", "URL"])

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"top_stories_selenium_{timestamp}.xlsx"

    filepath = os.path.join(SAVE_FOLDER, filename)

    df.to_excel(filepath, index=False)

    print(f"\nSaved file: {filepath}")


# -------------------------------
# Main Function
# -------------------------------
def main():

    print("Starting Selenium extraction...\n")

    driver = setup_driver()

    try:
        stories = extract_stories(driver)
        save_to_excel(stories)

    finally:
        driver.quit()

    print("\nExtraction completed successfully.")


if __name__ == "__main__":
    main()