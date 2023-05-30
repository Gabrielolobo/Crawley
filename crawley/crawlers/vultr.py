# Concrete Vultr Crawler
from bs4 import BeautifulSoup

from .crawler import Crawler
from .result import Result


class VultrCrawler(Crawler):

    URL = "https://www.vultr.com/products/bare-metal/#pricing"

    def _parse(self, main_page) -> list[Result]:
        soup = BeautifulSoup(main_page, 'html.parser')
        cpu = soup.find(CPU)
        ram = soup.find(MEMORY)
        ssd = soup.find(STORAGE)
        band = soup.find(BANDWIDTH)
        price = soup.find(PRICE)

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
        return
