from src.scraper.scraper import scrape_quotes
from src.db.seed import upload_data
import json

base_url = "http://quotes.toscrape.com"


def main():
    """
    Main function to initiate scraping process.
    """
    all_quotes = []
    next_page_url = base_url + "/page/1"

    while next_page_url:
        print(f"Scraping page {next_page_url}")
        quotes, next_page_url = scrape_quotes(next_page_url, base_url)
        all_quotes.extend(quotes)

    # Writing quotes data to JSON file
    with open('../src/json/quotes.json', 'w') as file:
        json.dump(all_quotes, file, indent=4)

    # Extracting unique authors and writing to JSON file
    authors = {quote['author']: quote['author_details'] for quote in all_quotes}
    with open('../src/json/authors.json', 'w') as file:
        json.dump(list(authors.values()), file, indent=4)

    upload_data()


if __name__ == '__main__':
    main()
