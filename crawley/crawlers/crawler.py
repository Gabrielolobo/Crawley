# Abstract Crawler

from abc import ABC, abstractmethod


class Crawler(ABC):
    def __init__(self):
        self.url = self.URL

    @abstractmethod
    def _parse(self):
        pass

    @abstractmethod
    def _get(self):
        pass
