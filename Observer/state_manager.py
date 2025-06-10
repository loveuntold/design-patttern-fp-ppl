class StateManager:
    def __init__(self):
        self.subscribers = []
        self.user_books = {}

    def subscribe(self, callback):
        self.subscribers.append(callback)

    def notify(self, user_id, books, event_type):
        for callback in self.subscribers:
            callback(user_id, books, event_type)

    def borrow_book(self, user_id, book):
        self.user_books.setdefault(user_id, []).append(book)
        self.notify(user_id, self.user_books[user_id], event_type="borrow")

    def return_book(self, user_id, book_id):
        if user_id in self.user_books:
            self.user_books[user_id] = [
                b for b in self.user_books[user_id] if b["id"] != book_id
            ]
            self.notify(user_id, self.user_books[user_id], event_type="return")
