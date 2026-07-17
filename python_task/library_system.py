def add_book(catalog, book_id, title, author, year):
    
    catalog[book_id] = (title, author, year)
def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Book {book_id} borrowed successfully.")
    elif book_id not in catalog:
        print(f"Book {book_id} does not exist in catalog.")
    else:
        print(f"Book {book_id} is already borrowed.")
def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Book {book_id} returned successfully.")
    else:
        print(f"Book {book_id} was not borrowed, nothing to return.")
def register_member(members, member_id):
    if member_id in members:
        print(f"Member {member_id} is already registered. Skipping.")
    else:
        members.add(member_id)
        print(f"Member {member_id} registered successfully.")
def show_available(catalog, borrowed_books):
    print("Available books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"  ID {book_id}: {title} by {author} ({year})")
def main():
    catalog = {}
    borrowed_books = []
    members = set()
    add_book(catalog, 1, "The Hobbit", "J.R.R. Tolkien", 1937)
    add_book(catalog, 2, "Clean Code", "Robert C. Martin", 2008)
    add_book(catalog, 3, "Dune", "Frank Herbert", 1965)
    add_book(catalog, 4, "1984", "George Orwell", 1949)
    register_member(members, 101)
    register_member(members, 102)
    register_member(members, 103)
    register_member(members, 101)  
    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 3)
    return_book(borrowed_books, 1)
    show_available(catalog, borrowed_books)
    print("\nFinal state:")
    print("Borrowed books:", borrowed_books)
    print("Members:", members)
if __name__ == "__main__":
    main()
