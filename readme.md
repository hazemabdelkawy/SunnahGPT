
# Hadith dataset builder with GPT3 Embeddings for NLP projects

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

## License
This project is licensed under the MIT License.