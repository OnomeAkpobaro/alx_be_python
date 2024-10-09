class Book:
    def __init__(self, title, author):
        """Initializes Book instance"""

        self.title = title
        self.author = author
    def __str__(self):
        """String representation of the Book"""

        return f"Book: {self.title} by {self.author}"
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        """Initializes EBook with additional file_size attribute."""
        
        self.file_size = file_size
    def __str__(self):
        """String representation of the EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        """Initializes PrintBook with additional page_count attribute."""

        self.page_count = page_count
    def __str__(self):
        """String representation of PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
    
class Library:
    def __init__(self):
        """Initializes an empty Library"""

        self.books = []
    
    def add_book(self, book):
        """Add a Book, EBook or PrintBook instance to the Library."""
        self.books.append(book)

    def list_books(self):
        """Print details of book in the Library."""
        for book in self.books:
            print(book)



   
        
        
        

