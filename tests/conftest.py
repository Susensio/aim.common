import pytest
import random


@pytest.fixture
def random_array_100():
    random.seed(0)
    return [random.random() for _ in range(100)]


@pytest.fixture
def random_array_1000():
    random.seed(0)
    return [random.random() for _ in range(1000)]
