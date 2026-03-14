import os
import requests
import pandas as pd
from datetime import datetime


# -------------------------------
# Configuration
# -------------------------------
TOP_STORIES_API = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_API = "https://hacker-news.firebaseio.com/v0/item/{}.json"

TOP_N = 10
SAVE_FOLDER = "API_SAVED_FILES"


# -------------------------------
# Get Top Story IDs
# -------------------------------
def get_top_story_ids():

    try:
        response = requests.get(TOP_STORIES_API, timeout=10)
        response.raise_for_status()

        story_ids = response.json()

        return story_ids

    except requests.exceptions.RequestException as e:

        print("Error fetching top stories:", e)

        return []


# -------------------------------
# Get Story Details
# -------------------------------
def get_story_details(story_id):

    try:
        url = ITEM_API.format(story_id)

        response = requests.get(url, timeout=10)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        print(f"Error fetching story {story_id}:", e)

        return None


# -------------------------------
# Extract Stories
# -------------------------------
def extract_stories():

    print("Fetching top story IDs...")

    story_ids = get_top_story_ids()

    if not story_ids:

        print("No story IDs received")

        return []

    stories = []

    for rank, story_id in enumerate(story_ids[:TOP_N], start=1):

        story = get_story_details(story_id)

        if story is None:
            continue

        title = story.get("title", "N/A")

        author = story.get("by", "N/A")

        score = story.get("score", 0)

        url = story.get("url", "N/A")

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

    if not data:

        print("No data to save")

        return

    os.makedirs(SAVE_FOLDER, exist_ok=True)

    df = pd.DataFrame(data, columns=["Rank", "Title", "Author", "Score", "URL"])

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"top_stories_api_{timestamp}.xlsx"

    filepath = os.path.join(SAVE_FOLDER, filename)

    df.to_excel(filepath, index=False)

    print(f"\nSaved file: {filepath}")


# -------------------------------
# Main Function
# -------------------------------
def main():

    print("Starting API extraction...\n")

    stories = extract_stories()

    save_to_excel(stories)

    print("\nExtraction completed successfully.")


if __name__ == "__main__":
    main()