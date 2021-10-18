class SparseMatrix:

    def __init__(self, values, cols, rows_pointers, n_cols, n_rows):
        # link to staticmethod from_file
        self._values = values
        self._cols = cols
        self._rows_pointers = rows_pointers
        self._n_cols = n_cols
        self._n_rows = n_rows

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def is_sparse(self) -> bool:
        # return sqrt(self.size_mat_row * self.size_mat_col) > len(self.values)
        pass

    def to_matrix(self) -> list[list[float]]:
        # Создает обычную матрицу из разреженной
        pass

    @staticmethod
    def from_file(path_to_file):
        with open(path_to_file) as f:
            n_rows, n_cols = map(lambda x: int(x), f.readline().split(' '))
            values = []
            cols = []
            rows_pointers = [0, ]
            pointer = 0
            for _ in range(n_rows):
                row = [int(x) for x in f.readline().strip().split()]
                for col in range(n_cols):
                    if row[col] != 0:
                        values.append(row[col])
                        cols.append(col)
                        pointer += 1
                rows_pointers.append(pointer)
        return SparseMatrix(values, cols, rows_pointers, n_cols, n_rows)

    @staticmethod
    def from_matrix(matrix):  # -> SparseMatrix
        # Создает разреженную матрицу из обычной
        pass

    @staticmethod
    def identity(n):  # -> SparseMatrix
        # Создает единичную матрицу NxN
        pass
