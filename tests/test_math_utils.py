"""Unit tests for math utility functions."""

from src.math_utils import add, subtract, multiply, divide


def test_add():
    """Test the add function."""
    assert add(3, 2) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-3, -7) == -10


def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(1, 1) == 0
    assert subtract(0, 5) == -5
    assert subtract(-3, -1) == -2


def test_multiply():
    """Test the multiply function."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    assert multiply(-3, -2) == 6


def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
    assert divide(7, 2) == 3.5
    assert divide(0, 5) == 0
    assert divide(-6, 2) == -3

    # Test division by zero raises an exception
    try:
        divide(5, 0)
        # If we reach this line, no exception was raised
        assert False, "ZeroDivisionError was not raised"
    except ZeroDivisionError:
        # Exception was raised as expected
        pass
