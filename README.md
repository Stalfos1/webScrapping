# WebScrapping
## Overview
This project is a web application that scrapes the top 30 entries from Hacker News and presents them through an interface. Built with Python, Flask and BeautifulSoup.

## 🚀 Features

* **Web Scraping:** Fetches the top 30 entries from Hacker News using BeautifulSoup.
* **Pagination:** Displays the first 12 entries by default, with an option to view all entries.
* **Filtering:** Provides buttons to filter titles based on word count (more than 5 words or 5 words or fewer).
* **Search Functionality:** Implements a dynamic search to filter entries by rank, title, score, or comments.
* **UI:** Includes hover effects on table rows for improved user experience.
* **Modular JavaScript:** Separates search logic into an external `filter.js` file for better code organization.


## 📁 Project Structure
The project's source (src) directory contains the following:

### ├── app/
### │   ├── static/
### │       └── filter.js
### │       └── style.css
### │   ├── templates/
### │       └── index.html
### │   └── app.py
###
### ├── scraper/
### │   └── scraper.py
###
### ├── tests/
### │   └── test_scraper.py

### `src/app/`
Contains the core of the Flask web application:
* `app.py`: Initializes the Flask application.
* `static`: Contains the css styles and the JavaScript code
* `templates/`: Holds the HTML template files used to render the web pages.

### `src/scraper/`

Data scraping logic:

* `scraper_class.py`: Contains the `Scraper` class, responsible for fetching data from Hacker News and parsing it into a usable format.

  
### `src/tests/`

Contains the project's test suite:

* `test_scraper.py`: Includes test cases written using the `pytest` framework to verify the functionality and correctness of the `Scraper` class.
