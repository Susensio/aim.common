class Matrix(list):
    """Allow 2D matrix slicing numpy style."""

    def __init__(self, iterable):
        try:
            for row in iterable:
                iter(row)
        except TypeError as exc:
            raise TypeError("Expected a nested iterable") from exc

        return super().__init__(iterable)

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
