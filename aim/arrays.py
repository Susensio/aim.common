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
        """Avoid infinite recursion in: rows, columns, m and n."""
        return self[row_num, :]

    def _column(self, col_num):
        """Avoid infinite recursion in: rows, columns, m and n."""
        return self[:, col_num]

    @property
    def rows(self):
        return [self._row(row_num) for row_num in range(self.m)]

    @property
    def columns(self):
        return [self._column(col_num) for col_num in range(self.n)]

    @property
    def m(self):
        """Number of rows."""
        return len(self._column(0))

    @property
    def n(self):
        """Number of columns."""
        return len(self._row(0))

    @property
    def size(self):
        return self.m, self.n

    def __getitem__(self, arg):
        try:
            rows, cols = arg
        except TypeError:   # args not a tuple
            # Allow normal list slicing: matrix[0][0]
            return super().__getitem__(arg)

        try:
            # Handle double slicing: matrix[0:9,0:9]
            # and row slicing:       matrix[0:9, 0]
            return [row[cols] for row in super().__getitem__(rows)]
        except TypeError:
            # Handle column slicing: matrix[0, 0:9]
            # and item selection:    matrix[0, 0]
            return super().__getitem__(rows)[cols]

    def __str__(self):
        return "".join(["[\n", *[str(row)+",\n" for row in self], "]"])

    def __repr__(self):
        return f"Matrix({super().__repr__()})"
