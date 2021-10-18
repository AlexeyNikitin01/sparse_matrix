import unittest

from sparse_matrix import SparseMatrix


class MyTestCase(unittest.TestCase):

    def test_from_file(self):
        sparse_matrix = SparseMatrix.from_file('MATRIX.txt')
        self.assertEqual(sparse_matrix._values, [1, 1, 1, 1, 3, 1])
        self.assertEqual(sparse_matrix._cols, [2, 3, 0, 0, 2, 1])
        self.assertEqual(sparse_matrix._rows_pointers, [0, 2, 3, 5, 6])
        self.assertEqual(sparse_matrix._n_cols, 4)
        self.assertEqual(sparse_matrix._n_rows, 4)

    def test_repr(self):
        sparse_matrix = SparseMatrix.from_file('MATRIX.txt')
        self.assertEqual(sparse_matrix.__repr__(), {2: 1, 3: 1, 4: 1, 8: 1, 10: 3, 13: 1, })


if __name__ == '__main__':
    unittest.main()
