from searchby import SearchByTitle, SearchByAuthor, SearchByCategory
from searchby import SearchStrategy

class BookSearch:
    def __init__(self, strategy: SearchStrategy):
        self.strategy = strategy

    def search(self, keyword: str, books: list) -> list:
        return self.strategy.search(keyword, books)

if __name__ == "__main__":
    # Contoh penggunaan
    books = [
        {"judul": "National Geographic - Supercomputer", "penulis": "Leo", "kategori": "Science"},
        {"judul": "Harry Potter", "penulis": "Budi", "kategori": "Fiksi"},
        {"judul": "Lord of The Ring", "penulis": "Asep", "kategori": "Fiksi"},
        {"judul": "Jago Ngoding", "penulis": "Darryl", "kategori": "Tech"},
    ]

    engine = BookSearch(SearchByTitle())
    print("Cari berdasarkan judul:", engine.search("super", books))

    engine = BookSearch(SearchByAuthor())
    print("Cari berdasarkan penulis:", engine.search("asep", books))

    engine = BookSearch(SearchByCategory())
    print("Cari berdasarkan kategori:", engine.search("fi", books))