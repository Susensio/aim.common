from aim.time import timeit
from time import sleep


def test_timeit_output():
    """Function is executed and returned as is."""
    assert timeit(lambda x: x)('test') == 'test'
