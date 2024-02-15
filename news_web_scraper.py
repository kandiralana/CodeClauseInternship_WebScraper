from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import time


def get_page_to_scrap(p_url):
    """
    Create a session and retrieve the HTML content from the specified URL.

    :param p_url: The URL to scrape.
    :return: HTML content of the page.
    """
    with requests.Session() as session:
        try:
            response_from_url = session.get(p_url)
            response_from_url.raise_for_status()
            if response_from_url.status_code not in [200, 399]:
                raise HTTPError
        except HTTPError as http_err:
            print('HTTP error has occurred.', http_err)
        except Exception as ex:
            print('Error has occurred.', ex)
    return response_from_url


def find_news_headline(container):
    """
    Extract the news headline from the HTML container.

    :param container: HTML container containing the news information.
    :return: News headline if found, else None.
    """
    headline_span = container.find('span', class_='c-posts__headlineText')
    if headline_span:
        return headline_span.get('title')
    else:
        headline_a = container.find('a', class_='c-posts__inner')
        return headline_a.get('title') if headline_a else None


def find_news_date(container):
    """
    Extract the news date from the HTML container.

    :param container: HTML container containing the news information.
    :return: News date if found, else 'Date'.
    """
    news_date = container.findAll('div', class_='c-posts__info')
    return news_date[1].text if news_date else 'Date'


def find_news_link(container):
    """
    Extract the news link from the HTML container.

    :param container: HTML container containing the news information.
    :return: News link if found, else None.
    """
    news_link = container.find('a', href=True)
    return news_link.get('href') if news_link else None


def get_current_time():
    """
    Get the current time in a formatted string.

    :return: Formatted current time.
    """
    current_time = time.time()
    time_struct = time.gmtime(current_time)
    formatted_time = time.strftime("%x %X", time_struct)
    return formatted_time


class NewsScraper:
    def __init__(self, page_url):
        """
        Initialize the NewsScraper object.

        :param page_url: URL of the page to scrape.
        """
        self.url = page_url
        self.page_to_scrape = get_page_to_scrap(page_url)
        self.soup = BeautifulSoup(self.page_to_scrape.text, 'html.parser')
        self.processed_news = {}

    def scrape_news(self):
        """
        Scrape news information from the HTML page and store it in the processed_news dictionary.
        """
        news_containers = self.soup.find_all('li', class_='c-posts__item')

        for container in news_containers:
            news_headline = find_news_headline(container)
            if not news_headline:
                continue
            news_date = find_news_date(container)
            news_link = find_news_link(container)

            if news_headline not in self.processed_news.keys():
                self.processed_news[news_headline] = {'date': news_date, 'link': news_link}

    def print_news(self):
        """
        Print the processed news information.
        """
        print(f"\nDownloaded: {get_current_time()}\n")
        for news_headline, news_info in self.processed_news.items():
            news_date = news_info.get('date')
            news_link = news_info.get('link')
            print(f"[{news_date}] {news_headline}\n"
                  f"Link: {news_link}")
            print('-' * 100)
