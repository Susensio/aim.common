from random import random
from aim import sorting, sorting_numpy


def test_bubble_sort(random_array_1000):
    assert sorting.bubble_sort(random_array_1000) == sorted(random_array_1000)


def test_selection_sort(random_array_1000):
    assert sorting.selection_sort(random_array_1000) == sorted(random_array_1000)


def test_merge_sort_slicing(random_array_1000):
    assert sorting.merge_sort_slicing(random_array_1000) == sorted(random_array_1000)


def test_merge_sort(random_array_1000):
    assert sorting.merge_sort(random_array_1000) == sorted(random_array_1000)


def test_selection_sort_numpy(random_array_1000):
    assert sorting_numpy.selection_sort(random_array_1000) == sorted(random_array_1000)


def test_merge_sort_numpy(random_array_1000):
    assert sorting_numpy.merge_sort(random_array_1000) == sorted(random_array_1000)
