from bs4 import BeautifulSoup
import requests
from requests.exceptions import HTTPError
import time


def get_page_to_scrap(p_url):
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
    headline_span = container.find('span', class_='c-posts__headlineText')
    if headline_span:
        return headline_span.get('title')
    else:
        headline_a = container.find('a', class_='c-posts__inner')
        return headline_a.get('title') if headline_a else None


def find_news_date(container):
    news_date = container.findAll('div', class_='c-posts__info')
    return news_date[1].text if news_date else 'Date'


def find_news_link(container):
    news_link = container.find('a', href=True)
    return news_link.get('href') if news_link else None


def get_current_time():
    current_time = time.time()
    time_struct = time.gmtime(current_time)
    formatted_time = time.strftime("%x %X", time_struct)
    return formatted_time


class NewsScraper:
    def __init__(self, page_url):
        self.url = page_url
        self.page_to_scrape = get_page_to_scrap(page_url)
        self.soup = BeautifulSoup(self.page_to_scrape.text, 'html.parser')
        self.processed_news = {}

    def scrape_news(self):
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
        print(f"\nDownloaded: {get_current_time()}\n")
        for news_headline, news_info in self.processed_news.items():
            news_date = news_info.get('date')
            news_link = news_info.get('link')
            print(f"[{news_date}] {news_headline}\n"
                  f"Link: {news_link}")
            print('-' * 100)
