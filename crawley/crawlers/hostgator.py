# Concrete Hostgator Crawler

from typing import List
import requests
from bs4 import BeautifulSoup
# import pdb

from .crawler import Crawler
from .result import Result


class HostgatorCrawler(Crawler):

    URL = "https://www.hostgator.com/vps-hosting"

    def _parse(self, main_page) -> List[Result]:
        if main_page is None:
            return []

        soup = BeautifulSoup(main_page, 'html.parser')
        cards = soup.find_all(
            "div", "responsive-columns__column responsive-columns__column--  col-sm-12 col-md-4")

        results = []

        for card in cards:
            cpus = card.find("h3", "card__planName").text.strip()
            price = card.find("a", "card__price rte-modal-link").text.strip()
            ram = self.clean_element(card, 'p:-soup-contains("RAM")')
            ssd = self.clean_element(card, 'p:-soup-contains("SSD")')
            band = self.clean_element(card, 'p:-soup-contains("bandwidth")')

            # pdb.set_trace()

            result = Result(
                cpu=cpus,
                monthly_cost=price,
                memory=ram,
                storage=ssd,
                bandwidth=band,
            )
            results.append(result)

        return results

    def clean_element(self, card, selector):
        elements = card.select(selector)
        cleaned_elements = [element.get_text(
            strip=True) for element in elements]
        return cleaned_elements

    def _get(self):
        response = requests.get(self.URL, timeout=None)

        if response.status_code == 200:
            print("Hostgator Successful Request")
            return response.text
        else:
            print("Hostgator HTTPS Error", response.status_code)
