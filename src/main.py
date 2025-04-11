from scraper.scraper_class import Scraper

def main():
    scraper = Scraper()
    scraper.fetch(limit=10)

    print(scraper.to_json())

    scraper.save_to_file()

if __name__ == '__main__':
    main()
