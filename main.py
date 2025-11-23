import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from library_manager.book import Book
from library_manager.inventory import LibraryInventory

def menu():
    print("")
    print("===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def main():
    library = LibraryInventory()

    while True:
        menu()
        choice = input("Enter choice (1-6): ")

        try:
            if choice == "1":
                title = input("Book Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")

                book = Book(title, author, isbn)
                library.add_book(book)
                print("Book added successfully.")

            elif choice == "2":
                isbn = input("Enter ISBN to issue: ")
                book = library.search_by_isbn(isbn)

                if book is not None and book.issue():
                    library.save_books()
                    print("Book issued successfully.")
                else:
                    print("Book not found or already issued.")

            elif choice == "3":
                isbn = input("Enter ISBN to return: ")
                book = library.search_by_isbn(isbn)

                if book is not None and book.return_book():
                    library.save_books()
                    print("Book returned successfully.")
                else:
                    print("Book not found or not issued.")

            elif choice == "4":
                library.display_all()

            elif choice == "5":
                title = input("Enter title keyword: ")
                results = library.search_by_title(title)
                if len(results) > 0:
                    for b in results:
                        print(b)
                else:
                    print("No matching books found.")

            elif choice == "6":
                print("Exiting program...")
                break

            else:
                print("Invalid input. Please enter 1–6.")

        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()