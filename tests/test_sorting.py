import random
from aim import sorting
from pytest import fixture


@fixture
def random_array_100():
    random.seed(0)
    return [random.random() for _ in range(100)]


@fixture
def random_array_1000():
    random.seed(0)
    return [random.random() for _ in range(1000)]


def test_bubble_sort(random_array_1000):
    assert sorting.bubble_sort(random_array_1000) == sorted(random_array_1000)


def test_selection_sort(random_array_1000):
    assert sorting.selection_sort(random_array_1000) == sorted(random_array_1000)


def test_merge_sort_slicing(random_array_1000):
    assert sorting.merge_sort_slicing(random_array_1000) == sorted(random_array_1000)


def test_merge_sort(random_array_1000):
    assert sorting.merge_sort(random_array_1000) == sorted(random_array_1000)
