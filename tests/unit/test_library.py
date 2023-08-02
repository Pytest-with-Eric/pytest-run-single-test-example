import pytest
from library.core import Library

@pytest.mark.add
def test_add_author():
    """Test adding an author."""
    library = Library()
    library.add_author("John Doe")
    assert "John Doe" in library.authors

def test_find_author():
    """Test finding an author by search term."""
    library = Library()
    library.add_author("John Doe")
    library.add_author("Jane Doe")
    assert set(library.find_author("Doe")) == {"John Doe", "Jane Doe"}
