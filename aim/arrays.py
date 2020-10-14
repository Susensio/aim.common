class Matrix(list):
    """Allow 2D matrix slicing numpy style."""

    def __init__(self, iterable):
        try:
            for row in iterable:
                iter(row)
        except TypeError as exc:
            raise TypeError("Expected a nested iterable") from exc

        return super().__init__(iterable)

    def row(self, row_num):
        return self[row_num, :]

    def column(self, col_num):
        return self[:, col_num]

    @property
    def m(self):
        """Number of rows."""
        return len(self.column(0))

    @property
    def n(self):
        """Number of columns."""
        return len(self.row(0))

    @property
    def rows(self):
        for row_num in range(self.m):
            yield self.row(row_num)

    @property
    def columns(self):
        for col_num in range(self.n):
            yield self.column(col_num)

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
