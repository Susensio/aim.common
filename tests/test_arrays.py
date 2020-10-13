from aim.arrays import Matrix
from pytest import fixture


@fixture
def simple_matrix():
    return Matrix([[1, 2], [3, 4]])


def test_slice_row(simple_matrix):
    assert simple_matrix[0, :] == [1, 2]


def test_slice_column(simple_matrix):
    assert simple_matrix[:, 0] == [1, 3]


def test_getitem(simple_matrix):
    assert simple_matrix[0, 0] == 1


def test_submatrix(simple_matrix):
    assert simple_matrix[0:1, 0:1] == [[1]]
