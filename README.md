# Python solution that extracts the same data from a website

## 1. Project Overview

This project demonstrates two different Method approaches for extracting data from the Hacker News website.

The same information is extracted using:

(1) via its publicly reachable JSON API 
(2) via traditional HTML scraping using tools like selenium, requests etc.

The goal of the project is to collect the **Top N stories from Hacker News** and store the extracted data into Excel files.

---

# 2. Website Used

The data is extracted from the Hacker News homepage.

Website:

Front page HTML:- https://news.ycombinator.com/

Official Hacker News API:

JSON API (no auth):- https://hacker-news.firebaseio.com/v0

API Endpoints used in this project:

Top stories endpoint

https://hacker-news.firebaseio.com/v0/topstories.json → array of IDs

Story details endpoint

https://hacker-news.firebaseio.com/v0/item/id.json → includes title, by, score, url

---

# 3. Information Extracted

For each story the following fields are extracted:

Rank  
Title  
Author  
Score  
URL  

Example:

| Rank | Title | Author | Score | URL |
|-----|------|------|------|------|
| 1 | Show HN: Channel Surfer | kilroy123 | 277 | https://channelsurfer.tv |

---

# 4. Project Structure

Interview/

Method_1_API  
- api_extract.py  
- API_SAVED_FILES  

Method_2_Selenium  
- selenium_extract.py  
- SELENIUM_SAVED_FILES  

README.md  
requirements.txt 


Explanation of files:

api_extract.py  
Script that extracts the top stories using the Hacker News API.

selenium_extract.py  
Script that scrapes the Hacker News website using Selenium.

requirements.txt  
Contains all required Python libraries.

README.md  
Documentation explaining how to run the project.

API_SAVED_FILES  
Stores Excel files generated from API extraction.

SELENIUM_SAVED_FILES  
Stores Excel files generated from Selenium scraping.

---

# 5. Requirements

Before running the project, install the following:

Python 3.8 or higher

Google Chrome Browser

Python libraries listed in requirements.txt

---
# 6. Setup and Run Instructions

Follow the steps below to run the project on your system.

---

## Step 1: Open Command Prompt

Open **Command Prompt (CMD)** and navigate to the project folder.

Example:

```bash
cd Interview
```
---

## Step 2: Create Python Virtual Environment

Run the following command to create the virtual environment inside the Interview folder.

```bash
python -m venv .
```

After this step, the folders **Scripts, Lib, and pyvenv.cfg** will be created.

---

## Step 3: Activate the Virtual Environment

Activate the virtual environment using:

```bash
Scripts\activate
```

After activation, the command prompt should show the environment name.

---

## Step 4: Install Required Libraries

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The main libraries used are:

requests  
pandas  
selenium  
openpyxl  

---

# Running Method 1 (API Extraction)

Navigate to the Method 1 folder in cmd:

```bash
cd Method_1_API
```

Run the script:

```bash
python api_extract.py
```

What this script does:

- Calls the Hacker News API
- Retrieves the top story IDs
- Fetches story details
- Extracts title, author, score, and URL
- Saves the results into an Excel file

Output Files will be saved in:

API_SAVED_FILES/

Example output file:

top_stories_api_20260315_104500.xlsx

---

# For Running Method 2 (Selenium Web Scraping)

Navigate to the Selenium folder in cmd:

```bash
cd Method_2_Selenium
```

Run the script:

```bash
python selenium_extract.py
```

What this script does:

- Opens the Hacker News homepage using Selenium
- Reads the top N stories displayed on the page
- Extracts title, author, score, and URL
- Saves the results into an Excel file

Output Files will be saved in:

SELENIUM_SAVED_FILES/

Example output file:

top_stories_selenium_20260315_105300.xlsx



---

# 7. Difference Between the Two Methods

| Method | Data Source | Technology Used |
|------|------|------|
| API Extraction | Hacker News API | requests |
| Selenium Extraction | Hacker News Website | Selenium |

API extraction retrieves structured JSON data directly from the server.

Selenium extraction scrapes the HTML webpage using browser automation.

Both methods collect the same information but use different techniques.

---

# 8. Error Handling

The scripts include basic error handling to manage:

Network request failures

Missing story fields

Directory creation if folders do not exist

File overwriting by using timestamps

---

# 9. Output Example

Example extracted data stored in Excel:

| Rank | Title | Author | Score | URL |
|-----|------|------|------|------|
| 1 | Show HN: Channel Surfer | kilroy123 | 277 | https://channelsurfer.tv |
| 2 | Can I run AI locally? | ricardbejarano | 638 | https://example.com |

---

# 10. Summary

This project demonstrates two important techniques used in data extraction:

API based data retrieval

Web scraping using Selenium

The same dataset is collected using two different methods to show the difference between API extraction and browser-based scraping.

Both approaches successfully extract the top N Hacker News stories and save them into Excel files for further analysis.





