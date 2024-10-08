class Book:
    def __init__(self, title, author, year):
        """Initializes a Book injstance with title, author and year"""
        self.title = title
        self.author = author
        self.year = year
    def __del__(self):
        """Destructor that is called when an object is deleted."""
        print(f"Deleting {self.title}")
    def __str__(self):
        """Returns a string representation of the Book"""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Returns an official string represntaion of the Book"""
        return f"Book('{self.title}', '{self.author}', {self.year})"