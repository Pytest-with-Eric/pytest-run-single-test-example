from typing import List, Dict, Set

class Library:
    def __init__(self):
        self.books: Dict[str, str] = {}  # Dictionary to store books with their authors
        self.authors: Set[str] = set()  # Set to store unique authors

    def add_book(self, title: str, author: str) -> None:
        """Add a book with its title and author."""
        self.books[title] = author
        self.add_author(author)

    def add_author(self, author: str) -> None:
        """Add an author to the library's set of authors."""
        self.authors.add(author)

    def remove_book(self, title: str) -> None:
        """Remove a book by its title."""
        if title in self.books:
            del self.books[title]

    def has_book(self, title: str) -> bool:
        """Check if a book is in the library by its title."""
        return title in self.books

    def find_book(self, search_term: str) -> List[str]:
        """Find books containing a search term in their titles."""
        return [book for book, _ in self.books.items() if search_term in book]

    def find_author(self, search_term: str) -> List[str]:
        """Find authors containing a search term in their names."""
        return [author for author in self.authors if search_term in author]

    def list_books(self) -> Dict[str, str]:
        """List all books with their authors."""
        return self.books
