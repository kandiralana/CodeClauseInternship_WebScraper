from news_web_scraper import NewsScraper


def main():
    """
    Main function to run the news web scraper.

    1. Creates a NewsScraper object for the specified URL.
    2. Scrapes news information from the webpage.
    3. Prints the processed news information.

    :return: None
    """
    url = 'https://globalnews.ca/world/'

    news_scraper = NewsScraper(url)
    news_scraper.scrape_news()
    news_scraper.print_news()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
