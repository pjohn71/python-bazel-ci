"""Module providing a function printing python version."""


def reverse_string(s):
    """
    Reverse a string and return the result.

    Args:
        s: The input string

    Returns:
        The reversed string
    """
    return s[::-1]


def is_palindrome(s):
    """
    Check if a string is a palindrome.

    Args:
        s: The input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    # Clean the string by converting to lowercase and removing non-alphanumeric characters
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]


def count_vowels(s):
    """
    Count the number of vowels in a string.

    Args:
        s: The input string

    Returns:
        The number of vowels in the string
    """
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)
