from abc import ABCMeta, abstractmethod

from ovr import IMatrixInput


class OperationWithMatrix(metaclass=ABCMeta):
    @abstractmethod
    def increase_on_vector(self, vector_b: list):
        pass


class IncreaseOnVector(OperationWithMatrix):
    def __init__(self, sparse_matrix: IMatrixInput):
        self.sparse_matrix = sparse_matrix

        self.rows_pointers = [0, ]
        self.values = []
        self.cols = []

    def process_matrix(self):
        matrix = self.sparse_matrix.sparse_matrix()
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]:
                    self.values.append(matrix[i][j])
                    self.cols.append(j)
                    count += 1
            self.rows_pointers.append(count)

    def increase_on_vector(self, vector_b: list) -> list:
        assert max(self.cols)+1 == len(vector_b)

        vector_result = []
        for i in range(len(self.rows_pointers) - 1):
            segment_pointer = self.rows_pointers[i:i + 2]
            row_pointer = segment_pointer[1] - segment_pointer[0]
            result = 0
            for j in range(row_pointer):
                segment_cols = self.cols[segment_pointer[0]:segment_pointer[1]]
                segment_values = self.values[segment_pointer[0]:segment_pointer[1]]
                value_vector = vector_b[segment_cols[j]]
                result += value_vector * segment_values[j]
            vector_result.append(result)
        return vector_result

