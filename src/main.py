from scraper.scraper_class import Scraper

def main():
    scraper = Scraper()
    scraper.fetch(limit=10)

    print(scraper.to_json())
    
    print("\n")
    print("\n"+"********************************")

    filtered_entries = scraper.filter_entries_by_title_words_from_file()
    print("\nFiltered entries (titles > 5 words, sorted by comments):\n")
    for entry in filtered_entries:
        print(entry)

if __name__ == '__main__':
    main()
