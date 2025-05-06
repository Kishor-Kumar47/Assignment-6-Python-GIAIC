# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.



class Book:
    # Class variable shared across all instances
    total_books = 0
# total_books is a class variable, shared by all Book instances.

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Call class method to update count

    @classmethod
    def increment_book_count(cls):                           #Kishor Kumar
        cls.total_books += 1
# Example usage
book1 = Book("Python for Beginners")
book2 = Book("Data Science Essentials")
book2 = Book("Data Science Essentials")
book2 = Book("Data Science Essentials")

print("Total number of books:", Book.total_books)
