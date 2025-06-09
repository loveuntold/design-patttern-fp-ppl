from state_manager import StateManager

def ui_update(user_id, books):
    print(f"[UI] Update untuk user {user_id}:")
    for book in books:
        print(f"- {book['title']}")

def logger(user_id, books):
    print(f"[LOG] User {user_id} sekarang meminjam {len(books)} buku")

state = StateManager()
state.subscribe(ui_update)
state.subscribe(logger)

# Simulasi user meminjam dan mengembalikan buku
user_id = 1
state.borrow_book(user_id, {"id": 101, "title": "Python for Beginners"})
state.borrow_book(user_id, {"id": 102, "title": "Design Patterns"})
state.return_book(user_id, 101)
