import json

class Book:
    def __init__(self, title, author, isbn, status='available'):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def issue(self):
        if self.status == 'available':
            self.status = 'issued'
            return True
        return False

    def return_book(self):
        if self.status == 'issued':
            self.status = 'available'
            return True
        return False

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'status': self.status
        }

class LibraryInventory:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        # Check if ISBN already exists
        if any(b.isbn == book.isbn for b in self.catalog):
            return False  # ISBN not unique
        self.catalog.append(book)
        return True

    def search_by_title(self, title):
        return [book for book in self.catalog if title.lower() in book.title.lower()]

    def search_by_isbn(self, isbn):
        return [book for book in self.catalog if book.isbn == isbn]

    def display_books(self):
        return [book.to_dict() for book in self.catalog]

def save_catalog(catalog, filename):
    with open(filename, 'w') as f:
        json.dump([book.to_dict() for book in catalog], f)

def load_catalog(filename):
    try:
        with open(filename, 'r') as f:
            book_dicts = json.load(f)
            return [Book(**d) for d in book_dicts]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON in catalog file. Starting with empty catalog.")
        return []

def main():
    library = LibraryInventory()
    library.catalog = load_catalog('library.json')

    while True:
        print("1. Add Book\n2. Issue Book\n3. Return Book\n4. Search Book\n5. Display All\n6. Exit")
        choice = input("Enter choice: ").strip()

        if choice == '1':
            title = input("Title: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            author = input("Author: ").strip()
            if not author:
                print("Author cannot be empty.")
                continue
            isbn = input("ISBN: ").strip()
            if not isbn:
                print("ISBN cannot be empty.")
                continue
            book = Book(title, author, isbn)
            if library.add_book(book):
                print("Book added.")
            else:
                print("Book with this ISBN already exists.")
        elif choice == '2':
            isbn = input("ISBN to issue: ").strip()
            if not isbn:
                print("ISBN cannot be empty.")
                continue
            books = library.search_by_isbn(isbn)
            if books:
                if books[0].issue():
                    print("Book issued.")
                else:
                    print("Book is already issued.")
            else:
                print("Book not found.")
        elif choice == '3':
            isbn = input("ISBN to return: ").strip()
            if not isbn:
                print("ISBN cannot be empty.")
                continue
            books = library.search_by_isbn(isbn)
            if books:
                if books[0].return_book():
                    print("Book returned.")
                else:
                    print("Book is not issued.")
            else:
                print("Book not found.")
        elif choice == '4':
            title = input("Title to search: ").strip()
            if not title:
                print("Title cannot be empty.")
                continue
            books = library.search_by_title(title)
            if books:
                for book in books:
                    print(book.to_dict())
            else:
                print("No books found with that title.")
        elif choice == '5':
            books = library.display_books()
            if books:
                for book in books:
                    print(book)
            else:
                print("No books in catalog.")
        elif choice == '6':
            save_catalog(library.catalog, 'library.json')
            print("Catalog saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
   