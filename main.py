# This code was written by Hazem Abdelkawy and is licensed under the MIT license.

from src.scraper import HadithScraper
from src.config import OPENAI_KEY

if __name__ == '__main__':
    base_url = 'https://sunnah.com/bukhari'
    scraper = HadithScraper(base_url, OPENAI_KEY, data_dir="./Bukhari")
    books_data = scraper.scrape_books()