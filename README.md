# News Web Scraper

## Table of Contents

- [Installation](#installation)
- [Overview](#overview)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
  - [main.py](#mainpy)
  - [news_web_scraper.py](#news_web_scraperpy)
- [Dependencies](#dependencies)
- [Disclaimer](#disclaimer)

## Installation

1. Clone the repository: `git clone https://github.com/kandiralana/CodeClauseInternship_WebScraper.git`
2. Navigate to the project directory: `cd CodeClauseInternship_WebScraper`

## Overview

This Python script (`main.py`) utilizes a news web scraper (`news_web_scraper.py`) to extract and process news information from a specified URL. The web scraper is designed to work with the HTML structure of the Global News website (`https://globalnews.ca/world/`).

## Usage

1. Ensure you have the required dependencies installed by running:

    ```bash
    pip install beautifulsoup4 requests
    ```

2. Run the `main.py` script to execute the news web scraper. The script performs the following steps:

    - Creates a `NewsScraper` object for the specified URL.
    - Scrapes news information from the webpage.
    - Prints the processed news information.

    ```bash
    python main.py
    ```

## File Descriptions

### main.py

- `main()`: The main function to run the news web scraper.
  - Creates a `NewsScraper` object for the specified URL.
  - Scrapes news information from the webpage.
  - Prints the processed news information.

### news_web_scraper.py

- `get_page_to_scrap(p_url)`: Creates a session and retrieves the HTML content from the specified URL.
- `find_news_headline(container)`: Extracts the news headline from the HTML container.
- `find_news_date(container)`: Extracts the news date from the HTML container.
- `find_news_link(container)`: Extracts the news link from the HTML container.
- `get_current_time()`: Gets the current time in a formatted string.
- `NewsScraper`: Class to initialize the news scraper object and perform news scraping.

## Dependencies

- `BeautifulSoup` for HTML parsing.
- `requests` for handling HTTP requests.

## Disclaimer

This script is designed to work with the specific HTML structure of the Global News website as of the last knowledge update in January 2022. Any changes to the website structure may require modifications to the code for proper functionality. Use responsibly and in accordance with the website's terms of service.
