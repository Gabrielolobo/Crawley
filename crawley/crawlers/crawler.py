# Abstract Crawler
from abc import ABC, abstractmethod
from .result import Result


class Crawler(ABC):
    def __init__(self):
        self.url = self.URL

    def __init_subclass__(cls, *args, **kwargs):
        assert cls.URL

    @abstractmethod
    def _parse(self, main_page) -> list[Result]:
        pass

    @abstractmethod
    def _get(self):
        pass

    def run(self) -> list[Result]:
        main_page = self._get()
        results = self._parse(main_page)
        return results
