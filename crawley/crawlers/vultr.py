# Concrete Vultr Crawler

from typing import List
import requests
from bs4 import BeautifulSoup
# import pdb

from .crawler import Crawler
from .result import Result


class VultrCrawler(Crawler):

    URL = "https://www.vultr.com/products/bare-metal/#pricing"

    def _parse(self, main_page) -> List[Result]:
        if main_page is None:
            return []

        soup = BeautifulSoup(main_page, 'html.parser')
        cards = soup.find_all("a", "package package--boxed package--shadow")

        results = []

        for card in cards:
            cpus = card.find("h3", "package__title h6 center").text.strip()
            price = card.find("span", "price__value").text.strip()
            ram = self.clean_element(card, 'li:-soup-contains("Memory")')
            ssd = self.clean_element(card, 'li:-soup-contains("SSD")')
            band = self.clean_element(card, 'li:-soup-contains("Bandwidth")')

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
            print("Vultr Successful Request")
            return response.text
        else:
            print("Vultr HTTPS Error", response.status_code)
