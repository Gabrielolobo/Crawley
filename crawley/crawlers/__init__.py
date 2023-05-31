from .vultr import VultrCrawler
from .hostgator import HostgatorCrawler

AVAILABLE_CRAWLERS = {
    VultrCrawler.__name__: VultrCrawler(),
    HostgatorCrawler.__name__: HostgatorCrawler()
}
