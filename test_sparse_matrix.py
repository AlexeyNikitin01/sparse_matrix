import unittest

from sparse_matrix import SparseMatrix


class MyTestCase(unittest.TestCase):

    def test_from_file(self):
        check = SparseMatrix
        from_file = check.from_file('MATRIX.txt')
        self.assertEqual(from_file._val, [1, 1, 1, 1, 3, 1])
        self.assertEqual(from_file._cols, [2, 3, 0, 0, 2, 1])
        self.assertEqual(from_file._rows_pointers, [0, 2, 3, 5, 6])
        self.assertEqual(from_file._n_cols, 4)
        self.assertEqual(from_file._n_rows, 4)


if __name__ == '__main__':
    unittest.main()
