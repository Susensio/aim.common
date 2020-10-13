class Matrix(list):
    """Allow 2D matrix slicing numpy style."""

    def __getitem__(self, arg):
        rows, cols = arg
        try:
            return [row[cols] for row in super().__getitem__(rows)]
        except TypeError:
            return super().__getitem__(rows)[cols]
