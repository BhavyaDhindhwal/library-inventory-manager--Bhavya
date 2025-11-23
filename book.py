class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def __str__(self):
        return self.title + " by " + self.author + " | ISBN: " + self.isbn + " | Status: " + self.status

    def to_line(self):
        return self.title + " | " + self.author + " | " + self.isbn + " | " + self.status

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        return self.status == "available"