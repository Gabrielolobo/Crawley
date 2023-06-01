# Abstract Crawler
from abc import ABC, abstractmethod
from typing import List

from .result import Result


class Crawler(ABC):

    URL = None

    def __init__(self):
        self.url = self.URL

    def __init_subclass__(cls):
        assert cls.URL is not None, f"URL must be defined in {cls.__name__}"

    @abstractmethod
    def _parse(self, main_page) -> List[Result]:
        pass

    @abstractmethod
    def _get(self):
        pass

    def run(self) -> List[Result]:
        main_page = self._get()
        results = self._parse(main_page)
        return results
