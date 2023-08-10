def add(a, b):
    """
    This function adds two numbers and returns the result.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.

    Example:
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
