import unittest

from sparse_matrix import SparseMatrix


class MyTestCase(unittest.TestCase):
    def test_increase_on_vector(self):
        check = SparseMatrix()
        increase_on_vector = check.increase_on_vector([1, 2, 3, 1])
        self.assertEqual(increase_on_vector, [4, 1, 4, 2])

    def test_matrix_add(self):
        check = SparseMatrix()
        second_matrix = [[0, 0, 1, 1],
                         [1, 0, 0, 0],
                         [1, 0, 1, 0],
                         [0, 1, 0, 0]]
        add_matrix = check.matrix_add(second_matrix)
        result_matrix = [[0, 0, 2, 2],
                         [2, 0, 0, 0],
                         [2, 0, 2, 0],
                         [0, 2, 0, 0]]

        return self.assertEqual(add_matrix, result_matrix)


if __name__ == '__main__':
    unittest.main()
