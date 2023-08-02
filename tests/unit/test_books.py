import pytest
from library.core import Library

@pytest.mark.add
def test_add_book():
    """Test adding a book."""
    library = Library()
    library.add_book("Python for Beginners", "John Doe")
    assert library.has_book("Python for Beginners") == True

def test_remove_book():
    """Test removing a book."""
    library = Library()
    library.add_book("Python for Beginners", "John Doe")
    library.remove_book("Python for Beginners")
    assert library.has_book("Python for Beginners") == False

def test_find_book():
    """Test finding a book by search term."""
    library = Library()
    library.add_book("Python for Beginners", "John Doe")
    library.add_book("Advanced Python", "Jane Doe")
    assert library.find_book("Python") == ["Python for Beginners", "Advanced Python"]

def test_list_books():
    """Test listing all books with authors."""
    library = Library()
    library.add_book("Python for Beginners", "John Doe")
    library.add_book("Advanced Python", "Jane Doe")
    assert library.list_books() == {"Python for Beginners": "John Doe", "Advanced Python": "Jane Doe"}
