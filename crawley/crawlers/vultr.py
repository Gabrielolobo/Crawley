# Concrete Vultr Crawler
import requests
from bs4 import BeautifulSoup

from .crawler import Crawler
from .result import Result


class VultrCrawler(Crawler):

    URL = "https://www.vultr.com/products/bare-metal/#pricing"

    def _parse(self, main_page) -> list[Result]:
        soup = BeautifulSoup(main_page, 'html.parser')
        cpu = soup.find_all("h3", "package__title h6 center")
        ram = soup.find_all("MEMORY")
        ssd = soup.find_all("STORAGE")
        band = soup.find_all("BANDWIDTH")
        price = soup.find_all("PRICE")

        return [
            Result(
                process_unit=cpu.text,
                memory=ram.text,
                storage=ssd.text,
                transfer=band.text,
                monthly_cost=price.text
            ),
        ]

    def _get(self):
        response = requests.get(
            "https://www.vultr.com/products/bare-metal/#pricing", timeout=0.2)

        if response.status_code == 200:
            return
        else:
            print(response.status_code)
