class Matrix(list):
    """Allow 2D matrix slicing numpy style."""

    def __init__(self, iterable):
        try:
            for row in iterable:
                iter(row)
        except TypeError as exc:
            raise TypeError("Expected a nested iterable") from exc

        return super().__init__(iterable)

    def _row(self, row_num):
        """Avoid infinite recursion in: rows, columns, m and n.
        Private method prevents wrong overloading."""
        return self[row_num, :]

    def _col(self, col_num):
        """Avoid infinite recursion in: rows, columns, m and n.
        Private method prevents wrong overloading."""
        return self[:, col_num]

    row = _row
    col = _col

    @property
    def rows(self):
        return [self._row(row_num) for row_num in range(self.m)]

    @property
    def columns(self):
        return [self._col(col_num) for col_num in range(self.n)]

    @property
    def m(self):
        """Number of rows."""
        return len(self._col(0))

    @property
    def n(self):
        """Number of columns."""
        return len(self._row(0))

    @property
    def size(self):
        return self.m, self.n

    def __getitem__(self, arg):
        if not isinstance(arg, tuple):
            # Allow normal list slicing: matrix[0][0]
            return super().__getitem__(arg)

        rows, cols = arg

        if isinstance(rows, slice):
            # Handle double slicing: matrix[0:9,0:9]
            # and row slicing:       matrix[0:9, 0]
            return [row[cols] for row in super().__getitem__(rows)]
        else:
            # Handle column slicing: matrix[0, 0:9]
            # and item selection:    matrix[0, 0]
            return super().__getitem__(rows)[cols]

    def __str__(self):
        return "".join(["[\n", *[str(row)+",\n" for row in self], "]"])

    def __repr__(self):
        return f"Matrix({super().__repr__()})"
