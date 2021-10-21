from math import sqrt


class SparseMatrix:

    def __init__(self, values, cols, rows_pointers, n_cols, n_rows):
        # link to staticmethod from_file
        self._values = values
        self._cols = cols
        self._rows_pointers = rows_pointers
        self._n_cols = n_cols
        self._n_rows = n_rows

    def __str__(self):
        string_repr = []
        for i in range(self._n_rows):
            intermediate_result = []
            cols = self._cols[self._rows_pointers[i]:self._rows_pointers[i + 1]]
            values = self._values[self._rows_pointers[i]:self._rows_pointers[i + 1]]
            values = iter(values)
            for col in range(self._n_cols):
                if col in cols:
                    intermediate_result.append(next(values))
                else:
                    intermediate_result.append(0)
            string_repr.append(intermediate_result)
        return string_repr

    def __repr__(self):
        internal_repr = {}
        for i in range(len(self._rows_pointers) - 1):
            num_in_row = self._rows_pointers[i + 1] - self._rows_pointers[i]
            cols = self._cols[self._rows_pointers[i]:self._rows_pointers[i + 1]]
            values = self._values[self._rows_pointers[i]:self._rows_pointers[i + 1]]
            for j in range(num_in_row):
                unique_index = i * self._n_cols + cols[j]
                internal_repr[unique_index] = values[j]
        return internal_repr

    def __add__(self, other):
        sparse_matrix_2 = other
        assert (sparse_matrix_2._n_cols == self._n_cols) and \
               (sparse_matrix_2._n_rows == self._n_rows)
        add_rows_pointers = [0, ]
        add_values = []
        add_cols = []
        pointer = 0
        for i in range(self._n_rows):
            values_2 = sparse_matrix_2._values[sparse_matrix_2._rows_pointers[i]:sparse_matrix_2._rows_pointers[i+1]]
            values_2 = iter(values_2)
            values_1 = self._values[self._rows_pointers[i]:self._rows_pointers[i+1]]
            values_1 = iter(values_1)
            cols_2 = sparse_matrix_2._cols[sparse_matrix_2._rows_pointers[i]:sparse_matrix_2._rows_pointers[i+1]]
            cols_1 = self._cols[self._rows_pointers[i]:self._rows_pointers[i+1]]
            for col in range(self._n_cols):
                if col in cols_1 and col in cols_2:
                    add_values.append(next(values_1) + next(values_2))
                    add_cols.append(col)
                    pointer += 1
                elif col in cols_1:
                    add_values.append(next(values_1))
                    add_cols.append(col)
                    pointer += 1
                elif col in cols_2:
                    add_values.append(next(values_2))
                    add_cols.append(col)
                    pointer += 1
            add_rows_pointers.append(pointer)
        return add_rows_pointers, add_values, add_cols

    def is_sparse(self) -> bool:
        return sqrt(self._n_rows * self._n_cols) > len(self._values)

    def to_matrix(self) -> list[list[float]]:
        sparse_matrix = []
        for i in range(self._n_rows):
            row = []
            cols = self._cols[self._rows_pointers[i]:self._rows_pointers[i+1]]
            values = self._values[self._rows_pointers[i]:self._rows_pointers[i+1]]
            values = iter(values)
            for col in range(self._n_cols):
                if col in cols:
                    row.append(next(values))
                else:
                    row.append(0)
            sparse_matrix.append(row)
        return sparse_matrix

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
    def from_matrix(matrix):
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        values = []
        cols = []
        rows_pointers = [0, ]
        pointer = 0
        for row in range(n_rows):
            for col in range(n_cols):
                if matrix[row][col]:
                    values.append(matrix[row][col])
                    cols.append(col)
                    pointer += 1
            rows_pointers.append(pointer)
        return SparseMatrix(values, cols, rows_pointers, n_cols, n_rows)

    @staticmethod
    def identity(n):
        n_rows, n_cols = n, n
        values = [1] * n
        cols = [x for x in range(n)]
        rows_pointers = [x for x in range(n + 1)]
        return SparseMatrix(values, cols, rows_pointers, n_cols, n_rows)
