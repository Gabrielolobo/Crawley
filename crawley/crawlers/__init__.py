from .vultr import VultrCrawler
from .hostgator import HostgatorCrawler

AVAILABLE_CRAWLERS = {
    HostgatorCrawler.__name__: HostgatorCrawler(),
    VultrCrawler.__name__: VultrCrawler()
}
