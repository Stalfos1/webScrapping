import requests
from bs4 import BeautifulSoup
import json
import re

class Scraper:
    def __init__(self, url='https://news.ycombinator.com/'):
        self.url = url
        self.entries = []

    def fetch(self):
        response = self._make_request()
        soup = BeautifulSoup(response.text, 'html.parser')
        title_elements = self._extract_title_elements(soup)

        for i, element in enumerate(title_elements, start=1):
            entry = self._process_entry(element, i)
            self.entries.append(entry)
    
    def fetch(self, limit=30):
        response = self._make_request()
        soup = BeautifulSoup(response.text, 'html.parser')
        title_elements = self._extract_title_elements(soup)

        for i, element in enumerate(title_elements[:limit], start=1):
            entry = self._process_entry(element, i)
            self.entries.append(entry)
        

    def _make_request(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise ConnectionError(f"Failed to access the page. Status code: {response.status_code}")
        return response

    def _extract_title_elements(self, soup):
        return soup.find_all('tr', class_='athing')

    def _process_entry(self, element, rank):
        title = self._get_title(element)
        score = self._get_score(element)
        comments = self._get_comments(element)

        return {
            'rank': rank,
            'title': title,
            'score': score,
            'comments': comments
        }

    def _get_rank(self, element):
        rank_tag = element.find('span', class_='rank')
        if rank_tag:
            match = re.search(r'\d+', rank_tag.get_text(strip=True))
            return int(match.group()) if match else None
        return None

    def _get_title(self, element):
        titleline = element.find('span', class_='titleline')
        if titleline:
            link = titleline.find('a')
            return link.get_text(strip=True) if link else 'Titleless'
        return 'Titleless'

    def _get_score(self, element):
        next_row = element.find_next_sibling('tr')
        subtext = next_row.find('td', class_='subtext') if next_row else None
        score_tag = subtext.find('span', class_='score') if subtext else None
        return score_tag.get_text(strip=True) if score_tag else '0 points'

    def _get_comments(self, element):
        next_row = element.find_next_sibling('tr')
        subtext = next_row.find('td', class_='subtext') if next_row else None
        comment_links = subtext.find_all('a') if subtext else []
        comments_text = comment_links[-1].get_text(strip=True) if comment_links else 'No comments'
        comments_text = comments_text.replace('\xa0', ' ').strip() #Cleaning of \xa0 characters
        return comments_text if 'comment' in comments_text else '0 comments'
    
###########################
##Filter all previous entries with more than five words in the title, ordered by the number of comments first.
###########################

    def _clean_title(self, title):
        return re.sub(r'\s*\([^)]*\)\s*$', '', title).strip()
    
    def filter_entries_by_title_words_from_file(self, filename='hacker_news.json'):
        data = self._load_json_file(filename)
        if not data:
            return []

        filtered = []
        for entry in data:
            clean_title = self._clean_title(entry['title'])
            if self._title_has_more_than_five_words(clean_title):
                entry['title'] = clean_title
                filtered.append(entry)

        filtered.sort(key=lambda x: self._extract_comment_count(x['comments']), reverse=True)
        return filtered

    def _load_json_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            print(f"Could not decode JSON from '{filename}'.")
        return []

    def _title_has_more_than_five_words(self, title):
        clean_title = re.sub(r'[^\w\s]', ' ', title)
        words = clean_title.strip().split()
        return len(words) > 5

    def _extract_comment_count(self, comments_text):
        match = re.search(r'\d+', comments_text)
        return int(match.group()) if match else 0
    
###########################
##Filter all previous entries with less than or equal to five words in the title, ordered by points.
###########################

   
    def filter_entries_with_short_titles_by_score(self, filename='hacker_news.json'):
        data = self._load_json_file(filename)
        if not data:
            return []

        filtered = []
        for entry in data:
            clean_title = self._clean_title(entry['title'])
            if self._title_has_five_or_fewer_words(clean_title):
                entry['title'] = clean_title
                filtered.append(entry)

        filtered.sort(key=lambda x: self._extract_score(x['score']), reverse=True)
        return filtered

    def _title_has_five_or_fewer_words(self, title):
        clean_title = re.sub(r'[^\w\s]', ' ', title)
        words = clean_title.strip().split()
        return len(words) <= 5

    def _extract_score(self, score_text):
        match = re.search(r'\d+', score_text)
        return int(match.group()) if match else 0

    
 #############################################
 #Saving the scraping in a Json object
 #############################################
    
    def to_json(self):
        return json.dumps(self.entries, indent=4)

    def save_to_file(self, filename='hacker_news.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.entries, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {filename}")


