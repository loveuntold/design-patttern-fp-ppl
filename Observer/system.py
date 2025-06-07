class LibrarySystem:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

    def add_book(self, book_title):
        print(f"[SYSTEM] Buku baru ditambahkan: {book_title}")
        self.notify_observers(f"Buku baru tersedia: {book_title}")

    def generate_report(self, report_type):
        print(f"[SYSTEM] Laporan {report_type} berhasil dibuat.")
        self.notify_observers(f"Laporan {report_type} tersedia.")
