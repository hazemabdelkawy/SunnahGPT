# This code was written by Hazem Abdelkawy and is licensed under the MIT license.

import requests
from bs4 import BeautifulSoup
import json
import time
import openai
from typing import List
import logging
import os

logging.basicConfig(level=logging.INFO)

class HadithScraper:
    """
    A class to scrape Hadiths from sunnah.com using BeautifulSoup and OpenAI's text-embedding API.

    Attributes:
    -----------
    base_url: str
        The base URL of the website to be scraped
    openai_key: str
        The OpenAI API key
    data_dir: str
        The path to the directory where the scraped data will be saved

    Methods:
    --------
    scrape_website(url: str) -> BeautifulSoup:
        Scrape a website and return the parsed content using BeautifulSoup.

    extract_books(soup: BeautifulSoup) -> list:
        Extract book data from the parsed HTML content of the website.

    extract_hadiths(book_data: dict) -> list:
        Extract hadith data from the parsed HTML content of the book page.

    gpt3_embedding(content: str, engine: str='text-embedding-ada-002') -> list:
        Embed the given text using OpenAI's text-embedding API.

    extract_embedding(text: str) -> list:
        Extract embeddings of the given text using OpenAI's text-embedding API.

    save_to_json(book_data: dict):
        Save the given book data as a JSON file.

    scrape_books() -> list:
        Scrape all the books and their hadiths from the website and save the data as JSON files.
    """

    def __init__(self, base_url: str, openai_key: str, data_dir: str):
        self.base_url = base_url
        self.openai_key = openai_key
        openai.api_key = self.openai_key
        self.data_dir = data_dir
        
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(os.path.join(self.data_dir, 'scraper.log'))
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

    def scrape_website(self, url: str) -> BeautifulSoup:
        """
        Scrape a website and return the parsed content using BeautifulSoup.

        Parameters:
        -----------
        url: str
            The URL of the website to be scraped.

        Returns:
        --------
        soup: BeautifulSoup
            The parsed content of the website using BeautifulSoup.
        """
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def extract_books(self, soup: BeautifulSoup) -> list:
        """
        Extract book data from the parsed HTML content of the website.

        Parameters:
        -----------
        soup: BeautifulSoup
            The parsed content of the website using BeautifulSoup.

        Returns:
        --------
        books_data: list
            A list of dictionaries containing book data.
        """
        self.logger.info('Extracting book data from website...')
        books_containers = soup.find_all(class_='book_title')
        books_data = []
        for container in books_containers:
            book_number = container.find(class_='title_number').get_text(strip=True)
            book_link = f"{self.base_url}/{book_number}"
            book_en_name = container.find(class_='english_book_name').get_text(strip=True)
            book_ar_name = container.find(class_='arabic_book_name').get_text(strip=True)
            books_data.append({
                'book_link': book_link,
                'book_number': book_number,
                'english_name': book_en_name,
                'arabic_name': book_ar_name
            })
        self.logger.info(f'{len(books_data)} books data extracted from website.')
        return books_data

    def extract_hadiths(self, book_data: dict) -> List[dict]:
        """
        Extract hadith data from the parsed HTML content of the book page.

        Parameters:
        -----------
        book_data: dict
            A dictionary containing book data.

        Returns:
        --------
        hadiths_data: List[dict]
            A list of dictionaries containing hadith data.
        """
        self.logger.info(f'Extracting hadith data from book: {book_data["english_name"]}...')
        page = requests.get(book_data['book_link'])
        soup = BeautifulSoup(page.content, 'html.parser')
        hadith_containers = soup.find_all(class_='actualHadithContainer')
        hadiths_data = []
        for idx, container in enumerate(hadith_containers):
            hadith_en_text = container.find(class_='text_details').get_text(strip=True)
            hadith_ar_text = container.find(class_='arabic_hadith_full').get_text(strip=True)
            hadith_ref = container.find(class_='hadith_reference').get_text(strip=True)
            ref_parts = hadith_ref.split('In-book reference:')
            reference = ref_parts[0].strip().replace('Reference:', '')
            book_reference = None
            hadith_number = None
            if len(ref_parts) > 1:
                book_ref_parts = ref_parts[1].strip().split(',')
                book_reference = book_ref_parts[0].strip()
                hadith_number = book_ref_parts[1].strip().split('USC-MSA')[0].strip()
            hadiths_data.append({
                'english': hadith_en_text,
                'arabic': hadith_ar_text,
                'reference': reference,
                'book_reference': book_reference,
                'hadith_number': hadith_number
            })
        self.logger.info(f'Extracted {len(hadiths_data)} hadiths from book: {book_data["english_name"]}.')
        return hadiths_data


    def gpt3_embedding(self, content: str, engine: str='text-embedding-ada-002') -> list:
        """
        Embed the given text using OpenAI's text-embedding API.

        Parameters:
        -----------
        content: str
            The text to be embedded.

        engine: str
            The name of the OpenAI engine to be used for text embedding.

        Returns:
        --------
        vector: list
            The embedding vector of the given text.
        """
        try:
            response = openai.Embedding.create(input=content, engine=engine)
            vector = response['data'][0]['embedding']
            return vector
        except Exception as e:
            self.logger.error(f'Embedding failed. Error message: {e}')


    def extract_embedding(self, text: str) -> list:
        """
        Extract embeddings of the given text using OpenAI's text-embedding API.

        Parameters:
        -----------
        text: str
            The text to be embedded.

        Returns:
        --------
        embedding: list
            The embedding vector of the given text.
        """
        try:
            embedding = self.gpt3_embedding(text)
        except:
            while(True):
                try:
                    if len(text) > 8191:
                        self.logger.warning('[OPENAI ERROR] Trying to get shorter input < 8191 for text...')
                        embedding = self.gpt3_embedding(text[:8191])
                    else:
                        embedding = self.gpt3_embedding(text)
                    break
                except Exception as e:
                    self.logger.error(f'Trying to get the embedding for text. Error message: {e}')
                    time.sleep(5)
        return embedding


    def save_to_json(self, book_data: dict):
        """
        Save the given book data as a JSON file.

        Parameters:
        -----------
        book_data: dict
            A dictionary containing book data to be saved as a JSON file.
        """
        filename = f"{book_data['book_number'].zfill(2)}_{book_data['english_name']}.json"
        filepath = os.path.join(self.data_dir, filename)
        self.logger.info(f'Saving book data to file: {filepath}...')
        with open(filepath, 'w') as f:
            json.dump(book_data, f)
        self.logger.info(f'Book data saved to file: {filepath}.')


    def scrape_books(self) -> List[dict]:
        """
        Scrape all the books and their hadiths from the website and save the data as JSON files.

        Returns:
        --------
        books_data: List[dict]
            A list of dictionaries containing book and hadith data.
        """
        self.logger.info('Scraping started...')
        soup = self.scrape_website(self.base_url)
        books_data = self.extract_books(soup)
        for book_data in books_data:
            self.logger.info(f'Scraping book: {book_data["english_name"]}...')
            hadiths_data = self.extract_hadiths(book_data)
            for hadith_data in hadiths_data:
                hadith_data['english_embeddings'] = self.extract_embedding(hadith_data['english'])
                time.sleep(1)
                hadith_data['arabic_embeddings'] = self.extract_embedding(hadith_data['arabic'])
                time.sleep(1)
            book_data['hadith_data'] = hadiths_data
            self.save_to_json(book_data)
            self.logger.info(f'Finished scraping book: {book_data["english_name"]}.')
        self.logger.info(f'Scraping finished. Scraped {len(books_data)} books.')
        return books_data