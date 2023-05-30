# Abstract Crawler

from abc import ABC, abstractmethod


class Crawler(ABC):
    def __init__(self) -> None:
        self.url = self.URL

    def __init_subclass__(cls) -> None:
        assert cls.URL

    @abstractmethod
    def _parse(self):
        pass

    @abstractmethod
    def _get(self):
        pass

    def run(self):
        main_page = self._get()
        results = self._parse(main_page)
        return results
