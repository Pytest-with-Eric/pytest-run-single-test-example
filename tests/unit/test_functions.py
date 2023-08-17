from operations.core import add_numbers, multiply_numbers
import pytest

def test_add_positive_numbers():
    assert add_numbers(1, 2) == 3
   
@pytest.mark.end_to_end
def test_add_negative_numbers():
    assert add_numbers(-1, -2) == -3

@pytest.mark.skip
def test_add_numbers_zero():
    assert add_numbers(0, 0) == 0

class TestsUnit:
    @pytest.mark.unit
    def test_multiply_numbers(self):
        assert multiply_numbers(2, 3) == 6

    @pytest.mark.unit
    def test_multiply_numbers_zero(self):
        assert multiply_numbers(0, 0) == 0
