from random import random
from aim import sorting

test_array = [random() for _ in range(100)]
sorted_array = sorted(test_array)


def test_bubble_sort():
    assert sorting.bubble_sort(test_array) == sorted_array


def test_selection_sort():
    assert sorting.selection_sort(test_array) == sorted_array


def test_merge_sort_slicing():
    assert sorting.merge_sort_slicing(test_array) == sorted_array


def test_merge_sort():
    assert sorting.merge_sort(test_array) == sorted_array
