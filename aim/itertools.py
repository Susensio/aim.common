def combinations(iterable, length):
    """Return length subsequences of elements from the input iterable.

    >>> list(combinations([1, 2, 3], 2)) == [{1, 2}, {1, 3}, {2, 3}]
    True
    >>> list(combinations('ABCD',2)) == [{'A', 'B'}, {'A', 'C'}, {'A', 'D'},\
        {'B', 'C'}, {'B', 'D'}, {'C', 'D'}]
    True
    """
    if length == 0:
        yield {}
    elif length == 1:
        for item in iterable:
            yield {item}
    else:
        for i, item in enumerate(iterable):
            for items in combinations(iterable[i+1:], length-1):
                yield {item, *items}


def powerset(items):
    """ Set of all subsets

    >>> list(powerset([1, 2, 3])) == [{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]
    True
    """
    for n in range(len(items) + 1):
        yield from combinations(items, n)
