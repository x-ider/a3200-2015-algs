import unittest
import lab11.Evtushenko.square as square


class TestSquare(unittest.TestCase):
    def test_from_site(self):
        arr = [2, 5, 1, 2, 3, 4, 7, 7, 6]
        res = square.calculate(arr)
        exp = 10
        self.assertEqual(res, exp)

    def test_empty(self):
        arr = []
        res = square.calculate(arr)
        exp = 0
        self.assertEqual(res, exp)

    def test_one_column(self):
        arr = [228]
        res = square.calculate(arr)
        exp = 0
        self.assertEqual(res, exp)

    def test_two_columns(self):
        arr = [228, 282]
        res = square.calculate(arr)
        exp = 0
        self.assertEqual(res, exp)

    def test_true_mountain(self):
        arr = [1, 3, 5, 6, 7, 9, 15, 25, 47, 75, 97, 324, 243, 200, 153, 65, 43, 21, 15, 6, 4, 2]
        res = square.calculate(arr)
        exp = 0
        self.assertEqual(res, exp)

    def test_everybody_has_that_one_friend(self):
        arr = [2, 5, 2, 5, 2, 5, 2, 5, 999999999, 5]
        res = square.calculate(arr)
        exp = 3
        self.assertEqual(res, exp)
