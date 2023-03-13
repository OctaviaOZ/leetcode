def divide(num_1: float, num_2: float) -> float:
    """
    >>> divide(5, 2)
    2.5
    >>> divide(20, 3)
    6.67
    >>> divide(3, 3)
    1.0
    >>> divide(1, 0)
    ZeroDivisionError('division by zero')
    >>> divide("1", "2")
    TypeError("unsupported operand type(s) for /: 'str' and 'str'")
    >>> divide("gg", 2)
    TypeError("unsupported operand type(s) for /: 'str' and 'int'")
    """
    try:
        val = round(num_1 / num_2, 2)
        return val
    except (ZeroDivisionError, TypeError) as e:
        return e


if __name__ == "__main__":
    print(divide(1, 1000))

    import doctest

    doctest.testmod()

