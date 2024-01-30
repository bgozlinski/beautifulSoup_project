
# Quotes Scraper Project

## Description
The 'Quotes Scraper' project is an application for scraping quotes and author information from [http://quotes.toscrape.com](http://quotes.toscrape.com). The project collects data, saves it in JSON format, and facilitates loading it into a database.

## Project Structure
```
src/
├── db/
│   ├── connect_db.py   # Script for connecting to the database
│   ├── models.py       # Database model definitions
│   └── seed.py         # Script for seeding the database with data
│
├── scraper/
│   └── scraper.py      # Script for scraping data
│
├── json/
│   ├── authors.json    # JSON data of authors
│   └── quotes.json     # JSON data of quotes
│
├── load_dotenv.py      # Script for loading environment variables
│
└── main.py             # Main file to start scripts

```

## Requirements
- Python 3.x
- BeautifulSoup
- requests

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python src/main.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


