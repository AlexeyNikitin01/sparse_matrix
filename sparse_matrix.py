from math import sqrt


class SparseMatrix:
    PATH_TO_FILE = 'MATRIX.txt'
    PATH_TO_FILE_TWO = 'MATRIX_TWO.txt'

    def __init__(self):
        pass

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

    def increase_on_vector(self, vector_b: list) -> list:
        # умноженеие на вектор
        pass

    def to_matrix(self) -> list[list[float]]:
        # Создает обычную матрицу из разреженной
        pass

    @staticmethod
    def from_file(path_to_file):
        with open(path_to_file) as f:
            val = []
            cols = []
            rows_pointers = [0, ]
            point = 0
            for line in f:
                num = line.strip().split()
                for count, j in enumerate(num):
                    if int(j) > 0:
                        val.append(int(j))
                        cols.append(count)
                        point += 1
                rows_pointers.append(point)
        SparseMatrix._sparse_matrix = [val, cols, rows_pointers]
        return SparseMatrix._sparse_matrix

    @staticmethod
    def from_matrix(matrix): # -> SparseMatrix
        # Создает разреженную матрицу из обычной
        pass

    @staticmethod
    def identity(n): # -> SparseMatrix
        # Создает единичную матрицу NxN
        pass
