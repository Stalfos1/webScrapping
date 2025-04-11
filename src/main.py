from scraper.scraper_class import Scraper

def main():
    scraper = Scraper()
    scraper.fetch(limit=30)
    json_file='src\hacker_news.json'
    print(scraper.to_json())
    
    print("\n")
    print("\n"+"********************************")

    filtered_entries = scraper.filter_entries_by_title_words_from_file(json_file)
    print("\nFiltered entries (titles > 5 words, sorted by comments):\n")
    for entry in filtered_entries:
        print(entry)
       
         
    print("\n")
    print("\n"+"********************************")

        
    short_titles = scraper.filter_entries_with_short_titles_by_score(json_file)
    for entry in short_titles:
        print(entry)

if __name__ == '__main__':
    main()
