class StateManager:
    def __init__(self):
        self._borrowed_books = {} 
        self._observers = []

    def subscribe(self, observer_func):
        self._observers.append(observer_func)

    def _notify(self, user_id):
        for observer in self._observers:
            observer(user_id, self._borrowed_books.get(user_id, []))

    def borrow_book(self, user_id, book):
        if user_id not in self._borrowed_books:
            self._borrowed_books[user_id] = []
        self._borrowed_books[user_id].append(book)
        self._notify(user_id)

    def return_book(self, user_id, book_id):
        if user_id in self._borrowed_books:
            self._borrowed_books[user_id] = [
                b for b in self._borrowed_books[user_id] if b["id"] != book_id
            ]
            self._notify(user_id)

    def get_borrowed_books(self, user_id):
        return self._borrowed_books.get(user_id, [])
