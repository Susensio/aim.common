from aim.arrays import Matrix
import pytest


@pytest.fixture
def simple_matrix():
    return Matrix([[1, 2], [3, 4]])


@pytest.fixture
def rectangular_matrix():
    return Matrix([[1, 2], [3, 4], [5, 6]])


def test_slice_row(simple_matrix):
    assert simple_matrix[0, :] == [1, 2]


def test_slice_column(simple_matrix):
    assert simple_matrix[:, 0] == [1, 3]


def test_getitem_slicing(simple_matrix):
    assert simple_matrix[0, 0] == 1


def test_getitem_normal(simple_matrix):
    assert simple_matrix[0][0] == 1


def test_submatrix(simple_matrix):
    assert simple_matrix[0:1, 0:1] == [[1]]


def test_str_matrix(simple_matrix):
    assert str(simple_matrix) == "[\n[1, 2],\n[3, 4],\n]"


def test_matrix_is_iterable():
    with pytest.raises(TypeError):
        Matrix(None)
        Matrix([None])


def test_matrix_dimmensions(rectangular_matrix):
    assert rectangular_matrix.m == 3
    assert rectangular_matrix.n == 2
    assert rectangular_matrix.size == (3, 2)


def test_matrix_columns(simple_matrix):
    assert list(simple_matrix.columns) == [[1, 3], [2, 4]]


def test_matrix_row(simple_matrix):
    assert list(simple_matrix._row(1)) == [3, 4]
