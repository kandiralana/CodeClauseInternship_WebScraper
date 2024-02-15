from news_web_scraper import NewsScraper

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = 'https://globalnews.ca/world/'

    news_scraper = NewsScraper(url)
    news_scraper.scrape_news()
    news_scraper.print_news()
