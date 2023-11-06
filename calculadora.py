def soma(x, y):
    """
        Soma x e y

        doctests detectam o erro e caso não exista o programa roda normal, o numero abaixo e o resultado esperado
    >>> soma(10, 20)
    30

    >>> soma(-10, 20)
    10

    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: X precisa ser int ou float
    """
    assert isinstance(x, (int, float)), "X precisa ser int ou float"
    assert isinstance(y, (int, float)), "Y precisa ser int ou float"
    return x + y

def subtrai(x, y):
    """
        Subtrai x e y

        >>> subtrai(10, 5)
        5

        >>> subtrai('10', 5)
        Traceback (most recent call last):
        ...
        AssertionError: X precisa ser int ou float
    """
    assert isinstance(x, (int, float)), "X precisa ser int ou float"
    assert isinstance(y, (int, float)), "Y precisa ser int ou float"
    return x - y

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)