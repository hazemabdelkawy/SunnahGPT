## Abstract
SunnahGPT is a natural language processing (NLP) project aimed at scraping hadith data from the popular website sunnah.com and applying OpenAI's GPT-3.5 model to generate textual embeddings for each hadith. The project is designed to provide researchers and developers with a comprehensive and structured dataset of hadiths, complete with accurate Arabic and English translations, reference information, and GPT-3.5 embeddings. We believe that SunnahGPT represents a significant step forward in the field of NLP and Islamic studies, providing researchers with a powerful tool for analyzing and understanding hadith literature.

## Introduction
Hadith literature is an essential source of Islamic jurisprudence and theology, offering insights into the teachings of the Prophet Muhammad (PBUH) and the early Islamic community. Despite its importance, hadith literature remains challenging to study and analyze, particularly given the sheer volume of texts and the complexity of the Arabic language. In recent years, natural language processing (NLP) has emerged as a powerful tool for analyzing text data, offering researchers new ways to uncover insights and patterns in large datasets.

SunnahGPT is a project that leverages NLP techniques to extract and analyze hadith data from sunnah.com. The project applies OpenAI's GPT-3.5 model to generate textual embeddings for each hadith, providing researchers with a powerful tool for studying and analyzing hadith literature. The project also provides a comprehensive and structured dataset of hadiths, complete with accurate Arabic and English translations, reference information, and GPT-3.5 embeddings.

SunnahGPT represents a significant step forward in the field of NLP and Islamic studies, providing researchers with a powerful tool for analyzing and understanding hadith literature. We believe that this project has significant potential for advancing research in this area and facilitating new insights into the teachings of the Prophet Muhammad (PBUH) and the early Islamic community.

## SunnahGPT Embeddings for NLP projects

This is a Python script to scrape hadiths from sunnah.com and save the extracted data in JSON files. The script uses BeautifulSoup to parse HTML content and OpenAI's text-embedding API to embed the hadiths' text.


## Project Structure

The project consists of the following files:

- main.py: The main file to run the program.
- scraper.py: A file containing the HadithScraper class to scrape hadiths from sunnah.com.
- config.py: A file containing the OpenAI API key.
- README.md: A file containing the project description and usage instructions.

## Requirements
The project requires the following dependencies to be installed:

- requests: To fetch the content of web pages.
- BeautifulSoup: To parse and extract data from HTML.
- json: To convert data to JSON format.
- time: To set time intervals between requests.
- openai: To use OpenAI's text-embedding API.

You can install these dependencies by running the following command in your - terminal or command prompt:

```console
user@machine:~$ pip install requests beautifulsoup4 openai
```

## Usage

To use the project, follow these steps:

- Clone or download the project from GitHub.
- Open config.py and enter your OpenAI API key.
- In main.py, specify the main URL of sunnah.com and the directory where the extracted data will be saved.
- Run the following command 

```console
user@machine:~$ python main.py
```
## Collected data
1- Sahih AL Bukhari : https://drive.google.com/drive/folders/1NSOnadQcnDkL-kEFjPFWelp9VYsy1gwu?usp=share_link

## License
This project is licensed under the MIT License.