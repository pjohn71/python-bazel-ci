"""Unit tests for string utility functions."""
from src.string_utils import reverse_string, is_palindrome, count_vowels


def test_reverse_string():
    """Test the reverse_string function."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"


def test_is_palindrome():
    """Test the is_palindrome function."""
    assert is_palindrome("radar") is True
    assert is_palindrome("A man, a plan, a canal, Panama") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("Race car") is True


def test_count_vowels():
    """Test the count_vowels function."""
    assert count_vowels("hello") == 2
    assert count_vowels("python") == 1
    assert count_vowels("aeiou") == 5
    assert count_vowels("") == 0
    assert count_vowels("bcdfghjklmnpqrstvwxyz") == 0
    assert count_vowels("AEIOU") == 5
