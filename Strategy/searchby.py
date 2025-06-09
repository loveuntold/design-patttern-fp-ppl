from abc import ABC, abstractmethod

class SearchStrategy(ABC):
    @abstractmethod
    def search(self, keyword: str, books: list) -> list:
        pass

class SearchByTitle(SearchStrategy):
    def search(self, keyword: str, books: list) -> list:
        return [b for b in books if keyword.lower() in b['judul'].lower()]

class SearchByAuthor(SearchStrategy):
    def search(self, keyword: str, books: list) -> list:
        return [b for b in books if keyword.lower() in b['penulis'].lower()]

class SearchByCategory(SearchStrategy):
    def search(self, keyword: str, books: list) -> list:
        return [b for b in books if keyword.lower() in b['kategori'].lower()]