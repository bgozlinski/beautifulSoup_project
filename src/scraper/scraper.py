import requests
from bs4 import BeautifulSoup
from src.db.seed import upload_data
import json


def scrape_quotes(page_url, base_url):
    """
    Scrape quotes from a single page and return quotes data along with next page URL.
    """
    quotes_data = []
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]
        author_url = base_url + quote.find('a')['href']

        # Extracting author details
        author_data = scrape_author(author_url)

        quotes_data.append({
            'tags': tags,
            'author': author,
            'quote': text,
            'author_details': author_data
        })

    # Finding the URL of the next page
    next_page = soup.find('li', class_='next')
    next_page_url = base_url + next_page.find('a')['href'] if next_page else None

    return quotes_data, next_page_url


def scrape_author(author_url):
    """
    Scrape author details from the author page.
    """
    response = requests.get(author_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    fullname = soup.find('h3', class_='author-title').text.strip()
    born_date = soup.find('span', class_='author-born-date').text.strip()
    born_location = soup.find('span', class_='author-born-location').text.strip()
    description = soup.find('div', class_='author-description').text.strip()

    return {
        'fullname': fullname,
        'born_date': born_date,
        'born_location': born_location,
        'description': description
    }
