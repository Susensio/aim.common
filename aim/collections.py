from typing import Iterable


def count(elements: Iterable) -> dict:
    """
    >>> data = ['A','B','A']
    >>> counter = count(data)
    >>> counter['A']
    2
    >>> counter['B']
    1
    """
    counter = {}
    for el in elements:
        counter[el] = counter.get(el, 0) + 1
    return counter


def most_frequent(elements: Iterable):
    """
    >>> data = ['A', 'B', 'A']
    >>> most_frequent(data)
    'A'

    >>> data = ['A', 'B', 'A', 'B', 'C', 'B']
    >>> most_frequent(data)
    'B'

    >>> data = (_ for _ in ['Hearts', 'Spades', 'Diamonds', 'Diamonds', 'Clubs'])
    >>> most_frequent(data)
    'Diamonds'
    """
    counter = count(elements)
    return max(counter, key=counter.get)
