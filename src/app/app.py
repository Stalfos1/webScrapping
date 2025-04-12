from flask import Flask, render_template, jsonify,redirect,url_for
import json
import os
from scraper.scraper_class import Scraper

app = Flask(__name__)

@app.route('/')
def index():
    scraper = Scraper()
    scraper.fetch()
    json_file = 'app\hacker_news.json'
    scraper.save_to_file(json_file)
    
    json_path = os.path.join(json_file)

    if not os.path.exists(json_path):
        return render_template('index.html', entries=[], message="File not found, please run the scraper first.")

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return render_template('index.html', entries=data, message=None)

if __name__ == '__main__':
    app.run(debug=True)