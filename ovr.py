from abc import ABCMeta, abstractmethod


class IMatrixInput(metaclass=ABCMeta):
    @abstractmethod
    def sparse_matrix(self):
        pass


class DataInputMatrix(IMatrixInput):
    PATH_TO_FILE = 'MATRIX.txt'

    def __init__(self):
        self._sparse_matrix = None
        with open('MATRIX.txt') as f:
            self._sparse_matrix = [list(map(int, row.split())) for row in f.readlines()]

    def sparse_matrix(self):
        return self._sparse_matrix
