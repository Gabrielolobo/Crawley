# Concrete Hostgator Crawler
from bs4 import BeautifulSoup

from .crawler import Crawler


class HostgatorCrawler(Crawler):

    URL = "https://www.hostgator.com/vps-hosting"

    def _parse(self, main_page):
        soup = BeautifulSoup(main_page, 'html.parser')
        # cpu = soup.find CPU
        # memory = soup.find MEMORY
        # storage = soup.find STORAGE
        # band = soup.find BANDWIDTH
        # price = soup.find PRICE[$/mo]

        return

    def _get(self):
        return
