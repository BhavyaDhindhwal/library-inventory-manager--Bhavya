import os
import logging
from .book import Book

class LibraryInventory:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        logging.info("Book added: " + book.title)
        self.save_books()

    def search_by_title(self, title):
        result = []
        for b in self.books:
            if title.lower() in b.title.lower():
                result.append(b)
        return result

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            for b in self.books:
                print(b)

    def save_books(self):
        try:
            with open(self.filename, "w") as f:
                for book in self.books:
                    f.write(book.to_line() + "\n")
        except Exception as e:
            logging.error("Error saving to text file: " + str(e))

    def load_books(self):
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()
            return

        try:
            with open(self.filename, "r") as f:
                for line in f:
                    parts = line.strip().split(" | ")
                    if len(parts) == 4:
                        title = parts[0]
                        author = parts[1]
                        isbn = parts[2]
                        status = parts[3]
                        book = Book(title, author, isbn, status)
                        self.books.append(book)
        except Exception as e:
            logging.error("Error reading text file: " + str(e))
            print("Could not load books.txt. Starting fresh.")