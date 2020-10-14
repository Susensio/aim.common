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
        rows, cols = arg
        try:
            return [row[cols] for row in super().__getitem__(rows)]
        except TypeError:
            return super().__getitem__(rows)[cols]

    def __str__(self):
        return "".join(["[\n", *[str(row)+",\n" for row in self], "]"])

    def __repr__(self):
        return f"Matrix({super().__repr__()})"
