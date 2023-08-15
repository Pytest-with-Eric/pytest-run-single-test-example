## Introduction

Testing is a crucial aspect of software development, as it verifies that the code meets specific requirements and behaves as expected. Often, developers struggle with writing efficient, effective tests that cover various scenarios. In this article, you will explore how to overcome these challenges using Pytest, a popular testing framework in Python. 

By diving deep into testing specific code with Pytest, this guide aims to help developers master different aspects of testing, including how to test individual components, use markers to group tests, and even skip particular tests when necessary. 

Whether you're a beginner or an experienced developer, this article offers a comprehensive look into testing with Pytest to enhance your code quality.

## Objectives of the article

-   Understand the importance of testing in software development.
-   Introduction to Pytest and its features.
-   Learn how to run a single test using different options in Pytest.

## Pytest — Environment Setup

To get started with Pytest, follow these steps:

**Installing Pytest:** Use pip to install pytest:  
``` pip install pytest    ```  
**Dependencies:** Make sure you have the required version of Python     installed. 
**Naming Conventions:** Pytest follows certain naming   conventions for    test files and functions. Typically, test files    should start    with    test_ or end with _test, and test    functions/methods should    start with    test.

## Project Setup
To better understand running individual tests, we'll set up a simple project structure. Here is a class named **Library.** This class represents a basic library system, managing books and authors. You will test tghe functions of this class.
Check the complete [Github code from here](https://github.com/Pytest-with-Eric/pytest-run-single-test-example)

## How to Run a Single Test in Pytest
To run a single test in pytest, you would need to do the following steps.

### Creating Tests for the Library Class
Testing a class in Python involves writing separate test functions to check different methods of the class. In this scenario, the **Library class** is being tested.

Here is a complete code of Library class
```python
from typing import List, Dict, Set  
  
class Library:  
    def __init__(self):  
        self.books: Dict[str, str] = {}  # Dictionary to store books with their authors  
  self.authors: Set[str] = set()  # Set to store unique authors  
  
  def add_book(self, title: str, author: str) -> None:  
        """Add a book with its title and author."""  
  self.books[title] = author  
  self.add_author(author)  
  
    def find_book(self, search_term: str) -> List[str]:  
        """Find books containing a search term in their titles."""  
  return [book for book, _ in self.books.items() if search_term in book]  
  
    def list_books(self) -> Dict[str, str]:  
        """List all books with their authors."""  
  return self.books
```

### Creating a Test File

The tests are stored in a separate files, typically in a directory named tests. Pytest will automatically discover these tests due to the **test_** prefix in the filename and function names.

### Testing the add_book Method

This test function checks the add_book method of the Library class:
```python
from library import Library  
  
def test_add_book():  
library = Library()  
library.add_book("Python 101", "John Doe")  
assert  library.has_book("Python 101") == True
```
Here's what the code does:

-   Imports the Library class. 
-   Defines a test function test_add_book.    
-   Inside the test, an instance of Library is created.
-   The add_book method is called to add a book.    
-   The assert statement checks that the book has been added by calling the has_book method.

### Testing the remove_book Method

Similar to the previous test, this function checks the remove_book method:
```python
def test_remove_book():  
library = Library()  
library.add_book("Python 101", "John Doe")  
library.remove_book("Python 101")  
assert  library.has_book("Python 101") == False
```  

The flow is similar, but this time it checks that a book can be removed correctly.
## Running the Tests

After writing the tests, you can run them using pytest. Here's how:
### Run Tests in a Module

To run all tests in a specific file (module), use the following command:
```python
 pytest tests/unit/test_library.py
```

  **![](https://lh5.googleusercontent.com/xB9EDfd8na7K8BnPJloAz0r6I_d30Wu-POw7nplIFPn27bRiuVt5uOKetzYTZmvTqJjuS18RuZMd1NQ8CnDTvG3dUtOD1Nwr15Cg-wzpDIaJxTc9Zni2ldntBTjkN1X-KPbzB3KPf-8m0qo6SAyW0wY)**

### Run Tests in a Directory

To run all tests within a directory, use:
```python
pytest tests
```
This will find and run all tests in the tests directory.
**![](https://lh3.googleusercontent.com/0erzeB7Asu0N3Xv74vSse5T1KNlSDWIkn3WAFH1a2jiZOPqaXzow88IgFpA3T4JSLu1chgnnsonojQGoUJkXWIZdSu5mnMZ8ixSQ_lIYNEYTRDkhdqn16ZJx57GkDqqj0RgoyJSrRZCs2NyxBQ6OhzU)**

### Run Tests by Node IDs

To run a specific test function, you can use the test's "**node ID**", which is essentially its path:
```python
pytest tests/unit/test_books.py::test_add_book
```
**![](https://lh6.googleusercontent.com/TjaD62M7XoRiuLoU7-iF9RGtlrM3PxatJdsVkzxWQmLey92PedocchuRVPFLmwAnIgnCKF0JnLXb4kg-h4PZhPlYE1N9Y-02Skw2b33CkPTmtIeciU2-Ozx1ZbeJPxi38jHFABP4dVzSM6h9hCd38f4)**
This command runs only the test_add_book function in the specified file.

These commands control what tests to run, allowing you to focus on specific areas of your code, which can be particularly useful during development and debugging.

## Run Tests by Marker Expressions:

In Pytest, you can assign markers to your test functions using the **@pytest.mark** decorator. Markers are used to categorize tests and allow you to run specific groups of tests based on those markers. This is especially useful when you have different types of tests, such as fast and slow tests, and you want to run them selectively.

To run tests based on marker expressions, you use the **-m** flag followed by the marker name. 

### Basic Example

 Let's say we have some math-related tests and some tests related to string transformations. We can create markers for these groups.
 ```python 
import pytest

@pytest.mark.math
def test_addition():
    assert 1 + 1 == 2

@pytest.mark.math
def test_subtraction():
    assert 5 - 3 == 2

@pytest.mark.string
def test_lowercase_string():
    assert "Hello".lower() == "hello"

@pytest.mark.string
def test_uppercase_string():
    assert "world".upper() == "WORLD"
```
The provided code uses the pytest framework to create and categorize tests. It marks two test functions (`test_addition` and `test_subtraction`) as related to math operations and two others (`test_lowercase_string` and `test_uppercase_string`) as string-related. Each test checks a specific operation's outcome (e.g., addition, subtraction, string transformations) using assert statements. Marking helps organize and group tests, making it easy to run specific sets of tests based on their purpose.
### Running Tests with Labels
Once you've added these labels, you can run tests based on their labels.

#### Output: Run Only Math Tests

If you want to run only the math tests, you can use:
```bash
pytest -m math
```
**![](https://lh4.googleusercontent.com/Vtvu8KZCvS4T4DqKAI1lFZovydX4zEbPbqFDzvefhoV9IVi3Z6W3CC2SdACduRGJrszyXuLVldbzyB3_V0Bg9tJxC7w95n_y7V5xg1j6l7KV2NpSjcvUIAO5yL5NXpWf9saM0afrcFJ5U358LZVfo_0)**
### Complex Example
This code demonstrates a test for adding a book to a library using Pytest. The test function is marked as 'slow' to indicate it's a slow-running test. It creates a Library instance, adds a book, and checks if the book is added correctly. If the assertion passes, the test is successful; otherwise, it fails.
#### Example: Adding a new Book
```python
  
@pytest.mark.slow # Marking this test as 'slow'pytest -m slow  
def test_add_book():  
    """Test adding a book."""  
  library = Library()  
    library.add_book("Python for Beginners", "John Doe")  
    assert library.has_book("Python for Beginners") == True
```
#### Output: Run Only Slow Tests
In your example, you mentioned running tests marked as **slow**, so you would execute the following command:
```python
pytest -m slow
```
**![](https://lh6.googleusercontent.com/Hwtvi2-mwkyVB21qYNBUvjZcmLpnXIGYEaV5btmvHYUe0TmdeKM7GV6qgaRT7F-B7eNbhdHik45UeLXqWXFiqg1p6UEfe6IPSJ-RlllGPBtogvMF-70PEEGBrTPVIshdeC8obm-4BUXP1Th7hi1Zcb8)**

## If You Want to Skip a Test

There may be situations where you want to skip a particular test. Maybe the test is for a feature that's not ready yet, or you're dealing with a known bug that you don't want to test at the moment. In pytest, skipping a test is simple and can be done using a decorator.

Here's how you can do it:

-   Import the pytest module: You'll need to have pytest imported in your test file.
-   Use the pytest.mark.skip decorator: You can add this line above the test function you want to skip.
    

#### Example: Skipping a Test
```python
import pytest   
@pytest.mark.skip  
def test_list_books():  
    """Test listing all books with authors."""  
  library = Library()  
    library.add_book("Python for Beginners", "John Doe")  
    library.add_book("Advanced Python", "Jane Doe")  
    assert library.list_books() == {"Python for Beginners": "John Doe", "Advanced Python": "Jane Doe"}
```
When pytest runs, it will see the **@pytest.mark.skip** line and know that it should skip this test.
#### Output
**![](https://lh6.googleusercontent.com/FVbErrnNii30enxpBgGOhLQTRPY5v2Fxh83emeJjRxTZHBqANfxN1sF1npojGyydBFR3Qr0iD6Ql1N643o_LujeCTTSd4PhHtZUHpAmRERIH1EkYsmanfb8D0T0mocnWO3QmkQBSKb24_osMvjkVq7s)**

  



You can also add a reason for skipping the test like this:
```python
import pytest  
@pytest.mark.skip (reason="Skipping this test for now because of XYZ reason.")  
def test_list_books():  
    """Test listing all books with authors."""  
  library = Library()  
    library.add_book("Python for Beginners", "John Doe")  
    library.add_book("Advanced Python", "Jane Doe")  
    assert library.list_books() == {"Python for Beginners": "John Doe", "Advanced Python": "Jane Doe"}
```
When you run the tests, pytest will show that this test has been skipped and include the reason why.
**![](https://lh3.googleusercontent.com/7pt879TW1rbmYc4w4OagrxP_cbI7qNGzcRhn9Td3TmI1wKFxMR84_MSSg_zaelCoVQ3p_ygYRzcydgHpOEDMhVnBi9mrKy3ne7ZeM0JSWvwVnp-rszddFrPgTzQIy9i4mg1Qt9n0hT2-jk6J74ceWEw)**

You can find more information on skipping tests [here](https://pytest-with-eric.com/pytest-best-practices/pytest-skip-test/).

## Conclusion


To sum up, this article has provided you with a comprehensive understanding of the Pytest framework and its powerful features.

You've gained insight into setting up the testing environment, creating and running tests, and utilizing markers to categorize and selectively execute tests. 

As you continue to explore and utilize Pytest, you'll be equipped to write better code, improve the quality of your software, and become a more confident developer. 

Remember that testing isn't just a process – it's a mindset that empowers you to deliver higher quality solutions to your users.

If you have questions, ideas for improvement, or specific topics you'd like to learn more about, don't hesitate to reach out via various channels like Twitter, GitHub, or Email. Keep building and testing with Pytest – the sky's the limit!


## Additional Reading

-   [More on Pytest](https://pytest-with-eric.com/)
-   [Learn Python](https://www.python.org/about/gettingstarted/)
