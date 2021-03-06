def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    x = n // 2
    while x > 1:
        if n % x == 0:
            return False
        else:
            x -= 1
        return True