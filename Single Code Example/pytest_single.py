import pytest

def test_addition():
    assert 1 + 1 == 2

@pytest.mark.slow
def test_multiplication():
    assert 2 * 2 == 4