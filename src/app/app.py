from flask import Flask, render_template,request, jsonify,redirect,url_for
import json
import os
from scraper.scraper_class import Scraper

app = Flask(__name__)

@app.route('/')
def index():
    filter_type = request.args.get('filter', 'all')
    scraper = Scraper()
    scraper.fetch()
    json_file = 'app\hacker_news.json'
    scraper.save_to_file(json_file)
    
    json_path = os.path.join(json_file)

    if not os.path.exists(json_path):
        return render_template('index.html', entries=[], message="File not found, please run the scraper first.")

    if filter_type == 'long':
        entries = scraper.filter_entries_by_title_words_from_file(json_path)
        message = "Filtered: Titles with more than 5 words, ordered by the number of comments first"
    elif filter_type == 'short':
        entries = scraper.filter_entries_with_short_titles_by_score(json_path)
        message = "Filtered: Titles with 5 or fewer words, ordered by points"
    else:
        with open(json_path, 'r', encoding='utf-8') as f:
            entries = json.load(f)
        message = None

    return render_template('index.html', entries=entries, message=message)

if __name__ == '__main__':
    app.run(debug=True)