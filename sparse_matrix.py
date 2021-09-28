class Matrix:
    PATH_TO_FILE = 'MATRIX.txt'

    def __init__(self):
        self._sparse_matrix = None
        with open('MATRIX.txt') as f:
            self._sparse_matrix = [list(map(int, row.split())) for row in f.readlines()]

        self.rows_pointers = [0, ]
        self.values = []
        self.cols = []

        self.vector_result = []

    def process_matrix(self):
        count_for_pointers = 0
        for i in range(len(self._sparse_matrix)):
            for j in range(len(self._sparse_matrix[i])):
                if self._sparse_matrix[i][j]:
                    self.values.append(self._sparse_matrix[i][j])
                    self.cols.append(j)
                    count_for_pointers += 1
            self.rows_pointers.append(count_for_pointers)

    def increase_on_vector(self, vector_b: list) -> list:
        self.process_matrix()
        assert max(self.cols) + 1 == len(vector_b)

        for i in range(len(self.rows_pointers) - 1):
            segment_pointers = self.rows_pointers[i:i + 2]
            row_pointers = segment_pointers[1] - segment_pointers[0]
            result = 0
            for j in range(row_pointers):
                segment_cols = self.cols[segment_pointers[0]:segment_pointers[1]]
                segment_values = self.values[segment_pointers[0]:segment_pointers[1]]
                value_vector = vector_b[segment_cols[j]]
                result += value_vector * segment_values[j]
            self.vector_result.append(result)

        return self.vector_result
