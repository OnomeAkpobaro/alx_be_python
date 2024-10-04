class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False            #Private attribute to track availability
    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    def return_book(self):
        """Marks the book as returned and available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    def is_available(self):
        """Checks if the book is available."""
        return not self._is_checked_out
    
class Library:
    def __init__(self):
        self._books = []                       #Private list to store book objects
    def add_book(self, book):
        """Adds a book to the library."""
        self._books.append(book)
    def check_out_book(self, title):
        """Checks out the book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """Returns a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available at the moment.")