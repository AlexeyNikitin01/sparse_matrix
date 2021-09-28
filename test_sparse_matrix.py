import unittest


from sparse_matrix import Matrix


class MyTestCase(unittest.TestCase):
    def test_increase_on_vector(self):
        check = Matrix()
        increase_on_vector = check.increase_on_vector([1, 2, 3, 1])
        self.assertEqual(increase_on_vector, [4, 1, 4, 2])  # add assertion here


if __name__ == '__main__':
    unittest.main()
