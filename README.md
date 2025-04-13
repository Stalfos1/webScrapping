# WebScrapping
## Overview
This project is a web application that scrapes the top 30 entries from Hacker News and presents them through an interface. Built with Python, Flask and BeautifulSoup.

## 🔗 Deployment
The application is deployed on **Render** and can be accessed at:

👉 [Render](https://webscrapping-tjoi.onrender.com/)

## 🚀 Features

* **Web Scraping:** Fetches the top 30 entries from Hacker News using BeautifulSoup.
* **Pagination:** Displays the first 12 entries by default, with an option to view all entries.
* **Filtering:** Provides buttons to filter titles based on word count (more than 5 words or 5 words or fewer).
* **Search Functionality:** Implements a dynamic search to filter entries by rank, title, score, or comments.
* **UI:** Includes hover effects on table rows for improved user experience.
* **Modular JavaScript:** Separates search logic into an external `filter.js` file for better code organization.


## 📁 Project Structure
The project's source (src) directory contains the following:

* `app/`
    * `static/`
        * `filter.js`
        * `style.css`
    * `templates/`
        * `index.html`
    * `app.py`
* `scraper/`
    * `scraper.py`
* `tests/`
    * `test_scraper.py`
* `README.md`

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


## 🛠️ Installation


1.  Clone the repository:
    ```bash
    git clone https://github.com/Stalfos1/webScrapping.git
    cd src
    ```

2.  **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS and Linux
    venv\Scripts\activate  # On Windows
    ```

3.  Install the project dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    **The `requirements.txt` file list all dependencies like Flask, requests, beautifulsoup4, pytest, etc.)**



## 🕹️ Usage

1.  **For the web application:** Navigate to the project directory and run the Flask application:
    ```bash
    cd src
    python -m app.app   
    ```
    Then, open your web browser and go to `http://127.0.0.1:5000/` (default), or the address provided in the terminal.
    ### Using the web Application:

    Once the web application is running, you will see a page displaying the scraped data from Hacker News in a table format, showing the Rank, Title, Score, and Comments for each entry.

    * **Filter Buttons:** Above the table, you'll find three buttons:
        * **`No filters`:** Clicking this button will display the initial set of entries (the first 12 by default). It removes any active filters.
        * **`Titles with more than 5 Words`:** Clicking this button will filter the displayed entries to show only those news titles that contain more than five words. The results will be ordered by the number of comments, with the most commented articles appearing first. A message will appear indicating that this filter is active.
        * **`Titles less than or equal to 5 words`:** Clicking this button will filter the displayed entries to show only those news titles that contain five words or fewer. The results will be ordered by their score (points), with the highest-scoring articles appearing first. A message will appear indicating that this filter is active.

    * **Search Bar:** Below the filter buttons, there is a search bar labeled "Search titles...". You can type keywords into this bar to dynamically filter the displayed entries based on the text in the **Rank**, **Title**, **Score**, or **Comments** columns. As you type, the table will update in real-time to show only the entries that match your search query.

    * **Show All Entries Button:** Below the table (if not all entries are initially displayed), you will find a button that says "Show All Entries (XX)", where "XX" is the total number of scraped entries. Clicking this button will load and display all the scraped entries on the page, overriding the initial limit of 12. If a filter is active when you click "Show All Entries", the filter will still be applied to the complete list.


3.  **For the scraper as a standalone module:** You can use the `Scraper` class and test it in the src/main.py file or you can import it as:
    ```python
    from scraper.scraper_class import Scraper

    scraper = Scraper()
    data = scraper.fetch()
    ```
4. **Scraper Fetch Override:** The `fetch()` method in the `Scraper` class allows you to specify the number of entries to scrape. By default, calling `fetch()` without any arguments will retrieve the top 30 entries. To scrape a different number, simply pass the desired count as an argument:
      ```python
    from scraper.scraper_class import Scraper

    scraper = Scraper()
    data = scraper.fetch()
    data = scraper.fetch(10)
    data = scraper.fetch(40)
    ```
5.  **Title Word Count Filtering (Internal Methods):**

    The `Scraper` class includes internal helper methods to determine the number of words in a news title for filtering purposes:

    * **`_title_has_five_or_fewer_words(self, title)`:**
        * Takes a `title` string as input.
        * Removes any non-alphanumeric characters and whitespace using regular expressions (`re.sub(r'[^\w\s]', ' ', title)`).
        * Splits the cleaned title into a list of `words` based on whitespace.
        * Returns `True` if the number of words in the `title` is less than or equal to 5, and `False` otherwise (`return len(words) <= 5`).

    * **`_title_has_more_than_five_words(self, title)`:**
        * Takes a `title` string as input.
        * Performs the same cleaning and splitting of the `title` into `words` as the `_title_has_five_or_fewer_words` method.
        * Returns `True` if the number of words in the `title` is greater than 5, and `False` otherwise (`return len(words) > 5`).

    These methods are used internally by the `filter_entries_by_title_words_from_file` and `filter_entries_with_short_titles_by_score` methods to categorize news entries based on their title length.

## 🧪 Testing

1.  Ensure you have `pytest` installed (If you didn't use `pip install -r requirements.txt`, you'll need to install it manually).
2.  Navigate to the project's root directory.
3.  Run the tests using the `pytest` command:
    ```bash
    pytest -v
    ```
