# WebScrapping
## Overview
This project is a web application that scrapes the top 30 entries from Hacker News and presents them through an interface. Built with Python, Flask and BeautifulSoup.

## Project Structure
The project's source (src) directory contains the following:

├── app/
│   ├── static/
│       └── filter.js
│       └── style.css
│   ├── templates/
│       └── index.html
│   └── app.py

├── scraper/
│   └── scraper.py

├── tests/
│   └── test_scraper.py

### `src/app/`
Contains the core of the Flask web application:
* `app.py`: Initializes the Flask application.
* `static`: Contains the css styles and the JavaScript code
* `templates/`: Holds the HTML template files used to render the web pages.

### `src/scraper/`

Data scraping logic:

* `scraper_class.py`: Contains the `Scraper` class, responsible for fetching data from Hacker News and parsing it into a usable format.

Contains the project's test suite:

* `test_scraper.py`: Includes test cases written using the `pytest` framework to verify the functionality and correctness of the `Scraper` class.
