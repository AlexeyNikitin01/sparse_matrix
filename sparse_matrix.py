class SparseMatrix:
    PATH_TO_FILE = 'MATRIX.txt'
    PATH_TO_FILE_TWO = 'MATRIX_TWO.txt'

    def __init__(self, val, cols, rows_pointers, size_mat_col, size_mat_row):
        self._val = val
        self._cols = cols
        self._rows_pointers = rows_pointers
        self.size_mat_col = size_mat_col
        self.size_mat_row = size_mat_row

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def is_sparse(self) -> bool:
        # return sqrt(number_rows * number_cols) > len(self.values)
        pass

    def matrix_add(self): # -> SparseMatrix
        # сложение двух матриц
        return

    def to_matrix(self) -> list[list[float]]:
        # Создает обычную матрицу из разреженной
        pass

    @staticmethod
    def from_file(path_to_file):
        with open(path_to_file) as f:
            size_mat_col = 0
            size_mat_row = 0
            _val = []
            _cols = []
            _rows_pointers = [0, ]
            pointer = 0
            for line in f:
                row = [int(x) for x in line.strip().split()]
                size_mat_col += 1
                for count, val_in_line in enumerate(row):
                    if val_in_line:
                        _val.append(val_in_line)
                        _cols.append(count)
                        pointer += 1
                _rows_pointers.append(pointer)
            size_mat_row += max(_cols)+1
        return SparseMatrix(_val, _cols, _rows_pointers, size_mat_col, size_mat_row)

    @staticmethod
    def from_matrix(matrix): # -> SparseMatrix
        # Создает разреженную матрицу из обычной
        pass

    @staticmethod
    def identity(n): # -> SparseMatrix
        # Создает единичную матрицу NxN
        pass
