def add(a, b):
    """
    Add two numbers and return the result.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract b from a and return the result.

    Args:
        a: First number
        b: Second number

    Returns:
        The difference between a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers and return the result.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide a by b and return the result.

    Args:
        a: First number
        b: Second number

    Returns:
        The quotient of a and b

    Raises:
        ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
